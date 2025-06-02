from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from rest_framework import routers
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Edahiras.views import MembresViewSet, DahirasViewSet, AudioViewSet, LocalitesViewSet, SectionsViewSet, \
      serve_audio_file, ChapitreViewSet, ThemeViewSet, SequenceViewSet
from .views import ChapitresByThemeAPIView
from .views import AudioListView

router = routers.DefaultRouter()
router.register(r'membres', MembresViewSet)
router.register(r'dahiras', DahirasViewSet)
router.register(r'audios', AudioViewSet)
router.register(r'localites', LocalitesViewSet)
router.register(r'sections', SectionsViewSet)
router.register(r'chapitres', ChapitreViewSet)
router.register(r'themes', ThemeViewSet)
router.register(r'sequences', SequenceViewSet)
print(router.urls)

urlpatterns = [
                  path('audios/', AudioListView.as_view(), name='audio-list'),

                  path('', lambda request: HttpResponse("Bienvenue sur la page d'accueil de E-dahira!")),  # Page d'accueil
      path('admin/', admin.site.urls),
      path('api/', include(router.urls)),
      path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
      path('media/audio/<str:filename>', serve_audio_file), # nouvelle route audio directe
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                    path('api/themes/<int:theme_id>/chapitres/', ChapitresByThemeAPIView.as_view(),
                         name='chapitres-by-theme'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)