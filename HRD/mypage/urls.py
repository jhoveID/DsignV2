from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="main_page"),
    path("sync/",views.syncPage, name="sync_page"),    
    path("staff/", views.staffPage, name="sync_page"),
    path("holiday/", views.holidayPage, name="sync_page"),
    path("payslip/", views.payslipPage, name="sync_page"),
    path("payslipSummary/", views.payslipSummaryPage, name="sync_page"),




]
