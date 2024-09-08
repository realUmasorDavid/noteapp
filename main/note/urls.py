from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns =   [
    path('', views.note_list, name='note_list'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('update/<int:pk>/', views.update_note, name='update_note'),
    path('new', views.new_note, name='new_note'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='register'),
    path('logout', views.logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)