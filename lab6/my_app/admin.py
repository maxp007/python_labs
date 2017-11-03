from django.contrib import admin
from my_app.models import OrderModel, ComputerModel, CustomerModel

admin.site.register(CustomerModel)
admin.site.register(OrderModel)
admin.site.register(ComputerModel)
