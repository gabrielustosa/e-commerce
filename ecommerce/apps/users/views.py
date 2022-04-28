from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from .forms import UserCreateForm
from ecommerce.apps.users.forms import UserEditForm
from .models import Address


class ProfileView(TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        addresses = Address.objects.filter(user=self.request.user)
        context['addresses'] = addresses
        return context


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Perfil salvo com sucesso.')
        else:
            messages.add_message(request, messages.ERROR, 'Algum campo foi preenchido incorretamente')

    form = UserEditForm(instance=request.user)
    return render(request, 'account/edit_profile.html', {'form': form})


class CreateAddressView(CreateView):
    template_name = 'address/address.html'
    model = Address
    fields = ('name', 'postal_code', 'address', 'number', 'complement', 'city', 'state')
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateAddressView, self).form_valid(form)


class UpdateAddressView(UpdateView):
    template_name = 'address/address.html'
    model = Address
    fields = ('name', 'postal_code', 'address', 'number', 'complement', 'city', 'state')
    success_url = reverse_lazy('users:profile')


class DeleteAddressView(DeleteView):
    template_name = 'address/address_delete.html'
    model = Address
    success_url = reverse_lazy('users:profile')


class ManageAddressView(TemplateView):
    template_name = 'address/address_manage.html'

    def get_context_data(self, **kwargs):
        context = super(ManageAddressView, self).get_context_data(**kwargs)
        addresses = Address.objects.filter(user=self.request.user)
        context['addresses'] = addresses
        return context


def register(request):
    if request.POST:
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            account = authenticate(email=user.email, password=form.cleaned_data.get('password1'))
            login(request, account)
            return redirect('shop:home')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', context={
        'form': form
    })
