from django.shortcuts import render, redirect
from app.models import Coffee
from app.models import Transaction
from datetime import datetime

# Create your views here.
# def home(request):
#     return render(request, "app/coffee_list.html", {"coffees": Coffee.objects.all()})

# def transaction_detail(request, id):
#     transaction = Transaction.objects.get(id=id)
#     return render(request, "app/transaction_detail.html", {"transaction": transaction})

# def buy_coffee(request, id):
#     if request.method == "GET":
#         return render(request, "app/transaction_detail.html")
#     elif request.method == "POST":
#         coffee = Coffee.objects.get(id=id)
#         transaction = coffee.transaction_set.create(time=datetime.now(), pre_tax=coffee.price, tax=coffee.price * 0.07)
#         transaction.save()
#         return redirect("transaction_detail", transaction.id)

def home(models.Model):
    