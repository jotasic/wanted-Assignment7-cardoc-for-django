from django.urls                    import path, include
from rest_framework                 import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserGenericViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register('', UserGenericViewSet, basename='users')

urlpatterns = [
    path('', include((router.urls))),
    path('/token', TokenObtainPairView.as_view(), name='token_obtain'),
    path('/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]