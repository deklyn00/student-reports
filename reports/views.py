from django.shortcuts import render

# Create your views here.


def get_reports(request):
    return render(request, 'templates/reports/report_cards.html')
