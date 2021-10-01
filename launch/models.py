from django.db import models

# Create your models here.
from django.db.models import ForeignKey
from django.contrib.auth.models import User
from django.views import generic
# class for creating table according to customer
class Customer(models.Model):
    #user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=190, null=True)
    name = models.CharField(max_length=190, null=True)
    email = models.CharField(max_length=190, null=True)
    phone = models.CharField(max_length=190, null=True)
    age = models.CharField(max_length=190, null=True)
    country = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True, max_length=190, null=True)

    # function to return customer name
    def __str__(self):
        return self.name


# class for creating table according to tags
class Tag(models.Model):
    TAG = (
        ('php', 'php'),
        ('python', 'python'),
    )

    name = models.CharField(max_length=190, null=True)

    # function to return customer name for tags
    def __str__(self):
        return self.name


# class for creating table according to announcements
class Announcement(models.Model):
    CATOGERY = (

        ('Find Job', 'Find Job'),
        ('Parties', 'Parties'),
        ('Computer', 'Computer'),
        ('Community', 'Community'),
        ('Birds and Animals', 'Birds and Animals'),
        ('Cars', 'Cars'),
        ('Services ', 'Services '),
        ('Meetings and Show','Meetings and Show'),
        ('Education', 'Education'),
        ('Companies Guide', 'Companies Guide')
    )

    category = models.CharField(max_length=190, null=True, choices=CATOGERY)
    price = models.FloatField(null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag)
    date_publish = models.DateTimeField(auto_now_add=True, max_length=190, null=True)
    address = models.CharField(max_length=190, null=True)
    content = models.TextField(max_length=300, null=True)

    # function to return customer name who publish his announcement

    def __str__(self):
        return self.category


class Order(models.Model):
    STATUS = (
        ('success', 'success'),
        ('pending', 'pending'),
        ('failed', 'failed')
    )

    PAY = (
        ('free', 'free'),
        ('visa card', 'visa card'),
        ('master card', 'master card')
    )
    price = models.FloatField(null=True)
    pay = models.CharField(max_length=190, null=True, choices=PAY)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    announcement = models.ForeignKey(Announcement, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag)
    number = models.CharField(max_length=190, null=True)
    status = models.CharField(max_length=190, null=True, choices=STATUS)

    def __str__(self):
        return self.number


