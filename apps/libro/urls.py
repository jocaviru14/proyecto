from django.urls import path, include
from rest_framework import routers
from apps.libro import views

router=routers.DefaultRouter()
router.register(r'libros',views.LibroViewSet)

urlpatterns = [
    path('', include(router.urls))
]