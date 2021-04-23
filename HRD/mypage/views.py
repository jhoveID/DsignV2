from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#index page
def index(request):
    return render(request, "mypage/index.html")
    
    
def syncPage(request):
    return HttpResponse("<h1> This is sync option page </h1>")
    
    
def payslipPage(request):
    return HttpResponse("<h1> Payslip page </h1>")


def holidayPage(request):
    return HttpResponse("<h1>Holiday page </h1>")


def staffPage(request):
    return HttpResponse("<h1> Staff Setting page </h1>")


def payslipSummaryPage(request):
    return HttpResponse("<h1> Payslip Summary page </h1>")
