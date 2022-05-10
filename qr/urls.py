from django.urls import path
from . import views as v

urlpatterns = [
    path('login',v.MyTokenObtainPairView.as_view() , name='login'),
    path('register' , v.registerUser , name='register'),
    path('profile' , v.getUserProfile , name='user profile'),
    path('participant',v.register_part, name='register participant'),
    path('all_scans',v.get_all_scans,name='all scan data'),
    path('user_scan/<int:pk>',v.get_scan_data,name='user scan data')

]
