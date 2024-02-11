# You are given a CSV file containing information about sales transactions. Each row represents a transaction with columns: Date, Product, Quantity, and Revenue. calculate total revenue, monthly average revenue, highest selling product.

from sales_data_functions import import_sales_data, calculate_total_revenue, calculate_monthly_average, find_highest_selling_product

file_path = "sales_data.xlsx"
sales_data = import_sales_data(file_path)

# Calculating total revenue
total_revenue = calculate_total_revenue(sales_data)
print("Total revenue:",total_revenue)

# Calculating monthly average revenues
monthly_average = calculate_monthly_average(sales_data)
print("Monthly av. revenue:",monthly_average)

# Finding highest selling product
highest_selling_product = find_highest_selling_product(sales_data)
print("Highest Selling Product:",highest_selling_product)
