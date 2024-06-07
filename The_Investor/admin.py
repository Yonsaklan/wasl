from django.contrib import admin
from .models import Investor , Favorite , InvestmentRequest, InvestorRatingComment, Report



admin.site.register(Investor)
admin.site.register(Favorite)
admin.site.register(InvestmentRequest)
admin.site.register(InvestorRatingComment)
admin.site.register(Report)

