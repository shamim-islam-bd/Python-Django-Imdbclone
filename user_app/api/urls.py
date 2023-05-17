from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registration_View, Logout_view

urlpatterns = [
  path('login/', obtain_auth_token, name='login'),
  path('logout/', Logout_view, name='logout'),
  path('register/', registration_View, name='register'),
]