from django.shortcuts import render

# Create your views here.

from .models import Teacher, Institute, Courses

def course_view(request):
	return render(request, 'pages/course.html')
