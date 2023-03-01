import datetime
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
 
    
class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class ClientProductData(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    monthly = models.IntegerField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.product


class ProductData(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    productid = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    unit_price = models.IntegerField()

    def __str__(self):
        return self.productid


class StoreData(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    storeid = models.CharField(max_length=200)
    store_name = models.CharField(max_length=200)
    store_location = models.CharField(max_length=200)

    def __str__(self):
        return self.storeid


class StoreSales(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    prodid = models.CharField(max_length=200)
    storeid = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    units_sold = models.IntegerField()

    def __str__(self):
        return (str(self.user))

# poudct
# name-price/unit/releasedate/prod-id

# store
# storename/country/store-id/

# store-sales
# prod-id/100/date/store-id

