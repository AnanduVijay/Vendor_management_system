from rest_framework import viewsets, permissions
from vendor.api.serializers.vendor import VendorSerializer
from vendor.api.serializers.purchase_order import (
    PurchaceOrderSerializer,
    AcknowledgeSerializer,
)
from vendor.api.serializers.performance import PerformanceSerializer
from vendor.models import Vendor, PurchaseOrder, Performance
from rest_framework.response import Response
from rest_framework import status


class VendorViewSet(viewsets.ModelViewSet):
    """
    Vendor name listView and updating ViewSet
    """

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        print("are you sure you want to delete")
        return super().destroy(request, *args, **kwargs)


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    """
    Purchase order ListView and updating ViewSet
    """

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaceOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return the listed purchase order listt by filtering against
        'vendor' query parameters in the URL.
        """

        vendor_id = self.request.query_params.get("vendor", None)

        if vendor_id:
            return PurchaseOrder.objects.filter(vendor__id=vendor_id)
        else:
            return PurchaseOrder.objects.all()


class AknowledgmentOrderViewSet(viewsets.ModelViewSet):
    """
    Update Acknowledgment Endpoint.
    """

    queryset = PurchaseOrder.objects.all()
    serializer_class = AcknowledgeSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["post"]

    def create(self, request, pk_id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=pk_id)
            serializer = AcknowledgeSerializer(data=request.data)
        except PurchaseOrder.DoesNotExist:
            return Response(
                {"error": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if serializer.is_valid():
            acknowledgment_date = serializer.validated_data["acknowledgment_date"]
            purchase_order.acknowledgment_date = acknowledgment_date
            purchase_order.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerformanceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for performance of all vendors
    """

    serializer_class = PerformanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        vendor_id = self.kwargs["vendor_id"]
        return Performance.objects.filter(vendor_id=vendor_id)
