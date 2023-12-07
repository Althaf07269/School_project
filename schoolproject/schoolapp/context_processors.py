from .models import Course
def menu(request):
    links=Course.objects.all()
    return dict(links=links)
