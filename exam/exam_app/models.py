from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name should be 2 characters!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name should be 2 characters!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm_password']:  # Fix the typo here
            errors['confirm_password'] = "Passwords should match"  # Fix the typo here
        return errors

    
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters!"
        return errors

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
class PieManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if not postData.get('name'):
            errors['name'] = 'name is required.'
        if not postData.get('filling'):
            errors['filling'] = 'filling is required.'
        if not postData.get('crust'):
            errors['crust'] = 'crust is required.'


        return errors

class Pie(models.Model):
    name = models.CharField(max_length=255)
    filling= models.CharField(max_length=100)
    crust =models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    my_user = models.ForeignKey(User, related_name='cook',on_delete=models.CASCADE)
    objects = PieManager()
    vote = models.ManyToManyField(User, related_name='voted_pies')
