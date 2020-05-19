from rest_framework import routers
from .viewsets import RegionViewSet

router = routers.SimpleRouter()
router.register('Region', RegionViewSet)
urlpatterns = router.urls  