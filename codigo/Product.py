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
    
    def get_total_value(self):
        """Retorna o valor total do estoque (preço unitário x quantidade)."""
        total_value = self.price * self.stock_quantity
        return total_value

    def apply_discount(self, discount_percentage):
        """Aplica um desconto percentual ao preço do produto."""
        if 0 <= discount_percentage <= 100:
            self.price = self.price * (1 - discount_percentage / 100)
            return f"Desconto de {discount_percentage}% aplicado ao produto '{self.name}'. Novo preço: R${self.price:.2f}"
        else:
            return "O desconto deve estar entre 0% e 100%. Nenhum desconto aplicado."