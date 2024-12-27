from django.urls import path
from . import views

app_name = 'unis'

urlpatterns = [
    path('', views.unis_list, name='list'),
    path('<slug:slug>', views.uni_page, name='page'),
]
