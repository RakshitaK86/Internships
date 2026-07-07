#Product Color Code Lookup

print("Product Color Code Lookup")

# Dictionary using RGB tuples as keys
paint_stock = {
    (0, 0, 255): "Blue",
    (0, 255, 0): "Green",
    (255, 0, 0): "Red"   
}

# Lookup stock quantity
search_color = (0, 0, 255)
stock_level = paint_stock.get(search_color, 0)

print(f"Stock level for color {search_color}: {stock_level}")