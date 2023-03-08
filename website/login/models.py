from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    movie_title = models.CharField(max_length=255)
    movie_duration = models.PositiveIntegerField()
    movie_age_rating = models.PositiveIntegerField()
    movie_description = models.TextField()
    
    
class MovieShowings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_date = models.DateField()
    movie_time = models.TimeField()
    movie_screen = models.PositiveIntegerField() 
    movie_seats = models.PositiveIntegerField() 

class Ticket(models.Model):
    ticket_name = models.CharField(max_length=100)
    ticket_price = models.DecimalField(max_digits=6)

class NoOfTickets(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class MovieBooking(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField() 
    showing = models.ForeignKey(MovieShowings, on_delete=models.CASCADE)
    no_of_tickets = models.ManyToManyField(NoOfTickets) 
    



