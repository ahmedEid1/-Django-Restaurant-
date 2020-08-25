from django.shortcuts import render
from .forms import PizzaForm


# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'thanks for ordering! your %s %s and %s pizza is on its way!' %(
                filled_form.cleaned_data['size'],
                filled_form.cleaned_data['topping1'],
                filled_form.cleaned_data['topping2'])
            new_form = PizzaForm()
            return render(request, 'pizza/order.html',
                          {'pizza_form': new_form,
                           'note': note})

    form = PizzaForm()
    return render(request, 'pizza/order.html',
                  {'pizza_form': form})
