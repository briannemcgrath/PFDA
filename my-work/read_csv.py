import csv

with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header
    next(csv_reader)
    
    # Use list comprehension to extract and sum the ages in one step
    ages = [int(row[1]) for row in csv_reader]
    
    # Calculate the average age if we have data
    average_age = sum(ages) / len(ages) if ages else 0
    
    print(f"Average Age: {average_age:.2f}")

