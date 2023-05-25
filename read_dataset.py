import csv

def create_list(dataset):
    genre_list = []
    with open(f"./{dataset}", newline="") as books_file:
        books_dict = csv.DictReader(books_file)
        for row in books_dict:
            genre = row["Genre"]
            if genre.split(',')[0] not in genre_list:
                genre_list.append(genre.split(',')[0])
    return genre_list

# create_list("books_new.csv")

def filter_list(alist, string):
    alist = [item for item in alist if string.lower() in item.lower()]
    return alist


def show(dataset, name):
    print(f"\nEcco i libri di {name}")
    with open(f"./{dataset}", newline="") as books_file:
        books_dict = csv.DictReader(books_file)
        for row in books_dict:
            title = row["Title"]
            author = row["Author"]
            genre = row["Genre"]
            height = row["Height"]
            if name.lower() in row["Genre"].lower():
                print(f"""\nTitle:  {title}
Author:  {author}
Genre:  {genre}
Height:  {height}
""")
                print("*".rjust(len(title), '*'))

# show("books_new.csv", "Rutherford")