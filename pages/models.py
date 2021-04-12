from django.db import models

from django.db.models import Model 

# team model.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

# to avoid having djangoadmin showing "team object 1" instad of names of team . we must make sure function refers to its self.
def __unicode__(self):    
    return self.first_name

