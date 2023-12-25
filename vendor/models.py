from django.db import models
import uuid


class Vendor(models.Model):
    """
    Vendor model class.
    """
    name = models.CharField(max_length=130)
    contact_details = models.TextField(max_length=200)
    adress = models.CharField(max_length=200)
    vendor_code = models.CharField(
        max_length=4, default=uuid.uuid4, unique=True, editable=False
    )
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    """
    Purchase order model class.
    """
    class Status(models.TextChoices):
        PENDING = ("pending", "Pending")
        COMPLETED = ("completed", "Completed")
        CANCELLED = ("cancelled", "Cancelled")

    po_number = models.CharField(
        max_length=4, default=uuid.uuid4, unique=True, editable=False
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=True)  # Date when the order was placed.
    delivery_date = models.DateTimeField(
        null=True
    )  # Expected or actual delivery date of the order.
    items = models.JSONField()
    quantity = models.IntegerField(null=False)
    status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.PENDING
    )
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(null=True)
    acknowledgment_date = models.DateTimeField(null=True)

    def __int__(self):
        return self.po_number


class Performance(models.Model):
    """
    Performance model class
    """
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.vendor.name
