from typing import Any
from urllib import request
from django.shortcuts import render
from django.contrib import messages# for alert messages 
from . models import (
    UserProfile,
    Portfolio,
    Blog,
    Testimonial,
    Certificate
)
from django.views import generic# using inbuilt template and various django views 
from . forms import ContactForm

# Create your views here.We are creating a home page view here 
class IndexView(generic.TemplateView):
    
    template_name = "main/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        
        
        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        
        return context

class ContactView(generic.FormView):
    
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/" #where user will be redirected when the form is valid
    
    def form_valid(self,form):
        form.save()
        messages.success(self.request,'Thank you, we wil be in touch soon')
        return super().form_valid(form)
        
class PortfolioView(generic.ListView):
    
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10
    
    def get_queryset(self):
        # Directly filter the queryset returned by super()
        return super().get_queryset().filter(is_active=True)
    
class PortfolioDetailView(generic.DetailView):
    
    model = Portfolio
    template_name = "main/portfolio-detail.html"
    paginate_by = 10
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    
class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self):
        # Directly filter the queryset returned by super()
        return super().get_queryset().filter(is_active=True)
    
class BlogDetailView(generic.DetailView):
    
    model = Blog
    template_name = "main/blog-detail.html"
    paginate_by = 10
    
    def get_queryset(self):
        return super().get_queryset.filter(is_active=True)
    

    
    
    
    

