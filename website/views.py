from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (ListView, DetailView,CreateView)
from .forms import ContactForm
from .models import Post

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render (request ,'website/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'website/home.html' #<app><model>_<Viewtype>.html
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
class PostCreateView(CreateView):
    model = Post
    fields = ['post']






def about(request):
    return render (request ,'website/about.html')
def vision(request):
    return render (request ,'website/vision.html')
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "website/contact.html", {'form': form})