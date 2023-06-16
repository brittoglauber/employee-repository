from django.urls import path
from . import views
 
urlpatterns = [
      path('create/', views.add_query, name='add-query'),
      path('all/', views.view_query, name='view-query'),
      path('consult/', views.search_query_by_employee_name, name='query-by-employee')
]