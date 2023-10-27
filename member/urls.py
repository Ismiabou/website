from django.urls import path

from .views import user_register, user_login, user_logout, update_profile, account, user_delete

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('edit-profile', update_profile, name='edit-profile'),
    path('account', account, name='account'),
    path('delete', user_delete, name='delete'),
]