from rest_framework import routers
from .views import *
router = routers.SimpleRouter()
router.register(r'address', AddressViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'product', ProductViewSet)
router.register(r'vendor', VendorViewSet)
urlpatterns = router.urls