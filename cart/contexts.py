def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context
