from django.shortcuts import render, redirect

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

people = []

def add(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        new_person = Person(username, password)
        people.append(new_person)
        return redirect("default")
    return render(request, "add.html")

def default(request):
    return render(request, "default.html", {"people": people})

    