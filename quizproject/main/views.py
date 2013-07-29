# set encoding=utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from models import *
import re

def post_answer(userprofile, choice_id):
	"""
	This function creates a new UserAnswer and updates the userprofile.
	"""
	user_answer = UserAnswer()
	user_answer.userprofile = userprofile
	user_answer.choice = Choice.objects.get(id=choice_id)
	user_answer.save()

@login_required
def home(request):
	"""
	This function returns the home view. The User will be redirected to
	'account/login/' if not logged in.
	"""
	question_list = Question.objects.all().order_by('?')[:10]
	userprofile = request.user.get_profile()

	if not userprofile.has_taken_quiz():
		return render(request, 'main/home.html', {'question_list': question_list})
	else:
		num_correct_answes = userprofile.num_correct_answers()
		has_taken_quiz= userprofile.has_taken_quiz()
		answers = userprofile.answers()
		return render(request, 'main/result.html', {'answers': answers,  'num_correct_answes': num_correct_answes, 'has_taken_quiz': has_taken_quiz})
@login_required
def submit(request):
	"""
	This function fetches the data from the submitted form and saves it.
	"""
	userprofile = request.user.get_profile()
	if request.method == 'POST':

		# This line checks if the UserProfile has any UserAnswers yet.
		if not userprofile.has_taken_quiz():
			for question_id, choice_id in request.POST.iteritems():
				# This line uses regex to match the question from the input form
				if re.match(r'^\d+$', question_id):
					post_answer(userprofile, choice_id)

		else:
			num_correct_answes = userprofile.num_correct_answers()
			has_taken_quiz= userprofile.has_taken_quiz()	
			answers = userprofile.answers()
			return render(request, 'main/result.html', {'answers': answers,  'num_correct_answes': num_correct_answes, 'has_taken_quiz': has_taken_quiz})
	else:
		return redirect('/')
	num_correct_answes = userprofile.num_correct_answers()
	has_taken_quiz = False
	answers = userprofile.answers()
	return render(request, 'main/result.html', {'answers': answers,  'num_correct_answes': num_correct_answes, 'has_taken_quiz': has_taken_quiz})
def logout_view(request):
	"""
	This function logs out the user.
	"""
	logout(request)
	# return HttpResponseRedirect('../login/')

	# return HttpResponse('Logget ut')

	return render(request, 'main/logout.html')

