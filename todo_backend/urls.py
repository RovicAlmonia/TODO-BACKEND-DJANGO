from django.contrib import admin
from django.urls import path, include  # Make sure to include 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),  # Make sure this line is included
]
