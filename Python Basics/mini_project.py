
# ============================================================
# MINI PROJECT: RETAIL SALES ANALYSIS SYSTEM
# Domain: Data Analytics
# Level: Beginner to Intermediate
# Libraries: None
# ============================================================

# BUSINESS SCENARIO:
# A retail company wants to analyse sales, profit, customers,
# product performance, regional performance and inventory.
#
# Python concepts used:
# Variables, data types, strings, conditions, operators,
# loops, lists, tuples, sets, dictionaries, functions,
# lambda functions, comprehensions, exception handling,
# sorting and built-in functions.
# ============================================================


# ------------------------------------------------------------
# 1. PROJECT CONFIGURATION
# ------------------------------------------------------------

company_name = "Smart Retail Store"
report_year = 2026

# A discount is available on orders of Rs. 2,000 or more.
discount_threshold = 2000
discount_rate = 10

# Inventory below this level requires restocking.
restock_threshold = 10

print("=" * 65)
print(company_name.upper())
print("RETAIL SALES ANALYSIS REPORT")
print("Report Year:", report_year)
print("=" * 65)


# ------------------------------------------------------------
# 2. SAMPLE DATA
# ------------------------------------------------------------

# Each dictionary represents one sales transaction.
# cost_price and selling_price are per-unit prices.
# quantity indicates the number of units sold.

orders = [
    {
        "order_id": "O101",
        "customer": "  riya sharma ",
        "product": "Laptop",
        "category": "Electronics",
        "region": "West",
        "quantity": 1,
        "selling_price": 60000,
        "cost_price": 48000
    },
    {
        "order_id": "O102",
        "customer": "aarav mehta",
        "product": "Mouse",
        "category": "Accessories",
        "region": "West",
        "quantity": 3,
        "selling_price": 800,
        "cost_price": 500
    },
    {
        "order_id": "O103",
        "customer": "Riya Sharma",
        "product": "Keyboard",
        "category": "Accessories",
        "region": "North",
        "quantity": 2,
        "selling_price": 1500,
        "cost_price": 900
    },
    {
        "order_id": "O104",
        "customer": "kabir singh",
        "product": "Monitor",
        "category": "Electronics",
        "region": "South",
        "quantity": 2,
        "selling_price": 12000,
        "cost_price": 9000
    },
    {
        "order_id": "O105",
        "customer": "meera patel",
        "product": "Mouse",
        "category": "Accessories",
        "region": "West",
        "quantity": 5,
        "selling_price": 800,
        "cost_price": 500
    },
    {
        "order_id": "O106",
        "customer": "AARAV MEHTA",
        "product": "Laptop",
        "category": "Electronics",
        "region": "North",
        "quantity": 1,
        "selling_price": 60000,
        "cost_price": 48000
    },
    {
        "order_id": "O107",
        "customer": "sana khan",
        "product": "Keyboard",
        "category": "Accessories",
        "region": "East",
        "quantity": 4,
        "selling_price": 1500,
        "cost_price": 900
    },
    {
        "order_id": "O108",
        "customer": "kabir singh",
        "product": "Monitor",
        "category": "Electronics",
        "region": "North",
        "quantity": 1,
        "selling_price": 12000,
        "cost_price": 9000
    }
]

# Inventory is a dictionary:
# key = product name, value = units remaining.
inventory = {
    "Laptop": 8,
    "Mouse": 25,
    "Keyboard": 7,
    "Monitor": 12
}

# Tuple: fixed reporting periods.
report_months = ("January", "February", "March")

print("\nTotal order records:", len(orders))
print("Inventory products:", len(inventory))


# ------------------------------------------------------------
# 3. DATA CLEANING
# ------------------------------------------------------------

# Clean customer names by removing extra spaces
# and standardising capitalisation.

for order in orders:
    order["customer"] = order["customer"].strip().title()
    order["product"] = order["product"].strip().title()
    order["category"] = order["category"].strip().title()
    order["region"] = order["region"].strip().title()

