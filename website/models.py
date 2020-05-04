from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=500)
    post_date=models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
      return self.post 

    def get_absolute_url(self):
      return reverse ('post-detail', kwargs={'pk':self.pk})
