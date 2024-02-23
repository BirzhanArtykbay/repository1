from datetime import datetime

# Define the two dates
date1 = '2024-02-23 12:00:00'
date2 = '2024-02-23 13:30:45'

# Convert date strings to datetime objects
datetime1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
datetime2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

# Calculate the difference in seconds
difference_seconds = (datetime2 - datetime1).total_seconds()

print("Difference in seconds:", difference_seconds)

