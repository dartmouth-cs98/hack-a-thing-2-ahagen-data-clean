import pandas as pd
import numpy as np

# Open our file
with open('hist.txt') as f:
    content = f.readlines()
# Strip whitespace then split on first occurrence of pipe character
raw_data = [line.split('|', 1) for line in [x.strip() for x in content]]
# We now have a 2D list.
#print(raw_data[0][0])


data = pd.DataFrame(raw_data, columns=['datetime', 'url'])

#initalize the copy
data2019 = data
# loop through the dataframe
for index, row in data.iterrows():
	if "2019" not in row['datetime']:
		# remove row if it does not contain 2019
		data2019 = data2019.drop(index)

print(data2019)

# convert time stamp to datetime format
data2019.datetime = pd.to_datetime(data2019.datetime)
print(data2019.datetime[0])