import pandas as pd
import numpy as np

# Read Excel file
df = pd.read_excel("C:/Users/shail/Documents/2college management.xlsx")

# Display complete data
print("College Management Data:")
print(df)

# Convert Marks column into NumPy array
marks = np.array(df["Marks"])

print("\nMarks:")
print(marks)

# NumPy operations
print("\nAverage Marks:", np.mean(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))
print("Total Marks:", np.sum(marks))

# Students who scored more than 80
print("\nStudents with marks greater than 80:")
print(df[marks > 80])