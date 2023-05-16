from django.urls import path

from .views import index, loggerDefault

urlpatterns = [
    path("", index, name="app_base_index"),
    path("logging/", loggerDefault, name="app_base_logging")
]
