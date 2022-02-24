from django.contrib import admin
from myapp.models import Product
from myapp.models import Member
from myapp.models import Addressee
from myapp.models import Order

# Register your models here.
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Addressee)
admin.site.register(Order)