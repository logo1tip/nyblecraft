from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Worker
from .forms import CreateWorker, UserRegisterForm, UserLoginForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)  
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Success")
            return redirect('home')
        else:
            messages.error(request, "Registration error")
    else:
        form = UserRegisterForm()
    return render(request, "worker/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, "worker/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


class WorkerList(ListView):
    model = Worker
    

class DetailWorker(DetailView):
    model = Worker
    
    
class CreateWorker(CreateView):
    form_class = CreateWorker
    template_name = "worker/add_worker.html"


class DeleteWorker(DeleteView):

    model = Worker
    success_url = reverse_lazy('home')


class UpdateWorker(UpdateView):

    model = Worker






