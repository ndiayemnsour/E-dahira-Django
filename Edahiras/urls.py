import home
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.http import HttpResponse
from Edahiras import admin

# Vue basique pour la racine
def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil de E-dahira!")

urlpatterns = [
      path('', home),  # Cette ligne permet d'afficher la page d'accueil
      path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

