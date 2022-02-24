from django.db import models

class Product(models.Model):
    pName =  models.CharField(max_length=100, default='')
    pPrice = models.IntegerField(default=0)
    pImages = models.CharField(max_length=100, default='')
    pDescription = models.TextField(blank=True, default='')
    pQty = models.IntegerField(default=0)
    pro_Image = models.ImageField(upload_to='image/')
    def __str__(self):
        return self.pName

class Member(models.Model):
    cName = models.CharField(max_length=20,null=False)
    cSex = models.CharField(max_length=20,default='M',null=False)
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=50,default='',null=True)
    cPhone = models.CharField(max_length=50,default='',null=True)
    cAddr = models.CharField(max_length=100,default='',null=True)
    cAccount = models.CharField(max_length=100,default='',null=True)
    cPswd = models.CharField(max_length=100,default='',null=True)
    def __str__(self):
        return self.cAccount

class Addressee(models.Model):
    rAccount = models.CharField(max_length=100,default='',null=True)
    rName = models.CharField(max_length=20,null=False)
    rPhone = models.CharField(max_length=50,default='',null=True)
    rAddr = models.CharField(max_length=100,default='',null=True)
    rEmail = models.EmailField(max_length=50,default='',null=True)
    rPay = models.CharField(max_length=100,default='',null=True)
    rGrandtotal = models.IntegerField(default=0)
    rState = models.CharField(max_length=20,default='',null=True)

class Order(models.Model):
    rOrder = models.ForeignKey('Addressee',on_delete=models.CASCADE)
    rProduct = models.CharField(max_length=100, default='')
    rPrice = models.IntegerField(default=0)
    rQty = models.IntegerField(default=0)
    rTotal = models.IntegerField(default=0)
    def __str__(self):
        return self.rOrder

class Seller(models.Model):
    sName = models.CharField(max_length=20,null=False)
    sSex = models.CharField(max_length=20,default='M',null=False)
    sBirthday = models.DateField(null=False)
    sEmail = models.EmailField(max_length=50,default='',null=True)
    sPhone = models.CharField(max_length=50,default='',null=True)
    sAddr = models.CharField(max_length=100,default='',null=True)
    sAccount = models.CharField(max_length=100,default='',null=True)
    sPswd = models.CharField(max_length=100,default='',null=True)
    def __str__(self):
        return self.sAccount
