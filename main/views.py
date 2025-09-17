from django.shortcuts import render, redirect, get_object_or_404
from accounts.decorators import role_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category
from .forms import CategoryForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

@login_required
@role_required([1])  # Only System Admin
def admin_dashboard(request):
    return render(request, "main/admin_dashboard.html")

@login_required
@role_required([2])  # Only Service Provider
def provider_dashboard(request):
    return render(request, "main/provider_dashboard.html")

@login_required
@role_required([3])  # Only Customer
def customer_dashboard(request):
    return render(request, "main/customer_dashboard.html")

@login_required
@role_required([1])
def list_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'main/category_list.html', context)

@login_required
@role_required([1])
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save()
            return redirect('list_category')
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'main/category_form.html', context)

@login_required
@role_required([1])
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("list_category")
    else:
        form = CategoryForm(instance=category)
    context = {
        "form": form,
    }
    return render(request, "main/category_form.html", context)

@login_required
@role_required([1])
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("list_category")
    context = {
        "object": category,
        "type": "Category",
    }
    return render(request, "main/confirm_delete.html", context)
