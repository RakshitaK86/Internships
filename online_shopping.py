coustomer_name="Rakshita"
product_name="machine"
product_price=1234.00
quantity=2
gst_percentage=123.00
delivery_charge=234.00
total_price=product_price*quantity
gst_amount=total_price*gst_percentage/100
final_bill_amount=total_price+gst_amount+delivery_charge
print(f"coustomer name: {coustomer_name}")
print(f"product name: {product_name}")
print(f"product price: {product_price} ")
print(f"quantity: {quantity}")
print(f"gst percentage: {gst_percentage}")
print(f"delivery charge: {delivery_charge}")
print(f"total price: {total_price}")
print(f"gst amount: {gst_amount}")
print(f"final bill amount: {final_bill_amount}")
