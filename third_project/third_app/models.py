from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.


class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex], max_length=17, blank=False,unique=True)

    profile_pics=models.ImageField(upload_to='profile_pics',blank=True)
    age=models.CharField(blank=False,max_length=2)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    content=models.TextField(max_length=280)
    post_title=models.CharField(max_length=180,blank=False)

    def __str__(self):
        return self.user.username
