from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Pet

# Create your views here.
def home(request):
    # return HttpResponse('Home View Page')
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})

def pet_detail(request, id):
        #return HttpResponse('pet detail page and id is {}'.format(id))

    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {'pet': pet})