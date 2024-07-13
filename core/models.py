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

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.client_name
    
from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=255)
    client_id = models.ForeignKey('core.Client',on_delete=models.CASCADE)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100,null=True,blank=True,default='No Update Yet')
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.department_name

class Designation(models.Model):
    designation_name = models.CharField(max_length=255)
    client_id = models.ForeignKey('core.Client',on_delete=models.CASCADE,default='No ID')
    #client_id =  models.ForeignKey(User,null = True,on_delete= models.SET_NULL,blank=True)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.designation_name

class User(models.Model):
    user_name = models.CharField(max_length=255)
    created_by = models.CharField(max_length=100)
    client_id =  models.ForeignKey('core.Client',on_delete=models.CASCADE,default='No ID')
    #department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    #designation_id = models.ForeignKey(Designation,on_delete=models.CASCADE)
    department_id = models.ForeignKey('core.Department', on_delete=models.CASCADE,default='No ID')
    designation_id = models.ForeignKey('core.Designation', on_delete=models.CASCADE,default='No ID')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    #is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.user_name