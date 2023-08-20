from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, verify_email, generate_password


app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify/<str:token>/', verify_email, name='verify'),
    path('profile/genpassword/', generate_password, name='generate_password'),
    
]