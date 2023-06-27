from django.shortcuts import render
from django.http import JsonResponse
from contact.models import Message
from contact.forms import ContactForm



def contact_form(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']

            Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            contact_form.send_mail()

            success = True
            message = 'Contact form sent successfully'
        else:
            success = False
            message = 'Contact form is not valid'
    else:
        success = False
        message = 'Invalid request method'

    context = {
        'success': success,
        'message': message,
    }
    return JsonResponse(context)



def contact(request):
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form
    }
    return render(request, 'contact.html',context)