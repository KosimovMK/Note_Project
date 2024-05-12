from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('create/', views.create_note, name='create_note'),
    path('<uuid:note_id>/edit/', views.edit_note, name='edit_note'),
    path('<uuid:note_id>/delete/', views.delete_note, name='delete_note'),
]
