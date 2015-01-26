from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice, Person

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	
	return render(request, 'index.html', {})
