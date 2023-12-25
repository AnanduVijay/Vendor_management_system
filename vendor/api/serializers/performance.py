from rest_framework import serializers
from vendor.models import Performance


class PerformanceSerializer(serializers.ModelSerializer):
    """
    Performance serializer
    """
    class Meta:
        model = Performance
        fields = [
            "vendor",
            "date",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
