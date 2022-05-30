from django.urls import path
from galleria import views

# app_name = 'galleria'

urlpatterns = [
    path('', views.galleries, name='gallery_list'),
    path('gallery', views.galleries, name='location'),
    path('search', views.search_gallery, name='search'),
    path('galleries/create', views.create_gallery, name='create'),
    path('galleries/<int:image_id>/update',
         views.update_gallery, name='update'),
    path('galleries/<int:image_id>/delete',
         views.delete_gallery, name='delete'),
]
