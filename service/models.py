from django.db import models

# Service categories
class ServiceCategory(models.Model):
    ar_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.ar_name

# Vehicles
class Vehicle(models.Model):
    ar_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.ar_name

# Customers
class Customer(models.Model):
    ar_name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.IntegerField(unique=True, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, related_name='customer_vehicle', on_delete=models.CASCADE, null=True, blank=True)
    vin = models.CharField(max_length=255, null=True, blank=True)
    engine = models.CharField(max_length=255, null=True, blank=True)
    license_plate = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.ar_name

# Orders 
class Order(models.Model):
    enter_date = models.DateField(null=True)
    exit_date = models.DateField(null=True)
    enter_time = models.TimeField(null=True)
    exit_time = models.TimeField(null=True)
    customer_call = models.NullBooleanField(default=False)
    vehicle_counter = models.IntegerField(blank=True, null=True)
    customer = models.ForeignKey(Customer, related_name='order_customer', on_delete=models.CASCADE)
    complaint = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=30) 
    notes = models.TextField(blank=True)
    bill_no = models.IntegerField(null=True)
    order_no = models.IntegerField(null=True)


# Bills
class Bill(models.Model):
    date = models.DateField()
    qty = models.FloatField(null=True)
    price = models.FloatField()
    discount = models.FloatField(null=True)
    tax = models.NullBooleanField(default=False)
    order = models.ForeignKey(Order, related_name='bill_order', on_delete=models.CASCADE)
    item_code = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=30) 

    unique_together = ("order", "description")

# Parts
class Stock(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
