from django.db.models.signals import post_save, pre_save
from django.db.models import F
from django.db.models import Avg
from django.db import models
from django.dispatch import receiver
from .models import PurchaseOrder


@receiver(pre_save, sender=PurchaseOrder)
def get_pre_save_po_state(sender, instance, **kwargs):
    """
    Functions to get the state of a purchase order
    """
    instance._pre_save_status = instance.status


@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, **kwargs):
    """
    Function to update the performance metrics of vendor while 
    updating on-time delivery rate, on-time acknowledgement date
    and quality rating average
    """
    from .models import Performance

    print(instance._pre_save_status)
    vendor = instance.vendor
    total_completed_order = PurchaseOrder.objects.filter(
        vendor=vendor, status=PurchaseOrder.Status.COMPLETED
    )
    # Update on-time delivery rate
    if (
        instance._pre_save_status != instance.status
        and instance.status == PurchaseOrder.Status.COMPLETED
    ):
        vendor = instance.vendor
        on_time_delivered_count = total_completed_order.filter(
            delivery_date__lte=F("acknowledgment_date")
        ).count()

        total_completed_order_count = total_completed_order.count()
        print(total_completed_order_count)
        on_time_delivery_rate = on_time_delivered_count / total_completed_order_count

        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.save(update_fields=["on_time_delivery_rate"])

    # Update quality rating average
    completed_po_with_rating = total_completed_order.exclude(quality_rating=None)
    quality_rating_avg = completed_po_with_rating.aggregate(Avg("quality_rating"))
    print(quality_rating_avg)
    quality_rating_avg = list(quality_rating_avg.values())[0]
    vendor.quality_rating_avg = quality_rating_avg
    vendor.save(update_fields=["quality_rating_avg"])

    # Update average response time
    average_response_time = PurchaseOrder.objects.filter(
        vendor=vendor, acknowledgment_date__isnull=False
    ).aggregate(
        avg_response_time=Avg(
            (F("issue_date") - F("acknowledgment_date")),
            output_field=models.DurationField(),
        )
    )
    response_time_duration = average_response_time["avg_response_time"]
    average_response_time_in_hours = response_time_duration.total_seconds() / 3600
    print("response time", average_response_time_in_hours)
    vendor.average_response_time = average_response_time_in_hours
    vendor.save(update_fields=["average_response_time"])

    # Update fulfillment rate
    all_purchase_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    fullfiled_pos = total_completed_order.count()
    fulfillment_rate = (fullfiled_pos / all_purchase_orders) * 100
    print("fulfillment_rate", fulfillment_rate)
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save(update_fields=["fulfillment_rate"])

    # Save to Performance model
    performance, created = Performance.objects.get_or_create(vendor=vendor)
    performance.on_time_delivery_rate = vendor.on_time_delivery_rate
    performance.quality_rating_avg = quality_rating_avg
    performance.average_response_time = average_response_time_in_hours
    performance.fulfillment_rate = fulfillment_rate
    performance.save()
