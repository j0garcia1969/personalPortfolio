from django.shortcuts import render
from .models import Job
# Create your views here.
def johnpaul(request):
    jobs = Job.objects  # django pulls all jobs from the db.
    # pass the jobs to home.html with a dictionary of jobs
    return render(request, 'jobs/home.html', {'jobs': jobs})
