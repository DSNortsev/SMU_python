# Import csv and math libraries
import csv
import math

def read_csv_file(file_name):
  """
     Read stock csv file.
     Return a list of rows.
   """
  # Open csv file
  print('Welcome to Program 3')
  print('Opening File...')
  stock_file = open(file_name)
  # Read as csv file and add all rows to the list
  data = list(csv.reader(stock_file, delimiter=','))
  # Close open file
  stock_file.close()
  return data

def select_metric():
  """
     Ask user to select an option to calcuate metric.
     Return user input as a string
  """
  print('What metric do you want to analyze?')
  print(' C) Close price')
  print(' V) Volume')
  print(' R) Range')
  return input('Choice: ')

def calculate_std(data):
  """Calculate Standard deviation"""
  n = len(data)
  mean = sum(data) / n
  return math.sqrt(sum((x - mean) ** 2 for x in data) / n)

def calculate_metric(data, option):
  """
    Calculate all metric.
    Return a tuple: (observations, mean, vol, max, max_day, min, min_day)
  """
  # Set header to False as default value
  header = False
  # Initialize vatiables
  total_sum = count = 0 
  # List of retrieve values based on selected option
  all_values = []
  # Min valu is infinity 
  min_value = float('inf')
  min_day = ''
  # Max value is negative infinity
  max_value = float('-inf')
  max_day = ''

  for row in data:
    # Skip header 
    if not header: 
      header = True
      continue
 
    # Select column based on selected option 
    if option == 'C':
      # Select Close column
      value = float(row[4])
    elif option == 'V':
      # Select Volume colum
      value = float(row[6])
    else:
      # Calculte range. Range = High - Low
      value = float(row[2]) - float(row[3])
    
    # Increase total sum
    total_sum += value
    # Add value to total list 
    all_values.append(value)

    # Find min value and day
    if min_value > value:
      min_value = value
      min_day = row[0]
  
    # Find max value and day
    if max_value < value:
      max_value = value
      max_day = row[0]
    
    # Increase count by 1 
    count += 1

  # Calculate mean value
  mean_value = total_sum / count
  # Calculate the standard deviation
  std = calculate_std(all_values)

  return count,mean_value, std, max_value, max_day, min_value, min_day

def main():
  # Set selected option to False as default value
  selected_option = False
  # Read csv file 
  stock_data = read_csv_file('TSLA.csv')

  while selected_option not in ('C', 'V', 'R'):
    # Print an error only when invalid option is entered
    if selected_option:
      print('\nInvalid option. Please try again!\n')
    # Ask user to choose an option to calculate metric
    selected_option = select_metric()

  # Calculate metric
  metric = calculate_metric(stock_data, selected_option)
  # Print calcuated metric

  print('\nTotal observations:', metric[0])
  print('Mean:              ', metric[1])
  print('Vol:               ', metric[2])
  print('Max:               ', metric[3])
  print('Max Day:           ', metric[4])
  print('Min:               ', metric[5])
  print('Min Day:           ', metric[6]) 
  print('\nGoodbye!')

if __name__ == '__main__':
  main()
