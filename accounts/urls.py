from django.urls import path
from . import views as v

urlpatterns = [
    path('register/',v.register_view, name='register'),
    path('home/',v.home_view, name='home'),
    path('login/',v.login_view, name='login'),
    path('logout/',v.logout_view, name='logout')
]