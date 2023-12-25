from rest_framework import serializers
from vendor.models import PurchaseOrder
from vendor.api.serializers.vendor import VendorSerializer


class PurchaceOrderSerializer(serializers.ModelSerializer):
    """
    Purchase order serializer
    """
    vendor = VendorSerializer()

    class Meta:
        model = PurchaseOrder
        fields = [
            "id",
            "po_number",
            "vendor",
            "order_date",
            "items",
            "quantity",
            "status",
            "quality_rating",
            "acknowledgment_date",
        ]


class AcknowledgeSerializer(serializers.ModelSerializer):
    """
    Acknowledge serializer
    """
    class Meta:
        model = PurchaseOrder
        fields = ["id", "acknowledgment_date"]
