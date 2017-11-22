from django.conf.urls import url, include
from django.contrib import admin
from my_app.views import testpage, \
    basepage, basextend, PageView, IncludePage, \
    ComputersClass, RegisterClass, authorization, RegisterDjango, AuthorizeDjango, LogoutClass

urlpatterns = [
    url(r'^basextend/', basextend, name='basextend'),
    url(r'^basepage/', basepage, name='basepage'),
    url(r'^testpage/', testpage, name='testpagebase'),
    url(r'^computers/page/(?P<id>\d+)', PageView.as_view(), name='page'),
    url(r'^inclpage/', IncludePage.as_view(), name="includepage"),
    url(r'^$', authorization, name='testpage'),
    url(r'computers/', ComputersClass.as_view(), name="computers"),
    url(r'registration/', RegisterClass, name="registration"),
    url(r'authorization/', authorization, name="authorization"),
    url(r'register/', RegisterDjango, name="RegisterDjango"),
    url(r'authorize/', AuthorizeDjango, name= "AuthorizeDjango"),
    url(r'logout/', LogoutClass.as_view(), name= "LogoutClass"),
]
