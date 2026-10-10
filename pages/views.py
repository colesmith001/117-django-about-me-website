from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def about_me_view(request):
  return render(request,'pages/about_me.html')

def contact_view(request):
  #POST : visitor submitted form
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      message = form.cleaned_data['message']

      message_body=(
        f'New message from your portfolio\n'
        f'name:{name}\n'
        f'email:{email}\n'
        f'message: {message}'
      )
      try:
        send_mail(
          'message from your portfolio',
          message_body,
          email, 
          ['colejsmith001@gmail.com'],

        )
        form = ContactForm()
        return render(request,'pages/contact.html', {'form':form})
      except Exception as e:
        return render(request, 'pages/contact.html', {'form':form})

    else :
        return render(request, 'pages/contact.html', {'form':form})

  else : 
    form = ContactForm()
    return render(request,'pages/contact.html',{'form': form})
    
def experience_view(request):
  return render(request, 'pages/experience.html')