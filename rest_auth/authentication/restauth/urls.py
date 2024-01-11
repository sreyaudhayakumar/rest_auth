from django.urls import path, include
from .import views

urlpatterns = [
    path('restauth/', include('rest_framework.urls')),
    path('adduser', views.AddUser.as_view(), name='adduser'),
    path('login',views.auth_login.as_view(),name='login'),
]

