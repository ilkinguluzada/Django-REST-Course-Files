from django.db import models

# Create your models here.
class Item(models.Model):
    ItemID = models.AutoField(primary_key=True,default=1)
    ItemName = models.CharField(max_length=200)
    Quantity = models.IntegerField()
    Category = models.CharField(max_length=200)
    Charity = models.CharField(max_length=200,default="None")

    def __str__(self):
        return str(self.ItemID)


class CharityRegistration(models.Model):
    Email = models.EmailField()
    CharityName = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    City = models.CharField(max_length=200)


    def __str__(self):
        return self.CharityName



class UserRegistration(models.Model):
    Email = models.EmailField()
    UserName = models.CharField(max_length=200)
    CharityName = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    City = models.CharField(max_length=200)

    def __str__(self):
        return self.UserName




class OrderedItem(models.Model):
    ItemID = models.ForeignKey('Item',on_delete=models.CASCADE)
    OrderDate = models.DateTimeField(auto_now_add=True)
    ItemName = models.CharField(max_length=200)
    Quantity = models.IntegerField()
    UserName = models.EmailField()

    def __str__(self):
        return self.ItemName

