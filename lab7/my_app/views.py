from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
from django.views import View
from my_app.models import ComputerModel, CustomerModel, OrderModel
from django.db.models import Count

def basepage(request):
    return render(request, "my_app/base.html")


def basextend(request):
    colors = {'colors': {"black": "#000000", "white": "#FFFFFF", "red1": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}}
    return render(request, "my_app/basextend.html", colors)


def testpage(request):
    pages = [
             {'title': "Первая страница", "id": 1},
             {'title': "Вторая страница", "id": 2},
             {'title': "Третья страница", "id": 3}
        ]
    server_times = {'date': datetime.datetime.now()}
    dicts = {"pages": pages, "server_times": server_times}
    return render(request, "my_app/index.html", dicts)


def function_view(request):
    return HttpResponse("Response from fucntion view")


class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse("response from class based view")


class PageView(View):
    def get(self, request, id):
        computer = ComputerModel.objects.get(id=int(id))
        data = {
            'pc': {
                'id': computer.id,
                'name': computer.name,
                'description': computer.description
            }
        }
        return render(request, 'my_app/page.html', {'computer': computer})


class IncludePage(View):
    def get(self, request):
        return render(request, 'my_app/inclpage.html')


class ComputersClass(View):

    def get(self, request):
        computers = ComputerModel.objects.all()
        return render(request, 'my_app/computers.html', {'computers': computers})
