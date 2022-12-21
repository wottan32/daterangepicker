from django.shortcuts import render
from .forms import MyForm


# Create your views here.
def my_view(request):
    form = MyForm()
    context = {'form': form}
    return render(request, 'home.html', context)
