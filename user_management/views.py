from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.views import PasswordChangeView
from .models import Role, User
from django.urls import reverse_lazy
from .forms import SignUpForm, CustomUserCreationForm, RoleForm, CustomUserChangeForm, PasswordChangingForm

class UsersListView(ListView):
    model = User
    template_name = 'lists/users_list.html'
    context_object_name = 'users'
    
class RolesListView(ListView):
    model = Role
    template_name = 'lists/roles_list.html'
    context_object_name = 'roles'

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class AddUserView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'add_pages/add_user.html'
    success_url = reverse_lazy('users-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.instance.set_password(form.cleaned_data['password1'])
        form.instance.save()
        return response
    
class EditUserView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'edit_pages/edit_user.html'
    success_url = reverse_lazy('users-list')

class AddRoleView(CreateView):
    model = Role
    form_class = RoleForm
    template_name = 'add_pages/add_role.html'
    success_url = reverse_lazy('roles-list')

class EditRoleView(UpdateView):
    model = Role
    form_class = RoleForm
    template_name = 'edit_pages/edit_role.html'
    success_url = reverse_lazy('roles-list')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html')

class UserDetailView(DetailView):
    model = User
    template_name = 'details/user_detail.html'

class RoleDetailView(DetailView):
    model = Role
    template_name = 'details/role_detail.html'