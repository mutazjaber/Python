from django.db import models
from datetime import datetime, date
class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2 :
            errors["title"] = "show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "show network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "show description should be at least 10 characters"
        if datetime.strptime(postData['release_date'],"%Y-%m-%d") > datetime.today():
            errors["release_date"]= "this date is in the future!! are you idiot!"
        return errors
class Shows(models.Model):
    title = models.CharField(max_length=45)
    Network = models.CharField(max_length=45)
    Release_Date = models.CharField(max_length=45)
    description = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()#connect the two classes
