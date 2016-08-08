"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from restaurants.views import menu, meta, welcome, list_restaurants, comment


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^menu/$', menu),
    url(r'^menu/meta/$', meta),
    url(r'^menu/welcome/$', welcome),
    url(r'^restaurants_list/$', list_restaurants),
    url(r'^comment/(\d{1,2})/$', comment),


#     #app
#     # url(r'^app/', include('app.urls')),
#     #menu
#     # url(r'^menu/', include('menu.urls')),

]
