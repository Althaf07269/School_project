from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Course
from schoolapp.forms import MyForm


def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def demo(request):
    obj = Course.objects.all()
    context = {
        'result': obj
    }
    return render(request, 'index.html', context)
def formr(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schoolapp:confirmation')
    else:
        form = MyForm()
    return render(request, 'form.html', {'form': form})

def confirmation(request):
    return render(request, 'confirmation.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

