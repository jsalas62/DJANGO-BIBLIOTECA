from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrestamoViewSet, LibroViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'prestamos', PrestamoViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
