from django.db import models
from django.conf import settings


class Campaign(models.Model):
    CampaignName = models.CharField(max_length=20)
    Date= models.CharField(max_length=20)
    Description = models.CharField(max_length=1000)
    Num_volunteers = models.IntegerField(default=0)
    # cover = models.ImageField(upload_to='webapp/',blank="True")

class Volunteer(models.Model):
    c_id = models.ForeignKey(Campaign,verbose_name='ID',on_delete=models.PROTECT)
    u_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)

class Donate(models.Model):
    AccountNumber = models.IntegerField()
    Amount= models.IntegerField()

class contact(models.Model):
    Email= models.EmailField(max_length=20)
    Description= models.CharField(max_length=500)


