from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()
    output = ",".join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request ))

def about(request):
    return HttpResponse("About page")

def detail(request, question_id):
       question = get_object_or_404(Question, pk=question_id)
       return render(request, 'polls/detail.html', {'question': question})
    
def results(request, question_id):
    question  = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
    # return HttpResponse("You're looking at results for quesiton: %s" % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
         selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
         return render(request, 'polls:detail',{'question': question, 'error_message': "You didn't select a choice"})
    else:
         selected_choice.votes += 1
         selected_choice.save()
         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))     
    # return HttpResponse("You're voting on question: %s" % question_id)
