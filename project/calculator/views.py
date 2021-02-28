from django.views.generic import CreateView

from .forms import CalculatorForm


class CreateCalculatorView(CreateView):
    form_class = CalculatorForm
    template_name = 'calculator.html'

    def form_valid(self, form):
        pass
