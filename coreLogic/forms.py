from django import forms


# Simple contact form sends email and message to store owner
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your Full Name. . ."
    }))
    
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': "Your Email Address. . ."
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Send us a message with your email/contact number and we'll get back to you ASAP. . ."
    }))
