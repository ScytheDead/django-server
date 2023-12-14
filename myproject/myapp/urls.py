from django.urls import path
from .views import user_list, edit_user, add_user, detail_user

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('users/add', add_user, name='add_user'),
    path('users/<int:id>', edit_user, name='edit_user'),
    path('users/detail/<int:id>', detail_user, name='detail_user'),
]