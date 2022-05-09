
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import participant , scan_data
from .serializer import UserSerializerWithToken,UserSerrializer,particSerializer
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
    img=qrcode.make(f"name{data['name']} , email:{data['email']} ")
    user=participant.objects.create(
        name=data['name'],
        last_name=data['last_name'],
        email=data['email'],
        qr_code=img.save(f"/home/speedweed/Desktop/QR/backend/upload{data['name']}_{data['last_name']}.png")
    )
    serializer=particSerializer(user,many=False)
    return Response(serializer.data)