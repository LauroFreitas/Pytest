class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        """Atualiza a quantidade em estoque do produto."""
        if quantity >= 0:  # Verifica se a quantidade é não negativa
            self.stock_quantity = quantity
            return (f"A quantidade em estoque do produto '{self.name}' foi atualizada para {quantity} unidades.")
        else:
            return (f"O estoque do produto '{self.name}' está negativo. Verifique o estoque!")

    def validate_stock(self):
        """Verifica se o estoque está adequado (não negativo)."""
        if self.stock_quantity >= 0:
            return (f"O estoque do produto '{self.name}' está adequado.")
        else:
            return (f"O estoque do produto '{self.name}' está negativo. Verifique o estoque!")
   
    def is_on_sale(self, sale_price):
        """Verifica se o produto está em promoção com base no preço fornecido."""
        return self.price < sale_price