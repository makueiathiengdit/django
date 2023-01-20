from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

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
    return HttpResponse("Your'e looking at question :%s " % question_id)
def results(request, question_id):
    return HttpResponse("You're looking at results for quesiton: %s" % question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question: %s" % question_id)