print("\n1. DATA CLEANING COMPLETED")
print("Customer names, product names and categories standardised.")


# ------------------------------------------------------------
# 4. VALIDATE THE DATA
# ------------------------------------------------------------

valid_orders = []
invalid_orders = []

for order in orders:

    # Check whether required fields exist and have valid values.
    required_fields = [
        "order_id", "customer", "product", "category",
        "region", "quantity", "selling_price", "cost_price"
    ]

    fields_present = all(field in order for field in required_fields)

    if not fields_present:
        invalid_orders.append(order)
        continue

    # Check numerical values.
    valid_numbers = (
        type(order["quantity"]) is int
        and type(order["selling_price"]) in (int, float)
        and type(order["cost_price"]) in (int, float)
        and order["quantity"] > 0
        and order["selling_price"] >= 0
        and order["cost_price"] >= 0
    )

    # Check text fields.
    valid_text = all([
        order["order_id"] != "",
        order["customer"] != "",
        order["product"] != "",
        order["category"] != "",
        order["region"] != ""
    ])

    if valid_numbers and valid_text:
        valid_orders.append(order)
    else:
        invalid_orders.append(order)

print("\n2. DATA VALIDATION")
print("Valid orders:", len(valid_orders))
print("Invalid orders:", len(invalid_orders))


# ------------------------------------------------------------
# 5. CALCULATE REVENUE, DISCOUNT AND PROFIT
# ------------------------------------------------------------

# Revenue = selling price * quantity
# Cost = cost price * quantity
# Gross profit = revenue - cost
#
# Discount is calculated on revenue when the order qualifies.
# Net revenue = revenue - discount
# Net profit = net revenue - cost

for order in valid_orders:

    order["revenue"] = (
        order["selling_price"] * order["quantity"]
    )

    order["total_cost"] = (
        order["cost_price"] * order["quantity"]
    )

    order["gross_profit"] = (
        order["revenue"] - order["total_cost"]
    )

    if order["revenue"] >= discount_threshold:
        order["discount"] = (
            order["revenue"] * discount_rate / 100
        )
    else:
        order["discount"] = 0

    order["net_revenue"] = (
        order["revenue"] - order["discount"]
    )

    order["net_profit"] = (
        order["net_revenue"] - order["total_cost"]
    )

    if order["net_profit"] > 0:
        order["profit_status"] = "Profitable"
    elif order["net_profit"] == 0:
        order["profit_status"] = "Break-even"
    else:
        order["profit_status"] = "Loss"


# ------------------------------------------------------------
# 6. SUMMARY STATISTICS
# ------------------------------------------------------------

revenues = [order["net_revenue"] for order in valid_orders]
costs = [order["total_cost"] for order in valid_orders]
profits = [order["net_profit"] for order in valid_orders]
discounts = [order["discount"] for order in valid_orders]
quantities = [order["quantity"] for order in valid_orders]

total_revenue = sum(revenues)
total_cost = sum(costs)
total_profit = sum(profits)
total_discount = sum(discounts)
total_units_sold = sum(quantities)
total_orders = len(valid_orders)

if total_orders > 0:
    average_order_value = total_revenue / total_orders
else:
    average_order_value = 0

if total_revenue > 0:
    profit_margin = total_profit / total_revenue * 100
else:
    profit_margin = 0

print("\n3. OVERALL BUSINESS SUMMARY")
print("-" * 45)
print(f"Total Orders       : {total_orders}")
print(f"Total Units Sold   : {total_units_sold}")
print(f"Net Revenue        : Rs. {total_revenue:,.2f}")
print(f"Total Cost         : Rs. {total_cost:,.2f}")
print(f"Total Discounts    : Rs. {total_discount:,.2f}")
print(f"Total Net Profit   : Rs. {total_profit:,.2f}")
print(f"Average Order Value: Rs. {average_order_value:,.2f}")
print(f"Profit Margin      : {profit_margin:.2f}%")


