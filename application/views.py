from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import KNTLword
from .forms import GiveAnswer
from .kntlquiz import mask_word, check_game

# Create your views here.
def quiz(request, word_id):
	try:
		if request.session['last_visited'][1:] != str(word_id):
			return HttpResponseRedirect(request.session['last_visited'])
	except:
		pass

	request.session['last_visited'] = '/' + str(word_id)

	data = KNTLword.objects.get(word_id=word_id)
	dict_data = {'word_id': data.word_id, 
				 'next_word_id': word_id+1, 
				 'real_word': data.word, 
				 'word_desc': data.word_desc}

	real_word = dict_data['real_word']
	dict_data['mask_word'] = mask_word(real_word)

	if request.method == 'POST':
		form = GiveAnswer(request.POST)
		if form.is_valid():
			ans_word = form.cleaned_data['answer'].upper()
			if check_game(real_word, ans_word):
				next_word_id = dict_data['next_word_id']
				request.session['last_visited'] = '/' + str(next_word_id)
				return HttpResponseRedirect(f'/{next_word_id}')

	form = GiveAnswer()
	dict_data['form'] = form

	return render(request, 'application/quiz.html', dict_data)