from django.contrib.auth import authenticate
from django.shortcuts import render
import os
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
import datetime
from django.views import View
from my_app.models import ComputerModel, CustomerModel, OrderModel
from django.db.models import Count
from lab5.settings import BASE_DIR, MIDDLEWARE
from .forms import RegisterForm, AuthorizeForm
from hashlib import md5



def basepage(request):
    return render(request, "my_app/base.html")


def basextend(request):
    colors = {
        'colors': {"black": "#000000", "white": "#FFFFFF", "red1": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}}
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


class PageView(View):
    def get(self, request, id):
        # TODO Получать запросами пикчи из базы даннных ,
        #  заполнять базу при старте всего и по мере загрузки новых пикч,
        # приведение в нужному формату происходит при загрузке каджой отдельной пикчи
        # id->pc.id,pc.name->name.lower->pic = db.get(name.lower)
        plist = os.listdir(os.path.join(BASE_DIR, "static"))
        pics = {el.rsplit('.', 1)[0]: el for el in plist}
        computer = ComputerModel.objects.get(id=int(id))
        return render(request, 'my_app/page.html', {'computer': computer, 'pics': pics})


class IncludePage(View):
    def get(self, request):
        return render(request, 'my_app/inclpage.html')


def authorization(request):
    names_dict = {}
    errors = []

    if request.method == "POST":
        names_list = ["username", "password"]
        names_dict = {x: request.POST.get(x, "") for x in names_list}
        username = request.POST.get("username")
        if not username:
            errors.append('Введите логин')
        password = request.POST.get('password')
        if not password:
            errors.append("Введите пароль")
        if not errors:
            return HttpResponseRedirect("/computers/")
    print(list(errors))
    return render(request, 'my_app/authorization.html', {"errors": errors, 'names_dict': names_dict})


# Форма средствами DJango
def RegisterDjango(request):
    names_dict = {}
    errors = []

    form = RegisterForm(request.POST or None)

    # TODO заменить на методы класса
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        names_list = ["firstname", "password", "email", "secondname", "login", "password2"]
        names_dict = {x: request.POST.get(x, "") for x in names_list}

        login = data["login"]

        if not login:
            errors.append('Введите логин')
        elif len(login) < 5:
            errors.append("Логин должен содержать не менее 5 симоволов")

        password = data['password']
        if not password:
            errors.append("Введите пароль")
        elif len(password) < 8:
            errors.append("Длина пароля должна быть не менее 8 символов")
        elif password != data["password2"]:
            errors.append("Пароли не совпадают")

        email = data['email']
        if not email:
            errors.append("Введите e-mail")

        firstname = data['firstname']
        if not firstname:
            errors.append("Введите Имя")

        secondname = data['secondname']
        if not secondname:
            errors.append("Введите Фамилию")

        if not errors:
            # updating data for registration
            new_form = form.save(commit=False)

            new_form.login = data.get('login')
            new_form.firstname = data.get('firstname')
            new_form.secondname = data.get('secondname')
            new_form.password = data.get('password')
            new_form.email = data.get('email')
            new_form.password = md5(new_form.password.encode('utf-8')).hexdigest()

            new_form.save()
            form.save_m2m()

            return HttpResponseRedirect("/computers/")
    return render(request, 'my_app/register.html', {"errors": errors, 'names_dict': names_dict, "form": form})


def AuthorizeDjango(request):
    names_dict = {}
    errors = []
    form = AuthorizeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        names_list = ["login", "password"]
        names_dict = {x: request.POST.get(x, "") for x in names_list}

        login = data["login"]
        if not login:
            errors.append('Введите логин')
        password = data['password']

        if not password:
            errors.append("Введите пароль")

        if not errors:
            try:
                userdata = CustomerModel.objects.get(login=data["login"])
                if userdata.password != md5(password.encode('utf-8')).hexdigest():
                    errors.append("Неправильное имя пользователя или пароль")

            except CustomerModel.DoesNotExist:
                errors.append("Неправильное имя пользователя или пароль")

            if not errors:
                # user = authenticate(username=login, password=password)
                # if user:
                # login(request, user)

                return HttpResponseRedirect("/computers/")
    print(list(errors))
    return render(request, 'my_app/authorize.html', {"errors": errors, 'names_dict': names_dict, "form": form})


class ComputersClass(View):
    def get(self, request):
        plist = os.listdir(os.path.join(BASE_DIR, "static"))
        computers = ComputerModel.objects.all()
        pics = {el.rsplit('.', 1)[0]: el for el in plist}
        return render(request, 'my_app/computers.html', {'computers': computers, "pics": pics})


class LogoutClass(View):
    def get(self, request):
        var = request.user.is_authenticated()
        return render(request, 'my_app/authorize.html')


# Форма в HTML шаблоне
def RegisterClass(request):
    names_dict = {}
    errors = []

    if request.method == "POST":
        names_list = ["username", "password", "password2", "email", "firstname", "secondname"]
        names_dict = {x: request.POST.get(x, "") for x in names_list}
        for k, v in names_dict.items():
            print("{}:{}".format(k, v))
        username = request.POST.get("username")
        if not username:
            errors.append('Введите логин')
        elif len(username) < 5:
            errors.append("Логин должен содержать не менее 5 симоволов")
        password = request.POST.get('password')
        if not password:
            errors.append("Введите пароль")
        elif len(password) < 8:
            errors.append("Длина пароля должна быть не менее 8 символов")
        password_repeat = request.POST.get("password2")
        if password != password_repeat:
            errors.append("Пароли должны совпадать")
        if not errors:
            return HttpResponseRedirect("/computers/")
    return render(request, 'my_app/registration.html', {"errors": errors, 'names_dict': names_dict})
