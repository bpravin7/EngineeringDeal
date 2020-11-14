from django.urls import path
from .views import signUpApi,loginApi

urlpatterns = [
    path('signUp', signUpApi),
    path('login', loginApi)
]
