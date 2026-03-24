from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import LandUseRecord, CropTypeRecord


@receiver(post_save, sender=LandUseRecord)
def sync_landuse_on_save(sender, instance, **kwargs):
    print(f"Signal fired for LandUseRecord id={instance.id} level={instance.level}")
    instance.sync_county_totals()


@receiver(post_save, sender=CropTypeRecord)
def sync_croptype_on_save(sender, instance, **kwargs):
    print(f"Signal fired for CropTypeRecord id={instance.id}")
    instance.sync_county_totals()