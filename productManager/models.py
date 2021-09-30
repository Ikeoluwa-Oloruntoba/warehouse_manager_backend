from django.db import models
from django.utils.timezone import now

# Create your models here.


class PUser(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    email_verified_at = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "users"


class Product(models.Model):

    Product_id = models.AutoField(primary_key=True)
    added_by = models.ForeignKey(PUser, on_delete=models.CASCADE)
    qty_in_stock = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_image = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = "products"


class Location(models.Model):

    location_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='location', null=True, blank=True)
    locate = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.locate

    class Meta:
        db_table = "location"


class ProductMovements(models.Model):

    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='movelocation', null=True, blank=True)
    from_location = models.CharField(max_length=100, null=True, blank=True)
    to_location = models.CharField(max_length=100, null=True, blank=True)
    qty_to_be_moved = models.IntegerField(null=True, blank=True)

    status = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    class Meta:
        db_table = "product_movements"
