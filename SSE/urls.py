"""SSE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from about import views as about_views
from search import views as search_views
from django.views.generic import TemplateView
from about.views import ContactPage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^about/$', about_views.index , name='about'),
    url(r'^about/contact/$', ContactPage.as_view(),name='contact'),
    url(r'^$', TemplateView.as_view(template_name='index.html'),name='homepage'),
    url(r'^search/$', search_views.index),
    url(r'^getmsgs/$',search_views.msgsToJson),
    url(r'^todb/$',search_views.toDb)   
]