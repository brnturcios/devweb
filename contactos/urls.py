from rest_framework import routers
from .api import ContactoViewSet

router = routers.DefaultRouter()

router.register('api/contactos', ContactoViewSet, 'contactos')

urlpatterns = router.urls

