
from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query/', include('api.urls_query')),
    path('employee/', include('api.urls_employee')),
    # path('employee', views.employees, name='list_of_employee'),
    # path('', views.registerEmployee, name='registerEmployee'),
]
