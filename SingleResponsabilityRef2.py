class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name:str, quantity:int, price:float) -> None: # Agregar items
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
class PaymentProcesor: # Procesador de pago
    def pay(self, order:Order, security_code:str, payment_type:str):
        # Si el metodo de pago es débito
        if payment_type == "debit":
            print("Processing debit payment type") # Procesar el metodo de pago
            print(f"Verifying security code: {security_code}") # Verificar el codigo de seguridad
            order.status = "paid"
        # Si el metodo de pago es credito
        elif payment_type == "credit":
            print("Processing credit payment type") # Procesar el metodo de pago
            print(f"Verifying security code: {security_code}") # Verificar el codigo de seguridad
            order.status = "paid"
        # Sino
        else:
            raise Exception(f"Unknown payment type: {payment_type}")

class CalculateProcesor: # Calcular el total
    def total_price(self, order = Order):
        total = 0
        for quantity, price in zip(order.quantities, order.prices):
            total += quantity * price
        return total

order = Order()
print(order.status)

# Agreamos item a nuestra orden de compra
order.add_item("Laptop", 1, 150)
order.add_item("SSD", 2, 20)
order.add_item("USB cable", 1, 5)

procesor = PaymentProcesor() # Instancia que procesa los pagos

# Procesamos el pago
procesor.pay(order, "12345", "debit")

# Verificamos el estado de la orden
print(order.status)

total = CalculateProcesor()
print(total.total_price(order))