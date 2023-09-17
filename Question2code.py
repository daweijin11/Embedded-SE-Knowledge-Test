import pandas as pd
df = pd.read_excel("Embedded Software Engineer Quiz Resource.xlsx", sheet_name=0)

# Read first column into list named "Base10" and second column into list named "Base 62"

Base10 = df['Base10'].tolist()
Base61 = df['Base61'].tolist()

# Set missing number 5 to 0. 0 can be set as the corresponding value as noBase 10 value is cleanly divided by 62.

tracker = {"5":0}

# Read through all Base 10 and corresponding base62 numbers, perform division of 61^2, 61, 1 to find values of the
# base 62 digits

for i in range(len(Base10)):
      num = Base10[i]
      a = num // (3844)
      num = num - (a*3844)
      b = num // 62
      num = num - (62*b)
      c = num
      if Base61[i][0] not in tracker.keys() and a!= 0:
            tracker[Base61[i][0]] = a
      if Base61[i][1] not in tracker.keys() and b!= 0:
            tracker[Base61[i][1]] = b
      if Base61[i][2] not in tracker.keys() and c!= 0:
            tracker[Base61[i][2]] = c
swap = {v: k for k, v in tracker.items()}

def Convert_ToBase62(num):
      answer = ""
      answer += swap[num//3844]
      num -= (num//3844) * 3844
      answer += swap[num//62]
      num -= (num//62) * 62
      answer += swap[num]
      return answer
print(Convert_ToBase62(16465))
