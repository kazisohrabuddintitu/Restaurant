from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

# Create a router for the ItemViewSet
router = DefaultRouter()
router.register(r'products', ItemViewSet)

# Define the URL patterns
urlpatterns = [
    # Include the product endpoints with the prefix <int:pk>/
    path('', include(router.urls)),
]
