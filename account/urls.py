from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('<int:pk>/profile', views.profile, name='profile'),
    path('logout', views.logout_user, name='logout'),

]
