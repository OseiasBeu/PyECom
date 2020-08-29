#coding=utf-8
from django.shortcuts import render
from django.urls import reverse_lazy
# from django.core.urlresolvers import 
from django.http import  HttpResponse
from catalog.models import  Category
from .forms import ContactForm
from django.core.mail import  send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import  View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.

User = get_user_model()

class IndexView(TemplateView):
    template_name = 'index.html'
    
index = IndexView.as_view()


def  contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_Mail()
        success = True   
    elif request.method == 'POST':
        messages.error(request, 'Formulário Inválido')          
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html',context)
