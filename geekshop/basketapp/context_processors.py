def basket(request):
    return {
        'basket': getattr(request.user, 'basket', None)
    }
