from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from base import views

router = routers.DefaultRouter()
router.register(r'animal-types', views.AnimalTypeViewSet)
router.register(r'breeds', views.BreedViewSet)
router.register(r'animals', views.AnimalViewSet)
router.register(r'weightings', views.WeightingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('base.urls')),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
