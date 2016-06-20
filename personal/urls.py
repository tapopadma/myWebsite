from django.conf.urls import url, patterns
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^aboutme/', views.aboutme, name='aboutme'),
    url(r'^skills/', views.skills, name='skills'),
    url(r'^career/', views.career, name='career'),
    url(r'^achievements/', views.achievements, name='achievements'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^thanks/', views.thanks, name='thanks'),
    ]    