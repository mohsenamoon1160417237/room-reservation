from django.urls import path
from .views.registration.normal import NormalUserRegister
from .views.registration.manager import ManagerUserRegister
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [

    path('register/manager/', ManagerUserRegister.as_view(), name='manager_register'),
    path('register/normal/', NormalUserRegister.as_view(), name='normal_register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
]