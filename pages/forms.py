from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(
    max_length=50, widget=forms.TextInput(attrs={
      'class':'form-control mb-3',
      'placeholder':'your name'})
  )
  email = forms.EmailField(
    widget=forms.EmailInput(attrs={
      'class':'form-control mb-3',
      'placeholder':'your email'})
  )
  message= forms.CharField(
    widget=forms.Textarea(attrs={
      'class':'form-control mb-3',
      'placeholder':'your message'})
    )