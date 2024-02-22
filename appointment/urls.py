from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter() # Wifi router toiri korlam
router.register('', views.AppointmentViewset) # router er antenna (GET, POST, UPDATE, DELETE request handle kore)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]