from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from products.models import Product


class PaymentView(LoginRequiredMixin, View):
    template_name = 'payments/payment.html'

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        # Implement payment processing logic here
        return render(request, self.template_name, {'product': product})
