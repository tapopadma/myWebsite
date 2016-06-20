from django import forms 

class ContactForm(forms.Form):
	first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First name', 'class' : 'form-control'}))
	last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class' : 'form-control'}))
	from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email id', 'class' : 'form-control'}))
	subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class' : 'form-control'}))
	message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Write here...', 'class' : 'form-control'}))