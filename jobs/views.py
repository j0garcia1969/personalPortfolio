from django.shortcuts import render

# Create your views here.
def johnpaul(request):
    return render(request, 'jobs/home.html')
