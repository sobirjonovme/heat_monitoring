from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.chicken_farm.models import FarmResource, FarmSalesReport


# Define the signal handler function
@receiver(post_save, sender=FarmSalesReport)
def sales_report_post_signal(sender, instance, created, **kwargs):
    # get FARM RESOURCE
    farm_resource = FarmResource.get_solo()

    if created:
        # update FARMS RESOURCE
        farm_resource.eggs_count -= instance.sold_egg_boxes * 30
        farm_resource.save()


# @receiver(pre_save, sender=DailyReport)
# def daily_report_pre_signal(sender, instance, **kwargs):
#     # get FARM RESOURCE
#     farm_resource = FarmResource.get_solo()
#
#     # if updating, not creating
#     if instance.id:
#         # get old instance
#         old_instance = DailyReport.objects.get(id=instance.id)
#
#         # update farm resource
#         farm_resource.eggs_count -= old_instance.laid_eggs - old_instance.broken_eggs - old_instance.sold_eggs
