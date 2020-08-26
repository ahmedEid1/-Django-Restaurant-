from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory


# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multi_form = MultiplePizzaForm()
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
                           'note': note,
                           'multi_form': multi_form})

    form = PizzaForm()
    return render(request, 'pizza/order.html',
                  {'pizza_form': form, 'multi_form': multi_form})


def pizzas(request):
    number_of_pizzas = 2
    filled_multi_pizza_form = MultiplePizzaForm(request.GET)

    if filled_multi_pizza_form.is_valid():
        number_of_pizzas = filled_multi_pizza_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == "POST":
        filled_form_set = PizzaFormSet(request.POST)
        if filled_form_set.is_valid():
            for form in filled_form_set:
                print(form.cleaned_data['topping1'])
            note = 'pizzas created successfully'
        else:
            note = 'something went wrong try again'
        return render(request, 'pizza/pizzas.html',
                      {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/pizzas.html',
                      {'formset': formset})

