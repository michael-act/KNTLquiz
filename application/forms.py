from django import forms

class GiveAnswer(forms.Form):
	answer = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control form-control-lg text-center text-uppercase', 
				'placeholder': 'Jawaban kamu disini'
			}
		), 
		max_length=6, 
		min_length=6)