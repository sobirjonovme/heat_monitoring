from django.apps import apps
from django.db import models


class DailyReportQuerySet(models.QuerySet):
    def annotate_sold_egg_boxes(self):
        """Annotate sales_report_count field to queryset."""
        sales_report_model = apps.get_model("chicken_farm", "FarmSalesReport")
        sub_query = sales_report_model.objects.filter(sold_at__date=models.OuterRef("date"))
        sub_query = sub_query.aggregate(models.Sum("sold_egg_boxes"))

        return self.annotate(
            sold_egg_boxes1=models.Value(sub_query["sold_egg_boxes__sum"], output_field=models.IntegerField())
        )


class DailyReportManager(models.Manager.from_queryset(DailyReportQuerySet)):  # type: ignore
    pass
