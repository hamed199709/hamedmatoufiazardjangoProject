from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Comment(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    comment = models.CharField(max_length=550)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.firstname)
        self.slug = slugify(self.lastname)
        super().save(*args,**kwargs)





