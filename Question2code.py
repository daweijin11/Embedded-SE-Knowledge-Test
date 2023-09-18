# declare dataframe
import pandas as pd
df = pd.read_excel("Embedded Software Engineer Quiz Resource.xlsx", sheet_name=0)

# Read first column into list named "Base10" and second column into list named "Base 62"
Base10 = df['Base10'].tolist()
Base61 = df['Base61'].tolist()

# Set missing number 5 to 0. 0 can be set as the missing value as no input value divided by 62 gives a remainder of 0.
# Set L to 21/L. This key value pair was found through trial and error when testing for all numbers 0-61
# Hashmap to store base 62(unique ordering) to base 10 digit conversions
tracker = {"5":0,"L":21}

# Hashmap to store base 62(unique ordering) to base 62 digit conversions
tracker2 = {"5":"0","L":"L"}

# List of all base 62 numbers in order
base62_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Read through all Base 10 and corresponding base62 numbers, perform division of 61^2, 61, 1 to find values of the
# base 62 digits
for i in range(len(Base10)):
      # algorithm to find numeric value of each letter in output
      num = Base10[i]
      a = num // (3844)
      num = num - (a*3844)
      b = num // 62
      num = num - (62*b)
      c = num

      # Store values into hashmaps
      if Base61[i][0] not in tracker.keys() and a!= 0:
            tracker[Base61[i][0]] = a
            tracker2[Base61[i][0]] = base62_chars[a]
      if Base61[i][1] not in tracker.keys() and b!= 0:
            tracker[Base61[i][1]] = b
            tracker2[Base61[i][1]] = base62_chars[b]
      if Base61[i][2] not in tracker.keys() and c!= 0:
            tracker[Base61[i][2]] = c
            tracker2[Base61[i][2]] = base62_chars[c]

# swap keys and values in hashmap to find base 10 and base 62 to base 62(unique ordering) conversions
swap = {v: k for k, v in tracker.items()}
swap2 = {v: k for k, v in tracker2.items()}

#Function to perform input to output
def Input_To_Output(Input):

      #Initialize an empty string to store the base 62 number
      base62 = ""

      # Perform the conversion from base 10(input) to the unique numbering system
      while Input > 0:
            remainder = Input % 62
            base62 = base62_chars[remainder] + base62
            Input //= 62
      Output = ""
      for i in range(len(base62)):
            Output += swap2[base62[i]]
      return Output
