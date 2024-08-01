from django.db import models
from booking.models import HolidayTripBook
from booking.models import ServiceBook

# Create your models here.
class Payment(models.Model): #payment products
    order = models.ForeignKey(HolidayTripBook,related_name = "payment",on_delete = models.SET_NULL,null = True)
    ammount = models.FloatField()
    payment_mode = models.CharField(max_length = 100,choices = (('khalti','Khalti'),('esewa','Esewa'),('cod','Cash On Ddelivery')))
    refrence_id = models.CharField(max_length = 4000,unique = True)
    remarks = models.CharField(max_length = 3000,null = True,blank = True)
    status= models.CharField(max_length=255, choices=[
        ('paid','Paid'),
        ('unpaid','Paid'),
        ('half', 'Half Payment'),
        ('cod','Cash On Delivery'),
        ('refunded','Refunded'),
    ],)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class PaymentFail(models.Model):
    order = models.ForeignKey(HolidayTripBook,related_name = "payment_fail",on_delete = models.SET_NULL,null = True)
    payment_mode = models.CharField(max_length = 100,choices = (('khalti','Khalti'),('esewa','Esewa'),('cod','Cash On Ddelivery')))
    refrence_id = models.CharField(max_length = 4000)
    services_product = models.CharField(max_length = 100)
    server_response = models.CharField(max_length = 3000,null = True,blank = True)

class PaymentService(models.Model):
    order = models.ForeignKey(ServiceBook,related_name = "payment",on_delete = models.SET_NULL,null = True)
    ammount = models.FloatField()
    payment_mode = models.CharField(max_length = 100,choices = (('khalti','Khalti'),('esewa','Esewa'),('cod','Cash On Ddelivery')))
    refrence_id = models.CharField(max_length = 4000,unique = True)
    remarks = models.CharField(max_length = 3000,null = True,blank = True)
    status= models.CharField(max_length=255, choices=[
        ('paid','Paid'),
        ('unpaid','Paid'),
        ('half', 'Half Payment'),
        ('cod','Cash On Delivery'),
        ('refunded','Refunded'),
    ],)