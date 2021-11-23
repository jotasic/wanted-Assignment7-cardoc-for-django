import requests
from benedict                        import benedict
from parse                           import parse
from django.db                       import transaction
from django.http                     import Http404
from django.conf                     import settings
from django.contrib.auth             import get_user_model
from rest_framework                  import status
from rest_framework.response         import Response
from rest_framework.viewsets         import GenericViewSet
from rest_framework.permissions      import AllowAny, IsAuthenticated
from rest_framework.decorators       import action
from rest_framework_simplejwt.tokens import RefreshToken

from .models          import UserTire
from .serializers     import SingupSerializers, UserTireRegisterSerializer
from cars.models      import Tire
from cars.serializers import TireSerializers


class UserGenericViewSet(GenericViewSet):
    permission_classes = [AllowAny]
    queryset           = get_user_model()
    lookup_field       = 'id'

    def create(self, request):
        serializer = SingupSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user  = serializer.save()
        token = RefreshToken.for_user(user)
        data  = {'refresh': str(token), 'access': str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], url_path='register-tires', permission_classes=[IsAuthenticated])
    def register_tires(self, request):
        serializer = UserTireRegisterSerializer(data=request.data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        serialized_data = serializer.data
        if len(serialized_data) > settings.MAX_REGISTRATION_TIRE_COUNT or len(serialized_data) == 0:
            return Response({'detail':'The number that can be registered at one time is exceeded or zero.'}, status=status.HTTP_400_BAD_REQUEST)
 
        tire_keys    = ['spec.driving.frontTire.value', 'spec.driving.rearTire.value']
        tire_pattern = '{width:w}/{aspect_ratio:w}R{wheel_size:w}'
        try:
            with transaction.atomic():
                for data in serialized_data:
                    user_obj = get_user_model().objects.get(id=data['id'])
                    response = requests.get(f'{settings.TRIM_API_URL}/{data["trimId"]}', timeout=1)
                    if response.status_code != status.HTTP_200_OK:
                        return Response({'detail':'Dose not exist trimId'}, status=status.HTTP_400_BAD_REQUEST)

                    trim_info = benedict(response.json(), format='json')
                    for tire_key in tire_keys:
                        tire = parse(tire_pattern, trim_info.get_str(tire_key, '').replace(' ', ''))
                        if tire:
                            tire = tire.named
                            tire['width'] = tire['width'] if tire['width'][0].isdigit() else tire['width'][1:]
                            tire_obj, _ = Tire.objects.get_or_create(**tire)
                            UserTire.objects.get_or_create(user=user_obj, tire=tire_obj)

            return Response({'detail':'Success'}, status=status.HTTP_200_OK)

        except get_user_model().DoesNotExist as e:
            return Response({'detail':'Dose not exist user'}, status=status.HTTP_400_BAD_REQUEST)
        except requests.RequestException :
            return Response({'detail':'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['GET'], url_path='tires', permission_classes=[IsAuthenticated])
    def get_users_tires(self, request, id):
        try:
            user  = self.get_object()
            tires = Tire.objects.prefetch_related('usertire_set') \
                                .filter(usertire__user=user)

            serializer = TireSerializers(instance=tires, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Http404:
            return Response({'detail':'Dose not exist user'}, status=status.HTTP_400_BAD_REQUEST)