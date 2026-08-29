"""
For Slicing
"""
movies = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

print(f"First 3 movies are = {movies[:4]}")
print(f"Last 3 movies are = {movies[-3:]}")
print(f"Middle section is = {movies[5:7]}")
print(f"Every second movie = {movies[0:-1:2]}")
print(f"Reverse order = {movies[-1::-1]}")