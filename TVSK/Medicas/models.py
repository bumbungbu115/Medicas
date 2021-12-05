from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Advisor_Profile(models.Model):
    image=models.ImageField(default="ava_doc.jpg", null=True, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    specialty=models.CharField(max_length=50, null=False, blank=False)
    info=models.CharField(max_length=500, blank=True)
    def __str__(self):
        return str(self.name)
        
class Specialty(models.Model):
   spec=models.CharField(max_length=50, null=False, blank=False)
   def __str__(self):
       return self.spec
   

class Doctor_Profiles(models.Model):
    image=models.ImageField(default="ava_doc.jpg", null=True, blank=False, upload_to="image/")
    title=models.CharField(max_length=50, null=False, blank=False)
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty=models.CharField(max_length=50, null=False, blank=False)
    info=models.CharField(max_length=500, blank=True)
    def __str__(self):
        return str(self.name)


    
class DANH_SACH_SP(models.Model):
    MASP=models.CharField(max_length=10)
    INFO=models.CharField(max_length=1000)
    TENSP=models.CharField(max_length=200)
    PHANLOAI=models.CharField(max_length=100)
    CONGDUNG=models.CharField(max_length=200)
    URL=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.TENSP
    
class INFOSP(models.Model):
    MASP=models.ForeignKey(DANH_SACH_SP,on_delete=models.CASCADE)    
    INFO=models.CharField(max_length=100)
    THUONGHIEU= models.CharField(max_length=100)
    SANXUAT=models.CharField(max_length=50)
    def __str__(self):
        return self.MASP
    

class MOTA(models.Model):
    MASP=models.ForeignKey(DANH_SACH_SP,on_delete=models.CASCADE)
    MOTASP=models.CharField(max_length=1000)
    VIEN=models.CharField(max_length=1000)
    DOITUONG=models.CharField(max_length=1000)
    LIEULUONG=models.CharField(max_length=1000)
    BAOQUAN= models.CharField(max_length=1000)
    THANTRONG=models.CharField(max_length=1000)
    URL=models.CharField(max_length=1000,default="google.com")
    def __str__(self):
        return self.MASP