from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter() # Request & Response handle amader router
router.register('list', views.DoctorViewset) # router er antenna
router.register('specialization', views.SpecializationViewset) # router er antenna
router.register('available_time', views.AvailableTimeViewset) # router er antenna
router.register('designation', views.DesignationViewset) # router er antenna
router.register('reviews', views.ReviewViewset) # router er antenna

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]