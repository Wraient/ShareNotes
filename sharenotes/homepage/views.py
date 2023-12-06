from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "homepage/index.html", {
        "first_name": "John",
        "last_name": "Doe",
        "username": "@johndoe",
        "time": "1 hour ago",
        "college_name": "ADYPSOE",
        "subject": "BEE",
        "chapter":"Unit-1",
        "post_title": "How to make a website",
        "post_content": "This is how you make a website.",
    })
