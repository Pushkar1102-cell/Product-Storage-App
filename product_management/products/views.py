from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')

    products = Product.objects.all()
    if search_query:
        products = products.filter(name__icontains=search_query)
    if status_filter:
        products = products.filter(status=status_filter)

    return render(request, 'products/product_list.html', {'products': products})

def product_form(request, id=None):
    product = get_object_or_404(Product, id=id) if id else None
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'products/product_form.html', {'form': form})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'products/confirm_delete.html', {'product': product})
