from django.db import models

# Create your models here.
class Users(models.Model):
    fullname =models.CharField(max_length=50 )
    phone_no =models.CharField(max_length=50)
    email =models.EmailField(max_length=150)
    password =models.CharField(max_length=150)
    
    def __str__(self):
        return self.fullname 
    
class Profile(models.Model):
    user =models.ForeignKey(Users, on_delete=models.CASCADE ,related_name='user_data')
    user_pic = models.ImageField(upload_to='User/Porfile/%Y/%m/%d',null=True ,blank=True)
    def __str__(self):
        return self.user.fullname + self.user.phone_no 
    
     
    