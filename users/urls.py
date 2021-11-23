from django.urls                    import path, include
from rest_framework                 import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserGenericViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register('users', UserGenericViewSet, basename='users')

urlpatterns = [
    path('', include((router.urls))),
    path('users/token', TokenObtainPairView.as_view(), name='token_obtain'),
    path('users/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]