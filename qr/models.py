
from django.contrib.auth.models import User
from django.db import models
import qrcode 
from django.core.files import File 
from PIL import Image
from io import BytesIO


class participant(models.Model):
    name=models.CharField(max_length=60 , blank=True)
    last_name=models.CharField(max_length=60 , blank=True)
    email=models.EmailField(blank=True)
    cin=models.IntegerField()
    qr_code=models.FileField(blank=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.name)
    
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(f'{self.name}.{self.last_name}.{self.cin}') 
        canvas = Image.new('RGB', (400, 400), 'white')
        canvas.paste(qrcode_img)
        fname = f'{self.name}_{self.last_name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
        
    
class scan_data(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    scnanned= models.CharField(max_length=100)
    cin= models.CharField(max_length=100 , null=True,blank=True)
    last_scan=models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return str(f"{self.user} scanns")  




    
