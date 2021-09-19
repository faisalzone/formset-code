from django.shortcuts import render
from django.forms import modelformset_factory
from .models import Example
from .forms import ExampleForm

# Create your views here.


def index(request):
    # Extra defaults to one.
    # ExampleFormSet = modelformset_factory(Example,
    #            fields=('name', 'location', 'photo'),
    #                                       extra=1)

    ExampleFormSet = modelformset_factory(Example, form=ExampleForm, extra=1)

    # queryset here will make sure no saved object is displayed
    # For a creation form, queryset is better to be none as we want the users
    # to enter data
    # form = ExampleFormSet(queryset=Example.objects.none())

    if request.method == 'POST':
        form = ExampleFormSet(request.POST, request.FILES)
        # form.save() will save all of the values. similar to modelform
        # To save individually, we can do a instances = form.save(commit=false)
        # instances = form.save(commit=False)
        #     for instance in instances:
        #         instance.save()

        # instances = form.save()
        form.save()
    form = ExampleFormSet(queryset=Example.objects.none())
    context = {
        'form': form,
    }
    return render(request, 'myapp/index.html', context)
