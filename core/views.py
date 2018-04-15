from django.shortcuts import render
from django.http import HttpResponse

from .models import Employees


# Create your views here.

def principal(request):

	emps = Employees.objects.all()

	template_name = 'home.html'
	context = {
		'emps' : emps
	}
	return render(request, template_name, context)

	
