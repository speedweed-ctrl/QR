
from distutils.command.upload import upload
from pyexpat import model
from django.contrib.auth.models import User
from django.db import models


class participant(models.Model):
    name=models.CharField(max_length=60 , blank=True)
    last_name=models.CharField(max_length=60 , blank=True)
    email=models.EmailField(blank=True)
    qr_code=models.FileField(upload_to='upload/')
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.name)
    
class scan_data(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    number_scans=models.IntegerField(default=0)
    data=models.TextField(default='')
    



    
