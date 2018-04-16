from django.shortcuts import render
#from django.http import HttpResponse

from .models import Employees
from .forms import AreaRestritaCore

# Create your views here.

def principal(request):
	emps = Employees.objects.all()

	if request.method == 'POST':
		dadosForm = AreaRestritaCore(request.POST)
	else:
		dadosForm = AreaRestritaCore()

	context = {
	    'emps': emps,
	    'formLogin': dadosForm
	}
	template_name = 'home.html'

	return render(request, template_name, context)