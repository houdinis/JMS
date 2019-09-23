from django.shortcuts import render
from user.minxins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from .models import Perm
from django.urls import reverse_lazy
from .forms import PermListForm
from django.utils import timezone


class PermList(LoginRequiredMixin, ListView):
    model = Perm
    context_object_name = 'perm'
    # form_class = PermListForm
    template_name = 'perm/list.html'

    form = PermListForm()

    def get_context_data(self, **kwargs):
        context = super(PermList, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context


class PermCreate(LoginRequiredMixin, CreateView):
    model = Perm
    form_class = PermListForm
    success_url = reverse_lazy('perm:list')


class PermDelete(LoginRequiredMixin, DeleteView):
    model = Perm
    success_url = reverse_lazy('perm:list')

# class PermDeleteView(SingleObjectMixin, View):
#     model = Perm
#
#     def post(self, request, *args, **kwargs):
#         perm = self.get_object()
#         perm.delete()
#         return HttpResponse("删除成功")


class PermDetails(DetailView):
    model = Perm
    template_name = 'perm/detail.html'