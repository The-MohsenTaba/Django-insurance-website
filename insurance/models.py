from django.db import models
from datetime import date, timedelta
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class UserInfo(models.Model):
    class SEX(models.TextChoices):
        Male = 'مذکر'
        Female = 'مونث'
    class Marriage(models.TextChoices):
        Married="متاهل"
        Single = "مجرد"
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    national_id = models.IntegerField()
    birth_date = models.DateField()
    job_title = models.CharField(max_length=100)
    sex = models.CharField(max_length=50 ,choices=SEX,null=False)
    marriage = models.CharField(max_length=100,null=False,choices=Marriage)
    job_address = models.CharField(max_length=100)
    home_address = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    phone_number = models.IntegerField()
    def __str__(self):
        return f"{self.username} informations"

class Insurance(models.Model):
    class PaymentMethods(models.TextChoices):
        complete='complete'
        yearly='yearly'
        monthly='monthly'
    class InsurancePlan(models.TextChoices):
        one='one year'
        four='four years'
        eight='eight years'
    class Status(models.TextChoices):
        checking='checking'
        accepted='accepted'
        rejected='rejected'
    payment_method = models.CharField(max_length=100,choices=PaymentMethods,default=PaymentMethods.yearly)
    plan =models.CharField(max_length=100,choices=InsurancePlan,default=InsurancePlan.one)
    status = models.CharField(max_length=100,choices=Status,null=False,default=Status.checking)
    request_date = models.DateField(default=date.today)
    accepted_date = models.DateField(null=True,blank=True)
    expired_date = models.DateField(default=date.today)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def save(self, *args, **kwargs):
        if self.accepted_date:
            if self.plan==Insurance.InsurancePlan.one:
                self.expired_date = self.accepted_date+timedelta(days=365)
            elif self.plan==Insurance.InsurancePlan.four:
                self.expired_date = self.accepted_date+timedelta(days=365*4)
            elif self.plan==Insurance.InsurancePlan.eight:
                self.expired_date = self.accepted_date+timedelta(days=365*8)
        super(Insurance,self).save(*args, **kwargs)
    @property
    def time_left(self):
        if self.expired_date:
            delta = self.expired_date - date.today()
            return delta.days if delta.days > 0 else 0
        return None