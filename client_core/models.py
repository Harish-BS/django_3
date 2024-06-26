from django.db import models

class role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class dept(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class user(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

