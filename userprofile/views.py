from django.contrib.auth import login, authenticate, logout
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserForm
from django.views import generic
from django.views.generic import View


class IndexView(generic.TemplateView):
    template_name = 'userprofile/index.html'
    context_object_name = 'user_profile'

    def get_queryset(self):
        return request.user.get_profile()


def logout_view(request):
    logout(request)
    return render(request, 'userprofile/logout.html')


# for new user
class UserFormView(View):
    form_class = UserForm
    template_name='userprofile/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process from data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User object if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        return render(request, self.template_name, {'form': form})