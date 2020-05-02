from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    image  = models.ImageField(default='default.jpg',upload_to='profile_pics',blank=True)

    def __str__(self):  # image sortig 
        return f'{self.user.username} profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or  img.width > 300 :
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class profile_update(models.Model):  # extara field adding update profile 
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    present_address = models.TextField()
    perment_address = models.TextField()
    bio = models.TextField()
    birthday=models.DateField(auto_now=False, null=True, blank=True)
    contact = models.TextField(max_length=13)

    