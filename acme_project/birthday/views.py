from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')

class BirthdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'

class BirthdayDeleteView(BirthdayMixin, DeleteView):
    pass

class BirthdayUpdateView(BirthdayMixin, BirthdayFormMixin, UpdateView):
    pass

class BirthdayCreateView(BirthdayMixin, BirthdayFormMixin, CreateView):
    pass

class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10
    
