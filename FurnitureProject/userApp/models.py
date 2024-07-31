from django.db import models

# Create your models here.
class CContactModel (models.Model):
    cname = models.CharField(max_length = 100)
    cmobile = models.CharField(max_length = 15)
    cemail = models.EmailField()
    ccity = models.CharField(max_length = 20)
    cmessage = models.TextField()