from django.shortcuts import render, redirect

from contact.forms import ContactForm
from contact.models import ContactMessage, Category


# Create your views here.


def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    ctx = {'form': form}
    return render(request, 'contact/index.html', context=ctx)

def success(request):
    return render(request,'contact/congrats.html')












