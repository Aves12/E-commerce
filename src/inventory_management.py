def process_orders(stock_levels, orders, threshold=10):
    """
    Processes sales orders and updates stock levels.
    If stock levels go below the threshold, a restocking alert is triggered.
    
    :param stock_levels: Dictionary of products with current stock levels.
    :param orders: List of orders, where each order is a dictionary with product_id and quantity.
    :param threshold: Stock level threshold for restocking alerts.
    :return: Updated stock levels.
    """
    for order in orders:
        product_id = order['product_id']
        quantity_ordered = order['quantity']

        if product_id not in stock_levels:
            raise ValueError(f"Product ID {product_id} does not exist in stock.")

        if stock_levels[product_id] < quantity_ordered:
            raise ValueError(f"Not enough stock for product ID {product_id}.")

        # Reduce stock levels
        stock_levels[product_id] -= quantity_ordered

        # Trigger restocking alert if stock goes below threshold
        if stock_levels[product_id] < threshold:
            print(f"Alert: Product ID {product_id} needs restocking. Stock level: {stock_levels[product_id]}")

    return stock_levels


def restock_items(stock_levels, restock_list):
    """
    Restocks items by updating the stock levels based on the restock list.
    
    :param stock_levels: Dictionary of products with current stock levels.
    :param restock_list: List of restock orders, where each item is a dictionary with product_id and quantity.
    :return: Updated stock levels.
    """
    for item in restock_list:
        product_id = item['product_id']
        restock_quantity = item['quantity']

        if product_id not in stock_levels:
            raise ValueError(f"Product ID {product_id} does not exist in stock.")

        stock_levels[product_id] += restock_quantity
        print(f"Product ID {product_id} restocked by {restock_quantity} units.")

    return stock_levels


# Example usage:
if __name__ == "__main__":
    # Sample stock levels
    stock_levels = {
        101: 50,  # Product ID 101 has 50 units in stock
        102: 30,
        103: 5,   # Low stock for Product ID 103
    }

    # Incoming sales orders
    orders = [
        {'product_id': 101, 'quantity': 20},
        {'product_id': 103, 'quantity': 3},
    ]

    # Process orders and update stock levels
    stock_levels = process_orders(stock_levels, orders)

    # Restock items where needed
    restock_list = [
        {'product_id': 103, 'quantity': 50},  # Restocking Product ID 103
    ]
    stock_levels = restock_items(stock_levels, restock_list)
