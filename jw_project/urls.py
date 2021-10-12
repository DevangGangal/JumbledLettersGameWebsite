
from django.contrib import admin
from django.urls import path
from jwapp.views import home,check
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('check/',check,name="check")
]
