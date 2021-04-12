from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('join/', views.join),
    path('portal/', views.webportal),
    path('members/', views.members)
]
