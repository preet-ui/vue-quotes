from django.db import models
from datetime import date
# Create your models here.
class Hotel(models.Model):
    hotel_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    rooms = models.IntegerField()
    city = models.CharField(max_length=100)
    def __str__(self):
          return self.name

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    age = models.IntegerField()
    def __str__(self):
          return 'User ID:' + self.user_id + 'Name:' + self.name

class Room(models.Model):
    Room_no = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=50)
    cost = models.FloatField()
    hotel_id = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    arr_date = models.DateField(("Date"), default=date.today)
    dep_date = models.DateField(("Date"), default=date.today)

class Booking(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    room_no = models.ForeignKey(Room,on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    book_date = models.DateField(("Date"), default=date.today)