# ------------------------------------------------------------
# 7. PRODUCT-WISE ANALYSIS
# ------------------------------------------------------------

# Dictionaries aggregate revenue, units and profit per product.

product_revenue = {}
product_units = {}
product_profit = {}

for order in valid_orders:

    product = order["product"]

    if product not in product_revenue:
        product_revenue[product] = 0
        product_units[product] = 0
        product_profit[product] = 0

    product_revenue[product] += order["net_revenue"]
    product_units[product] += order["quantity"]
    product_profit[product] += order["net_profit"]

print("\n4. PRODUCT-WISE PERFORMANCE")
print("-" * 65)
print(f"{'Product':<15}{'Units':>8}{'Revenue':>18}{'Profit':>18}")

for product in sorted(product_revenue):
    print(
        f"{product:<15}"
        f"{product_units[product]:>8}"
        f"{product_revenue[product]:>18,.2f}"
        f"{product_profit[product]:>18,.2f}"
    )

# Rank products by revenue using lambda.
ranked_products = sorted(
    product_revenue.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nProducts Ranked by Revenue:")

for rank, (product, revenue) in enumerate(ranked_products, start=1):
    print(f"{rank}. {product}: Rs. {revenue:,.2f}")

# Tuple unpacking retrieves the highest-revenue product.
if ranked_products:
    best_product, best_product_revenue = ranked_products[0]

    print(
        "\nTop Revenue Product:",
        best_product,
        "| Revenue: Rs.",
        f"{best_product_revenue:,.2f}"
    )


# ------------------------------------------------------------
# 8. REGION-WISE ANALYSIS
# ------------------------------------------------------------

region_revenue = {}
region_profit = {}
region_orders = {}

for order in valid_orders:

    region = order["region"]

    if region not in region_revenue:
        region_revenue[region] = 0
        region_profit[region] = 0
        region_orders[region] = 0

    region_revenue[region] += order["net_revenue"]
    region_profit[region] += order["net_profit"]
    region_orders[region] += 1

print("\n5. REGION-WISE PERFORMANCE")
print("-" * 55)

for region, revenue in sorted(
    region_revenue.items(),
    key=lambda item: item[1],
    reverse=True
):
    print(
        f"{region:<12} "
        f"Orders: {region_orders[region]:<4} "
        f"Revenue: Rs. {revenue:,.2f} "
        f"Profit: Rs. {region_profit[region]:,.2f}"
    )

best_region = max(region_revenue, key=region_revenue.get)

print("\nBest Performing Region:", best_region)


# ------------------------------------------------------------
# 9. CUSTOMER ANALYSIS
# ------------------------------------------------------------

# A set tracks unique customers.
unique_customers = set()

# A dictionary tracks each customer's total net revenue.
customer_spending = {}

for order in valid_orders:

    customer = order["customer"]

    unique_customers.add(customer)

    if customer not in customer_spending:
        customer_spending[customer] = 0

    customer_spending[customer] += order["net_revenue"]

print("\n6. CUSTOMER ANALYSIS")
print("-" * 45)
print("Unique Customers:", len(unique_customers))

for customer, spending in sorted(
    customer_spending.items(),
    key=lambda item: item[1],
    reverse=True
):
    print(f"{customer:<20} Rs. {spending:,.2f}")

top_customer = max(customer_spending, key=customer_spending.get)

print("\nHighest Spending Customer:", top_customer)
print(
    "Total Spending: Rs.",
    f"{customer_spending[top_customer]:,.2f}"
)


# ------------------------------------------------------------
# 10. INVENTORY AND RESTOCKING
# ------------------------------------------------------------

print("\n7. INVENTORY STATUS")
print("-" * 45)

for product, stock in inventory.items():

    if stock < restock_threshold:
        status = "RESTOCK REQUIRED"
    else:
        status = "Stock Available"

    print(f"{product:<15} Stock: {stock:<5} {status}")

# List comprehension selects products that need restocking.
restock_products = [
    product
    for product, stock in inventory.items()
    if stock < restock_threshold
]

print("\nProducts Requiring Restocking:", restock_products)


# ------------------------------------------------------------
# 11. ORDER-LEVEL REPORT
# ------------------------------------------------------------

print("\n8. ORDER-LEVEL REPORT")
print("-" * 80)

print(
    f"{'Order':<10}"
    f"{'Customer':<20}"
    f"{'Product':<15}"
    f"{'Revenue':>15}"
    f"{'Net Profit':>15}"
)

for order in valid_orders:
    print(
        f"{order['order_id']:<10}"
        f"{order['customer']:<20}"
        f"{order['product']:<15}"
        f"{order['net_revenue']:>15,.2f}"
        f"{order['net_profit']:>15,.2f}"
    )


# ------------------------------------------------------------
# 12. BUSINESS INSIGHTS USING CONDITIONS
# ------------------------------------------------------------

print("\n9. BUSINESS INSIGHTS")
print("-" * 45)

if profit_margin >= 30:
    print("Profit margin is strong.")
elif profit_margin >= 15:
    print("Profit margin is moderate.")
else:
    print("Profit margin needs improvement.")

high_value_orders = [
    order for order in valid_orders
    if order["net_revenue"] >= discount_threshold
]

profitable_orders = [
    order for order in valid_orders
    if order["net_profit"] > 0
]

print("High-Value Orders:", len(high_value_orders))
print("Profitable Orders:", len(profitable_orders))

if len(high_value_orders) > 0:
    print("High-value orders are contributing to revenue.")
else:
    print("Review strategies for increasing order values.")

if len(restock_products) > 0:
    print("Inventory action: reorder products listed above.")
else:
    print("Inventory action: no immediate restocking needed.")


# ------------------------------------------------------------
# 13. REUSABLE FUNCTION
# ------------------------------------------------------------

def calculate_average(values):

    # Exception handling prevents invalid data from breaking
    # this function if an incorrect input is passed.
    try:
        if len(values) == 0:
            return 0

        return sum(values) / len(values)

    except (TypeError, ZeroDivisionError):
        return 0


average_profit = calculate_average(profits)

print("\n10. FUNCTION DEMONSTRATION")
print(f"Average Net Profit per Order: Rs. {average_profit:,.2f}")


# ------------------------------------------------------------
# 14. BUILT-IN FUNCTION DEMONSTRATION
# ------------------------------------------------------------

print("\n11. DATA QUALITY CHECKS")
print("-" * 45)

all_orders_positive = all(
    order["quantity"] > 0 for order in valid_orders
)

any_order_has_discount = any(
    order["discount"] > 0 for order in valid_orders
)

print("All orders have positive quantities:", all_orders_positive)
print("Any order received a discount:", any_order_has_discount)

# Demonstrate zip() by matching products with inventory.
product_names = list(inventory.keys())
stock_values = list(inventory.values())

print("\nProduct and Stock Pairs:")

for product, stock in zip(product_names, stock_values):
    print(product, "->", stock)


# ------------------------------------------------------------
# 15. FINAL REPORT
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("FINAL REPORT")
print("=" * 65)

print(f"Company             : {company_name}")
print(f"Reporting Year      : {report_year}")
print(f"Valid Transactions   : {len(valid_orders)}")
print(f"Unique Customers     : {len(unique_customers)}")
print(f"Net Revenue          : Rs. {total_revenue:,.2f}")
print(f"Net Profit           : Rs. {total_profit:,.2f}")
print(f"Profit Margin        : {profit_margin:.2f}%")
print(f"Best Product         : {best_product}")
print(f"Best Region          : {best_region}")
print(f"Restock Requirements : {len(restock_products)}")

print("=" * 65)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 65)


# ============================================================
# END OF PROJECT
# ============================================================
