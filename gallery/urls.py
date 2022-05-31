from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('galleria.urls')),
    path('account/', include('account.urls'), name='account'),
    path('admin/', admin.site.urls),
]
