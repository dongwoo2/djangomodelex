from django.shortcuts import render

# Create your views here.

from .models import Info

def list(request):
    info_list = Info.objects.all()
    context = {
        'info_list' : info_list
    }
    return render(request, 'ex_model/list.html', context)