from django.urls import path, include
from . import views

urlpatterns= [
    path('index/',views.index, name='index'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
    path('campaign/',views.campaign, name='campaign'),
    path('about/',views.about,name='about'),
    path('donate/',views.donate,name='donate'),
    path('contact/',views.contact,name='contact'),

]

