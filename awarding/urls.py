from django.urls import path,include
from rest_framework import routers
from . import views
from django.db import router
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('projects', views.PostViewSet)
router.register('userprofiles', views.ProfileViewSet)

urlpatterns = [
    path('',views.index, name='home'),
    path('project/<post>', views.project, name='project'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('profile/<username>/', views.profile, name='profile'),
    path('search/', views.search_project, name='search'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls), name='api'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)