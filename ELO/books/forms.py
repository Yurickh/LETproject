from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100, min_length=3)
	email = forms.EmailField(required=False, label='Seu email')
	message = forms.CharField(widget=forms.Textarea)

	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Escreve mais ai!")
		return message
