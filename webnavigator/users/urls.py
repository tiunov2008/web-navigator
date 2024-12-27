from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    #path('user-page/', views.user_page_view, name='user-page'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
