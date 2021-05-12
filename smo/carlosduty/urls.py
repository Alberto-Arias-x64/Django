from django.urls import path
from carlosduty import views

urlpatterns = [
    path('',views.home,name='Inicio'),
    path('store',views.store,name='Tienda'),
    path('videos',views.videos,name='Videos'),
    path('blog',views.blog,name='Blog'),
    path('contact',views.contact,name='Contacto'),
]