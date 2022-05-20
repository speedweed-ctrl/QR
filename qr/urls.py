from os import name
from django.urls import path
from . import views as v

urlpatterns = [
    path('login',v.MyTokenObtainPairView.as_view() , name='login'),
    path('register' , v.registerUser , name='register'),
    path('profile' , v.getUserProfile , name='user profile'),
    path('users',v.get_allUsers , name='all users'),
    path('participant',v.register_part, name='register participant'),
    path('all_scans',v.get_all_scans,name='all scan data'),
    path('user_scan/<int:pk>',v.get_scan_data,name='user scan data'),
    path('user_scan_latest/<int:pk>',v.get_scan_data_latest,name='user scan data'),
    path('add_scann',v.add_scann,name='add a scan')

]
