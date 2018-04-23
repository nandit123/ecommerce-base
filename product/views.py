from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from product.forms import ContactForm
from product.models import Product
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DeleteView


class IndexView(generic.TemplateView):
    template_name = 'product/index.html'


class AboutView(generic.TemplateView):
    template_name = 'product/about.html'


class ContactView(generic.TemplateView):
    template_name = 'product/contact.html'


class CategoryView(generic.ListView):
    template_name = 'product/category.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()


class ProductView(generic.DetailView):
    model = Product
    template_name = 'product/product.html'


class CartView(generic.TemplateView):
    template_name = 'product/cart.html'


class ProductCreate(generic.CreateView):
    model = Product
    fields = ['name', 'price', 'description', 'product_photo']


class ProductUpdate(generic.UpdateView):
    model = Product
    fields = ['name', 'price', 'description', 'product_photo']


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product:category')


def email(request):
    def __init__(self, user):
        self.user = user

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.user)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['HR@company.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/thanks/')
    return render(request, "product/contact.html", {'form': form})


def thanks(request):
    return render(request, 'product/thanks.html')