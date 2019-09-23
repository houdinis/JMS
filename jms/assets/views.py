from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from user.minxins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, View, UpdateView
from .models import Assets
from .forms import AssetCreateForm, AssetUpdateForm
from django.urls import reverse_lazy


class AssetList(LoginRequiredMixin, ListView):
    model = Assets
    context_object_name = 'assets'
    template_name = 'assets/list.html'


class AssetCreate(LoginRequiredMixin, CreateView):
    model = Assets
    form_class = AssetCreateForm
    template_name = 'assets/create.html'
    success_url = reverse_lazy('assets:list')


class AssetDelete(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        assert_id = self.kwargs.get('pk', 0)
        asset = get_object_or_404(Assets, id=assert_id)
        asset.delete()
        return HttpResponseRedirect(reverse_lazy('assets:list'))


class AssetUpdate(LoginRequiredMixin, UpdateView):
    model = Assets
    form_class = AssetUpdateForm
    template_name = 'assets/update.html'
    success_url = reverse_lazy('assets:list')