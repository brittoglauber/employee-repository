from django.urls import path
from . import views
 
urlpatterns = [
      path('', views.ApiOverview, name='home'),
      path('create/', views.add_employee, name='add-employee'),
      path('all/', views.view_employee, name='view_employee'),
      path('<int:pk>/', views.view_employee_byId, name='view_employee_byId'),
      path('update/<int:pk>/', views.update_employee, name='update-employee'),
      path('<int:pk>/delete/', views.delete_employee, name='delete-employee'),
]