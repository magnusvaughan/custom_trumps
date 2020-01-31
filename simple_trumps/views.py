from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the index view of simple trumps")