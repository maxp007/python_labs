from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
from django.views import View

def basepage(request):
    return render(request, "my_app/base.html", locals())

def basextend(request):
    colors = {"black": "#000000", "white": "#FFFFFF", "red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
    return render(request, "my_app/basextend.html", locals())

def testpage(request):
    pages = [
             {'title': "Первая страница", "id": 1},
             {'title': "Вторая страница", "id": 2},
             {'title': "Третья страница", "id": 3}
        ]
    server_time = datetime.datetime.now()

    return render(request, "my_app/index.html", locals())

def function_view(request):
    return HttpResponse("Response from fucntion view")

class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse("response from class based view")

class PageView(View):
    def get(self, request, id):
        data = {'page': {'id': id}}
        return render(request, 'my_app/page.html', data)

class IncludePage(View):
    def get(self, request):

        return render(request, 'my_app/inclpage.html', locals())