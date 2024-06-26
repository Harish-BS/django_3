from django.db import models
from foundation.models import statuss
from foundation.models import stage
from client_core.models import role
from client_core.models import dept
from client_core.models import user

class project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class solution(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(project,null = True,on_delete= models.SET_NULL,blank=True)

    def __str__(self):
        return self.name
    
class feature(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(project,null = True,on_delete= models.SET_NULL,blank=True)
    solution = models.ForeignKey(solution,null = True,on_delete= models.SET_NULL,blank=True)

    def __str__(self):
        return self.name

class task(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(project,null = True,on_delete= models.SET_NULL,blank=True)
    solution = models.ForeignKey(solution,null = True,on_delete= models.SET_NULL,blank=True)
    feature = models.ForeignKey(feature,null=True,on_delete=models.SET_NULL,blank=True)
    statuss = models.ForeignKey(statuss,null=True,on_delete=models.CASCADE,blank=True)
    stage = models.ForeignKey(stage,null=True,on_delete=models.CASCADE,blank=True)
    role = models.ForeignKey(role,null=True,on_delete=models.CASCADE,blank=True)
    dept = models.ForeignKey(dept,null=True,on_delete=models.CASCADE,blank=True)
    user = models.ForeignKey(user,null=True,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.name
