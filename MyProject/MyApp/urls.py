from django.urls import path
from MyApp import views

# Template Tagging
app_name = 'MyApp'


urlpatterns = [
    path('help',views.help,name='help'),
    path('register',views.register, name='register'),
    path('login',views.user_login,name='user_login')
    # path('users',views.sign_up,name='users'),
    # path('relative',views.relative,name='relative'),
]