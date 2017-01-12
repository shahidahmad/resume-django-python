from __future__ import unicode_literals


#Import models module from the django.db library
from django.db import models

#A class that creates contactme table in the database
class ContactMe(models.Model):
    #the following variables represents column name of the contact me table, and the values assigned to them represent their datatype.
    name = models.TextField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email_add  = models.EmailField(max_length=80)
    message = models.TextField(max_length=500)


