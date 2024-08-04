from django.db import models

# Create your models here.

class EmailSetup(models.Model):
    smtp_server_address = models.CharField()  #EMAIL_HOST
    email_address = models.EmailField()
    password = models.CharField() #app password
    port = models.PositiveIntegerField()
    required_authentication = models.BooleanField(default = True)
    security = models.CharField(max_length = 200,choices = (('None','None'),('SSL','SSL'),('TSL','TSL')),default = 'None')
    smtp_username = models.CharField(max_length = 100,null = True,blank = True)
    verify_smtp_certificate = models.BooleanField(default = False)
