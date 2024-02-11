import pandas as pd
from typing import List, Dict, Union

def import_sales_data(file_path: str) -> List[Dict[str, Union[str, int, float]]]:
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')

file_path = "sales_data.xlsx"
sales_data = import_sales_data(file_path)

print("Imported Sales Data:")
for row in sales_data:
    print(row)


def calculate_total_revenue(data: List[Dict[str, Union[str, int, float]]]) -> float:
    return sum(float(row['Revenue']) for row in data)

def calculate_monthly_average(data: List[Dict[str, Union[str, int, float]]]) -> Dict[str, float]:
    
    monthly_totals = {}       # Initialize dictionaries to store monthly totals and counts
    monthly_counts = {}

    # Iterate over each row in the data
    for row in data:
        # Extract the month from the 'Date' field
        # month = row['Date'].split('-')[1]
        # date is in timestamp
        month = str(row['Date'].date()).split('-')[1]     


        # Convert 'Revenue' to a float
        revenue = float(row['Revenue'])

        # Update monthly totals and counts
        if month in monthly_totals:
            monthly_totals[month] += revenue
            monthly_counts[month] += 1
        else:
            monthly_totals[month] = revenue
            monthly_counts[month] = 1

    # Calculate monthly averages
    monthly_averages = {}
    for month in monthly_totals:
        monthly_averages[month] = monthly_totals[month] / monthly_counts[month]

    # Return the resulting dictionary containing monthly averages
    return monthly_averages

def find_highest_selling_product(data: List[Dict[str, Union[str, int, float]]]) -> str:
    product_quantities = {}
    for row in data:
        product = row['Product']
        quantity = int(row['Quantity'])
        product_quantities[product] = product_quantities.get(product, 0) + quantity
    return max(product_quantities, key=product_quantities.get)