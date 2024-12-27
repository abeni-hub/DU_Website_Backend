from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (
    UserAccountViewSet,
    UserCreateViewSet,
    RoleViewSet,
    UserDetail,
)
router = DefaultRouter()
router.register(r'users', UserAccountViewSet)
router.register(r'users/create', UserCreateViewSet, basename='user-create')  # Add the create endpoint
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/jwt/create/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('user-detail/', UserDetail, name= "UserDetail")

]