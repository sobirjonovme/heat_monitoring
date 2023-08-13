# import random
#
# import factory
# from django.contrib.gis.geos import Point
# from django.utils import timezone
#
# from apps.chicken_farm.models import (FarmDailyReport, FarmExpense,
#                                       FarmExpenseType, FarmSalesReport)
#
# TZ_INFO = timezone.get_current_timezone()
#
#
# class CompanyParentCategoryFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = CompanyCategory
#
#     parent = None
#     title = factory.Faker("word")
#     icon = factory.SubFactory("apps.care.factories.CareMediaFactory")
#     order = factory.Sequence(lambda n: n)
#     description = factory.Faker("text")
#     created_at = factory.Faker("date_time", tzinfo=TZ_INFO)
#     updated_at = factory.Faker("date_time", tzinfo=TZ_INFO)
#
#
# class CompanyCategoryFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = CompanyCategory
#
#     parent = factory.SubFactory(CompanyParentCategoryFactory)
#     title = factory.Faker("word")
#     icon = factory.SubFactory("apps.care.factories.CareMediaFactory")
#     order = factory.Sequence(lambda n: n)
#     description = factory.Faker("text")
#     created_at = factory.Faker("date_time", tzinfo=TZ_INFO)
#     updated_at = factory.Faker("date_time", tzinfo=TZ_INFO)
#
#
# class CompanyFactory(factory.django.DjangoModelFactory):
#     """
#     Extra kwargs usage:
#
#     - categories: list of categories to add to the company
#     example: CompanyFactory(categories=[CompanyCategoryFactory(), CompanyCategoryFactory()])
#
#     - projects: number of projects to add to the company
#     if -1 is passed in, a random number of projects will be added
#     if a specific number is passed in, that many projects will be added
#     if no number is passed in, no projects will be added
#     example: CompanyFactory(projects=5), CompanyFactory(projects=-1)
#
#     - followers: number of followers to add to the company
#     if -1 is passed in, a random number of followers will be added
#     if a specific number is passed in, that many followers will be added
#     if no number is passed in, no followers will be added
#     """
#
#     class Meta:
#         model = "company.Company"
#
#     name = factory.Faker("company")
#     legal_name = factory.LazyAttribute(lambda o: f"{o.name} legal name")
#     brand_logo = factory.SubFactory("apps.care.factories.CareMediaFactory")
#     cover_image = factory.SubFactory("apps.care.factories.CareMediaFactory")
#     old_review_rating = factory.Faker("random_int", min=1, max=5)
#
#     type = factory.Faker("random_element", elements=CompanyType.values)
#     short_description = factory.Faker("text", max_nb_chars=100)
#     register_date = factory.Faker("date_time", tzinfo=TZ_INFO)
#     about = factory.Faker("text")
#     phone_number = factory.Faker("phone_number")
#     phone_number_verified = factory.Faker("boolean")
#     email = factory.Faker("email")
#     email_verified = factory.Faker("boolean")
#     website = factory.Faker("url")
#     address = factory.Faker("address")
#
#     longitude = -90
#     latitude = -180
#     point = Point(5, 23, 8)
#
#     region = factory.SubFactory("apps.care.factories.RegionFactory")
#     verified = factory.Faker("boolean")
#     is_active = True
#     tin = factory.Faker("ssn")
#     work_type = factory.Faker("random_element", elements=Company.WORK_TYPE.values)
#     created_at = factory.Faker("date_time", tzinfo=TZ_INFO)
#     updated_at = factory.Faker("date_time", tzinfo=TZ_INFO)
