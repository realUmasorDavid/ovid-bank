from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('', login, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('otp/', otp, name='otp'),
]