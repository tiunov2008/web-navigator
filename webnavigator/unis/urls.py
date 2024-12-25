from django.urls import path
from . import views


urlpatterns = [
    path('', views.unis_list, name='unis'),
    path('<slug:slug>', views.unis_page, name='page'),
]
