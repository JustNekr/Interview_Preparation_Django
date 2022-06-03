from productsapp.models import ProductCategory


def products_categories(request):
    # categories = ProductCategory.objects.all()
    categories = ProductCategory.on_site.all()
    return {
        'categories': categories
    }
