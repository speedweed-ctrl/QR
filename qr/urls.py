from django.urls import path
from . import views as v

urlpatterns = [
    path('login',v.MyTokenObtainPairView.as_view() , name='login'),
    path('register' , v.registerUser , name='register'),
    path('profile' , v.getUserProfile , name='user profile')
]
