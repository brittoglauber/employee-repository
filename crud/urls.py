
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('api.urls_employee')),
    path('query/', include('api.urls_query'))
]
