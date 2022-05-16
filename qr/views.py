
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import participant , scan_data
from .serializer import UserSerializerWithToken,UserSerrializer,particSerializer, scanSerializer
from rest_framework.response import Response

import qrcode

#------------------------login---------------------------------------------
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
#---------------------------------------------------------------------------

#----------------------------------------user views--------------------------
@api_view(['POST'])
def registerUser(request):
    data = request.data
  
    user = User.objects.create(
            
            first_name=data['first_name'],
            last_name = data['last_name'],
            username = data['username'],
            email = data['email'],
            password = make_password(data['password'])
        )
    serializer = UserSerializerWithToken(user , many =False )
    return Response(serializer.data)
    



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializers = UserSerrializer(user, many=False)
    return Response(serializers.data)
#-----------------------------------------------------------------------------------------------------

@api_view(['POST'])
@permission_classes([IsAdminUser])
def register_part(request):
    data=request.data
    user=participant.objects.create(
        name=data['name'],
        last_name=data['last_name'],
        email=data['email'], 
        cin=data['cin']
    )
    serializer=particSerializer(user,many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_scan_data(request,pk):
    data=scan_data.objects.filter(user=pk)
    serializer=scanSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_scan_data_latest(request,pk):
    data=scan_data.objects.filter(user=pk).order_by('last_scan')
    serializer=scanSerializer(data,many=True)
    return Response(serializer.data[-1])

# to be modiied later to give the latest scan of each user
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_all_scans(request):
    data=scan_data.objects.all()
    serializer=scanSerializer(data,many=True)
    return Response(serializer.data)

