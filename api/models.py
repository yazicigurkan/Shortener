from django.db import models

# Create your models here.


class URL(models.Model):
    
    Origin_Url =models.TextField()
    Short_Path = models.TextField(default=None)
    Short_Url = models.TextField()
    visit_Count = models.IntegerField(default=0)

    