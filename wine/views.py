from django.shortcuts import render
from django.http import HttpResponse

def wine(request):
    return render(request=request, template_name='index.html', context={})