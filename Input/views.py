from django.shortcuts import render
from .models import DataInput

# Create your views here.
def add_new_input(request):
    print("Adding New data")
    data = "DATA INPUT"
    di = DataInput(data=data)

    di.save()

    ctxt = di

    return render(request, 'input/saved.html', {
        'ctxt': di,
    })