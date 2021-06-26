from django.shortcuts import render
from .models import Interview
from .forms import InterviewForm
# Create your views here.


def index(request):
    interview_objects = Interview.objects.all()

    return render(request, "list.html", {'interview_obj': interview_objects})


def create_interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)

        if form.is_valid():
            interviewer = form.cleaned_data["interviewer"]
            interviewee = form.cleaned_data["interviewee"]
            start_time = form.cleaned_data["start"]
            end_time = form.cleaned_data["end"]
            try:
                Interview.objects.create(
                    interviewer=interviewer,
                    interviewee=interviewee,
                    start=start_time,
                    end=end_time,
                    upcoming=True
                )
            except Exception as e:
                raise Exception(f"Error encountered {e}")
        else:
            print("request = ", request)
            raise Exception("Please give correct values in the form")

    return render(request, 'create.html', {'form': InterviewForm()})
