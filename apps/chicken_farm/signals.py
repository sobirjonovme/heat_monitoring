from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.chicken_farm.models import (FarmDailyReport, FarmResource,
                                      FarmSalesReport)


# Define the signal handler function
@receiver(post_save, sender=FarmDailyReport)
def daily_report_post_signal(sender, instance, created, **kwargs):
    # get FARM RESOURCE
    farm_resource = FarmResource.get_solo()

    if created:
        # update FARMS RESOURCE
        farm_resource.eggs_count += instance.laid_eggs - instance.broken_eggs
        farm_resource.chickens_count -= instance.dead_chickens
        farm_resource.save()

        # store total remaining eggs and remaining chickens in daily report
        instance.total_remaining_eggs = farm_resource.eggs_count
        instance.remaining_chickens = farm_resource.chickens_count

        # calculate daily productivity
        productivity = instance.laid_eggs / farm_resource.chickens_count * 100
        # round productivity to 1 decimal places
        instance.productivity = round(productivity, 1)
        instance.save()


@receiver(post_save, sender=FarmSalesReport)
def sales_report_post_signal(sender, instance, created, **kwargs):
    # get FARM RESOURCE
    farm_resource = FarmResource.get_solo()

    if created:
        # calculate debt and update instance
        instance.debt_payment = (
                instance.price_per_box * instance.sold_eggs - instance.card_payment - instance.cash_payment
        )
        instance.save()
        # update FARMS RESOURCE
        farm_resource.eggs_count -= instance.sold_eggs_count
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
