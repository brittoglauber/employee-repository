
from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('api.urls_employee')),
    path('query/', include('api.urls_query')),
    path('', views.home, name='home'),
    path('employee', views.employees, name='list_of_employee')
]
