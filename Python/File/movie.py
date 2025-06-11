movies = []
for i in range(3):
    movie = input(f"Enter favorite movie {i+1}: ")
    movies.append(movie)

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(movie + "\n")

with open("movies.txt", "r") as file:
    for line in file:
        print(line.strip().upper())
