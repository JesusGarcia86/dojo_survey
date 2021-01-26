from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['fname'],
            'location': request.POST['place'],
            'language': request.POST['language'],
        }
        return render(request, 'resultsurvey.html', context)
    return render(request, 'resultsurvey.html')

# Create your views here.
