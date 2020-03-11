
from django.contrib import admin
from django.urls import path
import csvvv.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('csv/', csvvv.views.csvsql, name="csa")
]
