from rest_framework import serializers

from vendor.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    """
    Vendor serializer
    """
    class Meta:
        model = Vendor
        fields = [
            "id",
            "name",
            "contact_details",
            "adress",
            "vendor_code",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
