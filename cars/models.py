from django.db import models
from django.utils.text import slugify

class Brand(models.Model):
    name=models.CharField(max_length=50)
    slug=models.CharField(max_length=50,null=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Representation(models.Model):
    name=models.CharField(max_length=30)
    slug = models.CharField(max_length=30, null=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name=models.CharField(max_length=30)
    slug = models.CharField(max_length=30, null=True)


    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
class Car(models.Model):
    name=models.CharField(max_length=30)
    driver=models.ManyToManyField(Driver)
    representation=models.ForeignKey(Representation, on_delete=models.CASCADE, null=True)
    brand=models.OneToOneField(Brand, on_delete=models.CASCADE, null=True)
    color=models.CharField(max_length=20)
    speed=models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    zero_to_hundred = models.CharField(max_length=50)
    combined_fuel_consumption = models.CharField(max_length=50)
    body_class = models.CharField(max_length=50)
    engine_volume = models.CharField(max_length=50)
    engine_power = models.CharField(max_length=50)
    number_of_cylinders = models.PositiveIntegerField()
    photo=models.ImageField(upload_to='images/cars')
    price=models.DecimalField(max_digits=11,decimal_places=2)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name+'-'+self.color)
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.name}---{self.color}---{self.price}'
