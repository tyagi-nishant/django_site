from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
    return render(request, 'home.html')

@csrf_protect
def index(request):
    return render(request, 'index.html')
@csrf_protect
def your_view(request):
    if request.method == 'POST':
        # Handle form submission
        question_text = request.POST.get('question')
        choice1 = request.POST.get('choice1')
        choice2 = request.POST.get('choice2')
        choice3 = request.POST.get('choice3')
        # Insert logic to save question and choices
        pass
    return render(request, 'polls/form.html', {})
