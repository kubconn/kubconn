from django.shortcuts import render,redirect,reverse
from . import models
from . import forms
from .models import ProductImage, Product
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def home_view(request):
    return render(request, 'index.html')


@require_POST
def contact(request):
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")
    service = request.POST.get("service", "")
    message = request.POST.get("message", "")

    send_mail(
        subject=f"KubConn Contact: {name}",
        message=f"""
Нэр: {name}
Email: {email}
Утас: {phone}
Үйлчилгээ: {service}

Мессеж:
{message}
""",
        from_email="info@kubconn.dev",
        recipient_list=["info@kubconn.dev"],
        reply_to=[email] if email else None,
        fail_silently=False,
    )

    return JsonResponse({
        "success": True,
        "message": "Email амжилттай илгээгдлээ."
    })

def custom_404_view(request, exception=None):
    return render(request, "404.html", status=404)