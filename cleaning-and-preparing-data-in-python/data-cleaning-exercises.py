from csv import reader
with open('cleaning-and-preparing-data-in-python/artworks.csv') as file:
    read_file = reader(file)
    data = list(read_file)
data = data[1:]

num_row = len(data)
print(num_row)