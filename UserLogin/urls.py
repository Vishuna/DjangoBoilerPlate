from django.urls import path, include
from . import views
from UserLogin.views import userLogin
 

urlpatterns=[ 
path('login/', views.userLogin, name='login'),
path('dashboard/', views.dashboard, name='dashboard'),
path('user_registration',views.userRegistration, name="user_registration")

]