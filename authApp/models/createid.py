from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class createid(AbstractBaseUser):

    id = models.AutoField(primary_key=True)
    namepc =  models.CharField(max_length=100)
    ubicationpc =  models.CharField(max_length=100)
    objects = models.Manager()


    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []
    def __str__(self):  
        return self.name

        