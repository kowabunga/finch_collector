from django.shortcuts import render

# THIS IS SIMULATING A MODEL, JUST FOR TODAY,
# SO WE HAVE DATA TO INJECT INTO OUR TEMPLATES
class Finch:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, color, description, age):
        self.name = name
        self.color = color
        self.description = description
        self.age = age


# This the array, we are injecting into the template
finchs = [
    Finch("Lolo", "purple", "looks like flappy bird", 3),
    Finch("Sachi", "orange", "lazy stupid bird", 0),
    Finch("Raven", "green", "normal i think?", 4),
]


# After this lesson this code will not be used
# because we'll use a REAL MODEL that can talk
# to the DB
##############################################


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def all_finches(request):
    return render(request, "finchs/index.html", {"finchs": finchs})
