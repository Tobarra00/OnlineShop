def total_price(request):
    total = 0
    if request.user.is_authenticated:
        for value in request.session['cart'].values():
            total += float(value['price']) 
    
    return {'total_price': total}
   