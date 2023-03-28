from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    gen = models.TextField(default='')
    fam = models.TextField(default='')
    phy = models.TextField(default='')
    bmi = models.IntegerField(default=0)
    smoking = models.TextField(default='')
    alc = models.TextField(default='')
    sleep = models.IntegerField(default=0)
    med = models.TextField(default='')
    junk = models.TextField(default='')
    stress = models.TextField(default='')
    bpl = models.TextField(default='')
    preg = models.IntegerField(default=0)
    uri = models.TextField(default='')

    pred_result = models.TextField(default='')

    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    activity = models.TextField(default="")
    cal_req = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile:'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

