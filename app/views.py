from django.shortcuts import render
from app.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.


def index_view(request):
    if request.GET:

        num1 = request.GET['num1']
        num2 = request.GET['num2']
        operator = request.GET['operator']
        try:
            if operator == "+":
                answer = int(num1) + int(num2)
            elif operator == "-":
                answer = int(num1) - int(num2)
            elif operator == "*":
                answer = int(num1) * int(num2)
            elif operator == "/":
                if int(num2) == 0:
                    answer = "ERROR"
                else:
                    answer = int(num1) / int(num2)
        except ValueError:
            Error = "ERROR"
            answer = 0
        context = {
        "answer": answer,
        "num1": num1,
        "num2": num2,
        "operator": operator,
        }
        return render(request, "index.html", context)

    return render(request, "index.html")


class UserCreateView(CreateView):
    model = User
    success_url = "/"
    form_class = UserCreationForm

class ProfileUpdateView(UpdateView):
    template_name = "profile.html"
    fields = ('access_level',)
    success_url = reverse_lazy('profile_view')

    def get_object(self):
        return Profile.objects.get(user=self.request.user)
