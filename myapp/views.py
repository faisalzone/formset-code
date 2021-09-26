from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory
from .models import Example, Programmer, Language, Book
from .forms import ExampleForm, BookFormset
from django import forms

# Create your views here.


def index(request):
    # Extra defaults to one.
    # ExampleFormSet = modelformset_factory(Example,
    #            fields=('name', 'location', 'photo'),
    #                                       extra=1)

    ExampleFormSet = modelformset_factory(Example, form=ExampleForm, extra=0)

    # queryset here will make sure no saved object is displayed
    # For a creation form, queryset is better to be none as we want the users
    # to enter data
    # form = ExampleFormSet(queryset=Example.objects.none())

    if request.method == 'POST':
        form = ExampleFormSet(request.POST, request.FILES)
        if form.is_valid():
            # form.save() will save all of the values. similar to modelform
            # To save individually, we can do a instances = form.save(commit=false)
            # instances = form.save(commit=False)
            #     for instance in instances:
            #         instance.save()

            # instances = form.save()
            form.save()
            return redirect("https://google.com/")
    form = ExampleFormSet(queryset=Example.objects.filter(name="First"))
    context = {
        'form': form,
    }
    return render(request, 'myapp/index.html', context)


def inline_example(request, programmer_id):
    programmer = Programmer.objects.get(pk=programmer_id)
    # Programmer is the parent model and Language is the child model, fields
    # are the fields from the child model
    LanguageFormset = inlineformset_factory(Programmer, Language, fields=('name',), can_delete=False, extra=1, max_num=5)

    if request.method == 'POST':
        # instance is the parent model
        formset = LanguageFormset(request.POST, instance=programmer)
        if formset.is_valid():
            formset.save()
            return redirect('inline_example', programmer_id=programmer.id)
    formset = LanguageFormset()
    context = {
        'formset': formset,
    }
    return render(request, 'myapp/inline.html', context)


def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'myapp/book_list.html', context)


def create_book_normal(request):
    template_name = 'myapp/create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Book(name=name).save()
            # once all books are saved, redirect to book list view
            return redirect('book_list')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })
