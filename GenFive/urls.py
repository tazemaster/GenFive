from django.contrib import admin
from django.urls import path, include

from CharacterCreator import views
#from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'parties', views.PartiesViewSet)
router.register(r'characters', views.CharacterViewSet)
router.register(r'spells', views.SpellsViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('register', views.register),
    path('home', views.home, name='home'),
    path('creation', views.creation),
    path('battle', views.battle),
]

#urlpatterns += router.urls
