"""
Send email for some views.
"""
from django.core.mail import send_mail, mail_admins
from django.core.urlresolvers import reverse

from .settings import DEFAULT_FROM_EMAIL

def reverse_full(*args, **kargs):
    """Return the full address using Django reverse."""
    # FIXME Avoid hard code the domain.
    return 'http://dev.lowfat.software.ac.uk{}'.format(reverse(*args, **kargs))

def new_fund_notification(fund):
    # Email to admin
    mail_admins(
        "New fund request",
        "Please review {}.".format(
            reverse_full("fund_review", args=[fund.id])
        ),
        fail_silently=False,
    )

    # Email to user
    send_mail(
        'Your fund request was received',
        'You can check the information of your fund at {}.'.format(
            reverse_full("fund_detail", args=[fund.id])
        ),
        DEFAULT_FROM_EMAIL,
        [fund.claimant.email],
        fail_silently=False
    )

def new_expense_notification(expense):
    # Email to admin
    mail_admins(
        "New expense submited",
        "Please process {}.".format(
            reverse_full("expense_review", args=[expense.id])
        ),
        fail_silently=False,
    )

    # Email to user
    send_mail(
        'Your new expense claim was received',
        'You can check the information of your expense claim at {}.'.format(
            reverse_full("expense_detail", args=[expense.id])
        ),
        DEFAULT_FROM_EMAIL,
        [expense.fund.claimant.email],
        fail_silently=False
    )

def new_blog_notification(blog):
    # Email to admin
    mail_admins(
        "New blog request",
        "Please review {}.".format(
            reverse_full("fund_review", args=[blog.id])
        ),
        fail_silently=False,
    )

    # Email to user
    send_mail(
        'Your new blog post was received',
        'You can check the information of your fund at {}.'.format(
            reverse_full("fund_detail", args=[blog.id])
        ),
        DEFAULT_FROM_EMAIL,
        [blog.fund.claimant.email],
        fail_silently=False
    )

def fund_review_notification(mail):
    # Email to user
    send_mail(
        'Update on your funding request',
        mail.justification,
        mail.sender.email,
        [mail.receiver.email],
        fail_silently=False
    )

def expense_review_notification(mail):
    # Email to user
    send_mail(
        'Update on your expense claim',
        mail.justification,
        mail.sender.email,
        [mail.receiver.email],
        fail_silently=False
    )

def blog_review_notification(mail):
    # Email to user
    send_mail(
        'Update on your blog post',
        mail.justification,
        mail.sender.email,
        [mail.receiver.email],
        fail_silently=False
    )