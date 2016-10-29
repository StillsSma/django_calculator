from django.shortcuts import render
from app.models import Profile, Operation
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
        user = request.user
        o = Operation(user=user ,num1=num1, num2=num2, operator=operator)
        o.save()
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

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        if self.request.user.profile.is_owner:
            context['operations'] = Operation.objects.all().order_by('-timestamp')
        else:
            context['operations'] = Operation.objects.filter(user=self.request.user)
        return context

    def get_object(self):
        return Profile.objects.get(user=self.request.user)
