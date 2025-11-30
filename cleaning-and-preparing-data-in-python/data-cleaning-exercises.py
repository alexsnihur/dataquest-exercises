from csv import reader
open_csv = open('cleaning-and-preparing-data-in-python/artworks.csv')
csv = reader(open_csv)
data_titles = list(csv)
data = data_titles[1:]

num_row = len(data)
print(num_row)