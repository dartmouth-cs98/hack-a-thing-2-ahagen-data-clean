import pandas as pd
import numpy as np
from urllib.parse import urlparse

# Open our file
with open('hist.txt') as f:
    content = f.readlines()
# Strip whitespace then split on first occurrence of pipe character
raw_data = [line.split('|', 1) for line in [x.strip() for x in content]]
# We now have a 2D list.
#print(raw_data[0][0])


data = pd.DataFrame(raw_data, columns=['datetime', 'url'])

#initalize the copy
data2019 = data.copy()
# loop through the dataframe
for index, row in data.iterrows():
	if "2019" not in row['datetime']:
		# remove row if it does not contain 2019
		data2019 = data2019.drop(index)

#print(data2019)

# convert time stamp to datetime format
data2019.datetime = pd.to_datetime(data2019.datetime)

# initialize for 2019 data with parsed urls
data2019p = data2019.copy()

parser = lambda u: urlparse(u).netloc
data2019p.url = data2019p.url.apply(parser)

# Aggregate domain entries
site_frequencies = data2019p.url.value_counts().to_frame()
# Make the domain a column
site_frequencies.reset_index(level=0, inplace=True)
# Rename columns to appropriate names
site_frequencies.columns = ['domain', 'count']
# Display top 2
#print(site_frequencies.head(20))

subjects = {"tech" : 0, "news": 0}

for index, row in data2019.iterrows():
	#print(row['url'])
	if "tech" in row['url']:
		subjects["tech"] += 1
	if "news." in row['url'] or "cnn" in row['url'] or "nytimes" in row['url'] or "techcrunch" in row['url'] or "vox" in row['url'] or "vice" in row['url'] or "verge" in row['url']:
		#print(row['url'])
		subjects["news"] +=1
# show frequency of urls within the subjects tech and news
print(subjects)

