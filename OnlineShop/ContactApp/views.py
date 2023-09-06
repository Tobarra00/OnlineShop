from django.shortcuts import render, redirect
from ContactApp import forms, models


# Create your views here.

def contact(request):
    
    contact_form = forms.ContactForm()
    
    if request.method == 'POST':
        contact_form = forms.ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            
            new_email = models.Contact(c_name=name, c_email=email, c_content=content)
            new_email.save()
            
            return redirect('/contact/?valid')
    
    return render(request, 'ContactApp/contact.html', {'c_form': contact_form})