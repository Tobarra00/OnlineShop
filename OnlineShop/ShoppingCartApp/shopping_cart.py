class ShoppingCart():
    
    def __init__(self, request) -> None:
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    def add(self, product):
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                'product_id': product.id,
                'name': product.name,
                'price': str(product.price),
                'amount': 1,
                'image': product.image.url
            }
        else:
            self.cart[str(product.id)]['amount'] += 1
            self.cart[str(product.id)]['price'] = str(product.price * self.cart[str(product.id)]['amount'])
        self.save_cart()
        
    def substract(self, product):
        if str(product.id) in self.cart.keys():
            if self.cart[str(product.id)]['amount'] > 0:
                self.cart[str(product.id)]['amount'] -= 1
                self.cart[str(product.id)]['price'] = str(float(self.cart[str(product.id)]['price']) - product.price)
            if self.cart[str(product.id)]['amount'] == 0:
                del self.cart[str(product.id)]
            self.save_cart()
                
    def remove(self, product):
        if str(product.id) in self.cart.keys():
            del self.cart[str(product.id)]
            self.save_cart()
    
    def reset(self):
        self.session['cart'] = {}
        self.session.modified = True
        
    def save_cart(self):
        self.session['cart'] = self.cart
        self.session.modified = True
    
    