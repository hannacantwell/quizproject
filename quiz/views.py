from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1,
   		"name": "Universum",
	   	"description": "Har du koll på vintergatan?"
	},
	{
		"quiz_number": 2,
   	   	"name": "Jorden",
	   	"description": "Hur mycket vet du om vår planet?"
	},
	{
		"quiz_number": 3,
   	    	"name": "Världens hav",
	    	"description": "Vad för fiskar simmar i våra hav?"	},
]


def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[int(quiz_number) - 1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
	    	"question": "Hur många bultar har ölandsbron?",
		"answer1": "12",
	   	"answer2": "66 400",
	    	"answer3": "7 428 954",
	    	"quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)

def completed(request, quiz_number):
	context = {
	    	"correct": 12,
	    	"total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/results.html", context)
