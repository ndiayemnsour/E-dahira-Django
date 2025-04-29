from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from rest_framework import routers
from django.contrib import admin

from Edahiras import views
from Edahiras.views import MembresViewSet, DahirasViewSet, AudioViewSet, LocalitesViewSet, SectionsViewSet

router = routers.DefaultRouter()
router.register(r'membres', MembresViewSet)
router.register(r'dahiras', DahirasViewSet)
router.register(r'audio', AudioViewSet)
router.register(r'localites', LocalitesViewSet)
router.register(r'sections', SectionsViewSet)
print(router.urls)

urlpatterns = [
      path('', lambda request: HttpResponse("Bienvenue sur la page d'accueil de E-dahira!")),  # Page d'accueil
      path('admin/', admin.site.urls),
      path('api/', include(router.urls)),
      path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

