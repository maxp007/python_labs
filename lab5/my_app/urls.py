from django.conf.urls import url, include
from django.contrib import admin
from my_app.views import function_view, testpage, ExampleClassBased,basepage, basextend, PageView, IncludePage


urlpatterns = [
    url(r'^basextend/', basextend, name='basextend'),
    url(r'^basepage/', basepage, name='basepage'),
    url(r'^testpage/', testpage, name='testpage'),
    url(r'^function_view/', function_view, name='function_view'),
    url(r'^class_based_view/', ExampleClassBased.as_view(), name='class_based_view'),
    url(r'^page/(?P<id>\d+)', PageView.as_view(), name='page'),
    url(r'^inclpage/', IncludePage.as_view(), name= "includepage"),
    url(r'^$', testpage, name='testpage')
]