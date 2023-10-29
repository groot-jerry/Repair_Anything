
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from products.models import Product
from technicians import forms
from technicians.models import Technician


class TechnicianAssignmentView(View):
    template_name = 'technicians/assignment.html'

    def get(self, request):
        product = Product.objects.all()
        # Query available technicians and display them for assignment
        technicians = Technician.objects.all()
        return render(request, self.template_name, {'product': product, 'technicians': technicians})


def TechnicianRegistrationView(request):
    if request.method == 'GET':
        form = forms.TechnicianCreationForm(request.GET)

        if form.is_valid():
            form.save()

            return HttpResponse("technician Created Successfully")

    else:
        form = forms.TechnicianCreationForm()

    return render(request, 'technicians/tech_registration.html', {
        'form': form
    })
