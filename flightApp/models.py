from django.db import models

class Flight(models.Model) :
    flightNumber = models.CharField(max_length=25)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length = 20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

    def __str__(self) :
        return self.flightNumber + " " + self.operatingAirlines

class Passenger(models.Model) :
    firstName = models.CharField(max_length = 10)
    lastName = models.CharField(max_length = 10)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)

    def __str__(self) :
        return self.firstName + self.lastName


class Reservation(models.Model) :
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
