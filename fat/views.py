from datetime import date

import django.utils
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from .models import *
from .forms import *
from .mail import *

def index(request):
    context = {
            'fellows': Fellow.objects.exclude(selected=False).order_by('application_year').reverse(),
            'events': Event.objects.filter(category="H", start_date__gte=django.utils.timezone.now()).order_by("start_date").reverse(),
            }

    if request.user.is_authenticated() and request.user.is_superuser:
        context.update({
            'show_grant_available': True,
            })

    return render(request, 'fat/index.html', context)

@login_required
def dashboard(request):
    context = {}

    if request.user.is_authenticated():
        if not request.user.is_superuser and not request.user.is_staff:
            fellow = Fellow.objects.get(user=request.user)

            context.update({
                'fellow': fellow,
                'events': Event.objects.filter(fellow=fellow).reverse(),
                'budget_available': fellow.fellowship_available(),
                })
        else:
            context.update({
                'events': Event.objects.filter(status__in=['U', 'P']).reverse(),
                'expenses': Expense.objects.filter(status__in=['W', 'S', 'P']).reverse(),
                'blogs': Blog.objects.filter(status__in=['U', 'R']).reverse(),
                })

    return render(request, 'fat/dashboard.html', context)

@login_required
def fellow(request):
    if not request.user.is_superuser and not request.user.is_staff:
       instance = Fellow.objects.get(user=request.user)
    else:
       instance = None

    if request.POST:
        # Handle submission
        formset = FellowForm(request.POST, request.FILES, instance=instance)

        if formset.is_valid():
            fellow = formset.save()
            return HttpResponseRedirect(reverse('fellow_detail',
                args=[fellow.id,]))
    else:
        formset = FellowForm(None, instance=instance)

    # Show submission form.
    context = {
            "title": "Create fellow",
            "formset": formset,
            "submit_text": "Save",
            }
    return render(request, 'fat/form.html', context)

def fellow_detail(request, fellow_id):
    this_fellow = Fellow.objects.get(id=fellow_id)

    if not this_fellow.selected:
        return HttpResponseNotFound("Fellow does not exist.")

    context = {
            'fellow': this_fellow,
            'events': Event.objects.filter(fellow=this_fellow),
            }

    if request.user.is_authenticated() and (request.user.is_superuser or
            Fellow.objects.get(user=request.user) == this_fellow):
            context.update({
                'expenses': Expense.objects.filter(event__fellow=this_fellow),
                'show_finances': True,
                })

    return render(request, 'fat/fellow_detail.html', context)

@login_required
def my_profile(request):
    if not request.user.is_superuser and not request.user.is_staff:
        fellow = Fellow.objects.get(user=request.user)
        return fellow_detail(request, fellow.id)

    return HttpResponseNotFound("Fellow does not exist.")

@login_required
def event(request):
    if request.POST:
        # Handle submission
        post = request.POST.copy()
        fellow = Fellow.objects.get(id=post['fellow'])
        post['fellow'] = fellow.id
        formset = EventForm(post)

        if formset.is_valid():
            event = formset.save()

            # Default value for budget_approved is budget_total.
            # The reason for this is to save staffs to copy and paste the approved amount.
            event.budget_approved = event.budget_total()
            event.save()

            new_event_notification(event)
            return HttpResponseRedirect(reverse('event_detail',
                args=[event.id,]))

    if not request.user.is_superuser:
        initial = {
            "fellow": Fellow.objects.get(user=request.user),
        }
    else:
        initial = {}

    formset = EventForm(initial=initial)

    if not request.user.is_superuser:
        formset.fields["fellow"].queryset = Fellow.objects.filter(user=request.user)

    # Show submission form.
    context = {
            "title": "Submit event",
            "formset": formset,
            "submit_text": "Submit",
            }
    return render(request, 'fat/form.html', context)

@login_required
def event_detail(request, event_id):
    this_event = Event.objects.get(id=event_id)
    
    context = {
            'event': this_event,
                }

    if request.user.is_authenticated():
        if (request.user.is_superuser or
            Fellow.objects.get(user=request.user) == this_event.fellow):
            budget_request = this_event.budget_total()

            context.update({
                    'expenses': Expense.objects.filter(event=this_event),
                    'blogs': Blog.objects.filter(event=this_event),
                    'budget_summary': True,
                    })

    return render(request, 'fat/event_detail.html', context)

