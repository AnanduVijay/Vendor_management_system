from django.urls import path
from rest_framework.routers import DefaultRouter
from vendor.api.views.views import (
    VendorViewSet,
    PurchaseOrderViewSet,
    PerformanceViewSet,
    AknowledgmentOrderViewSet,
)
from vendor.views import login


router = DefaultRouter()
router.register(r"vendors", VendorViewSet, basename="vendors") 
router.register(r"purchase_orders", PurchaseOrderViewSet, basename="purchase_orders")
router.register(
    r"purchase_orders/(?P<pk_id>\w+)/acknowledge",
    AknowledgmentOrderViewSet,
    basename="acknowledge",
)
router.register(
    r"vendors/(?P<vendor_id>\d+)/performance",
    PerformanceViewSet,
    basename="performance",
)

urlpatterns = [
    path("login", login, name="login"),
]

urlpatterns += router.urls
