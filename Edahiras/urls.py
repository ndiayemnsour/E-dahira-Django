import home
from attr.filters import include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.http import HttpResponse
from rest_framework import routers

from Edahiras import admin
from Edahiras.views import MembresViewSet, DahirasViewSet, AudioViewSet, LocalitesViewSet, SectionsViewSet


# Vue basique pour la racine
def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil de E-dahira!")

router = routers.DefaultRouter()
router.register('Membres', MembresViewSet)
router.register('Dahiras', DahirasViewSet)
router.register('Audio', AudioViewSet)
router.register('Localites', LocalitesViewSet)
router.register('Sections', SectionsViewSet)

urlpatterns = [
      path('', home),  # Cette ligne permet d'afficher la page d'accueil
      path('admin/', admin.site.urls),
      path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

