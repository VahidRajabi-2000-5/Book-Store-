from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class ProfileView(generic.DetailView):
    model = get_user_model()
    template_name = "registration/profile_view.html"


class ProfileEditView(generic.UpdateView):
    model = get_user_model()
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
    template_name = "registration/profile_edit.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("profile_view", kwargs={"pk": self.request.user.pk})
