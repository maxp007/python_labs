
from django.db import models


class ComputerModel(models.Model):

    class Meta:
        db_table = 'my_app_computer'
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "'name':{}, 'description':{}".format(self.name, self.description)


class CustomerModel(models.Model):

    class Meta:
        db_table = 'my_app_customer'
    name = models.CharField(max_length=64, default='')
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    computers = models.ManyToManyField(ComputerModel, through='OrderModel')

    def __str__(self):
        return "'name':{}, 'email':{}, 'password':{}".format(self.name, self.email, self.password )


class OrderModel(models.Model):
    class Meta:
        db_table = 'my_app_order'
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    computer = models.ForeignKey(ComputerModel, on_delete=models.CASCADE)
    date_received  = models.DateTimeField()
    date_completed = models.DateTimeField()
