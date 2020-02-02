from django.db import models


class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'banks'


class Branch(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=100)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    class Meta:
        db_table = 'branches'