@staff_member_required
def event_review(request, event_id):
    this_event = Event.objects.get(id=event_id)

    if request.POST:
        # Handle submission
        formset = EventReviewForm(request.POST, instance=this_event)

        if formset.is_valid():
            event = formset.save()
            return HttpResponseRedirect(reverse('event_detail',
                args=[event.id,]))

    formset = EventReviewForm(None, instance=this_event)

    context = {
            'event': this_event,
            'formset': formset,
            'submit_text': 'Update',
            }

    return render(request, 'fat/event_review.html', context)

def event_past(request):
    events = Event.objects.filter(
            start_date__lt=django.utils.timezone.now(),
            category="H"
            ).order_by("start_date").reverse()

    context = {
            'events': events,
            }

    return render(request, 'fat/event_past.html', context)

@login_required
def expense(request):
    if request.POST:
        # Handle submission
        formset = ExpenseForm(request.POST, request.FILES)

        if formset.is_valid():
            expense = formset.save()
            new_expense_notification(expense)
            return HttpResponseRedirect(reverse('expense_claim',
                args=[expense.id,]))
    else:
        # Store GET parameters
        event_id = request.GET.get("event_id")

        # Setup Event if provided
        if event_id:
            initial = {"event": Event.objects.get(id=event_id)}
        else:
            initial = {}

        formset = ExpenseForm(initial=initial)

        # Limit dropdown list to fellow
        if request.user.is_authenticated() and not request.user.is_superuser:
            fellow = Fellow.objects.get(user=request.user)
            formset.fields["event"].queryset = Event.objects.filter(fellow=fellow)

    # Show submission form.
    context = {
            "title": "Submit expenses",
            "formset": formset,
            "submit_text": "Submit",
            }
    return render(request, 'fat/form.html', context)

@login_required
def expense_claim(request, expense_id):
    context = {
            'expense': Expense.objects.get(id=expense_id),
            }

    return render(request, 'fat/expense_claim.html', context)

@staff_member_required
def expense_review(request, expense_id):
    this_expense = Expense.objects.get(id=expense_id)

    if request.POST:
        # Handle submission
        formset = ExpenseReviewForm(request.POST, instance=this_expense)

        if formset.is_valid():
            expense = formset.save()
            return HttpResponseRedirect(reverse('expense_claim',
                args=[expense.id,]))

    formset = ExpenseReviewForm(None, instance=this_expense)

    context = {
            'expense': this_expense,
            'formset': formset,
            'submit_text': 'Update',
            }

    return render(request, 'fat/expense_review.html', context)

@login_required
def blog(request):
    if request.POST:
        # Handle submission
        formset = BlogForm(request.POST)

        if formset.is_valid():
            blog = formset.save()
            new_blog_notification(blog)
            return HttpResponseRedirect(reverse('blog_detail',
                args=[blog.id,]))
    else:
        event_id = request.GET.get("event_id")
        if event_id:
            initial = {"event": Event.objects.get(id=event_id)}
        else:
            initial = {}
        formset = BlogForm(initial=initial)

        # Limit dropdown list to fellow
        if request.user.is_authenticated() and not request.user.is_superuser:
            fellow = Fellow.objects.get(user=request.user)
            formset.fields["event"].queryset = Event.objects.filter(fellow=fellow)

    # Show submission form.
    context = {
            "title": "Submit blog",
            "formset": formset,
            "submit_text": "Submit",
            }
    return render(request, 'fat/form.html', context)

@login_required
def blog_detail(request, blog_id):
    context = {
            'blog': Blog.objects.get(id=blog_id),
            }

    return render(request, 'fat/blog_detail.html', context)

@staff_member_required
def blog_review(request, blog_id):
    this_blog = Blog.objects.get(id=blog_id)

    if request.POST:
        # Handle submission
        formset = BlogReviewForm(request.POST, instance=this_blog)

        if formset.is_valid():
            blog = formset.save()
            return HttpResponseRedirect(reverse('blog_detail',
                args=[blog.id,]))

    formset = BlogReviewForm(None, instance=this_blog)

    context = {
            'blog': this_blog,
            'formset': formset,
            'submit_text': 'Update',
            }

    return render(request, 'fat/blog_review.html', context)

def geojson(request):
    """Return the GeoJSON file."""

    context = {
            'fellows': Fellow.objects.all(),
            'events': Event.objects.all(),
            }

    return render(request, 'fat/map.geojson', context)
