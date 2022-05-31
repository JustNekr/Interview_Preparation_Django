from productsapp.models import ProductCategory


def products_categories(request):
    categories = ProductCategory.objects.all()
    return {
        'categories': categories
    }
