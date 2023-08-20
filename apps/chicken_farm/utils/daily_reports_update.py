from apps.chicken_farm.models import FarmDailyReport, FarmResource

__all__ = ["bulk_update_daily_reports"]


def bulk_update_daily_reports(start_report):
    """
    Updates daily reports from start report to the last report
    Because daily reports are dependent on each other, we need to update them
    """
    # update start report
    start_report.update_according_to_previous()

    # get all daily reports posted after start report
    reports = FarmDailyReport.objects.filter(date__gt=start_report.date).order_by("date")
    # reports = reports.annotate_sold_egg_boxes()

    # loop through reports and update
    # previous_report = (
    #     FarmDailyReport.objects.filter(id=start_report.id).
    #     annotate_sold_egg_boxes().first()
    # )
    previous_report = start_report
    for report in reports:
        # update daily report
        report.total_remaining_eggs = (
            previous_report.total_remaining_eggs + report.laid_eggs - report.broken_eggs - report.sold_egg_boxes * 30
        )
        report.remaining_chickens = previous_report.remaining_chickens - report.dead_chickens
        report.productivity = round(int(report.laid_eggs) / int(report.remaining_chickens) * 100, 1)
        previous_report = report

    # bulk update reports
    FarmDailyReport.objects.bulk_update(reports, ["total_remaining_eggs", "remaining_chickens", "productivity"])

    # update Farm Resource
    FarmResource.update_according_to_last_report()
