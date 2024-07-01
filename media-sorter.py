import random
# imagine the film is in a list where first is most preferred and last is least preferred
def insert_film(film_list, film_title):
    if len(film_list) == 2:
        res = compare_films(film_title, film_list[1])
        if res == 2:
            return film_list + [film_title]
        elif res == 3:
            return [film_list[0], f"{film_list[1]}, {film_title}"]
        else:
            return insert_film(film_list[:1], film_title) + [film_list[1]]
    elif len(film_list) == 1:
        res = compare_films(film_title, film_list[0])
        if res == 1:
            return [film_title, film_list[0]]
        elif res == 3:
            return [f"{film_title}, {film_list[0]}"]
        else:
            return [film_list[0], film_title]
    elif len(film_list) == 0:
        return [film_title]

    midpoint = round(len(film_list)/2) - 1
    first_half = film_list[:midpoint]
    second_half = film_list[midpoint + 1:]
    res = compare_films(film_title, film_list[midpoint])
    if res == 1:
        return insert_film(first_half, film_title) + [film_list[midpoint]] + second_half
    elif res == 3:
        return first_half + [f"{film_list[midpoint]}, {film_title}"] + second_half
    else:
        return first_half + [film_list[midpoint]] + insert_film(second_half, film_title)


def compare_films(f1, f2):
    print(f"Prefer:\n1. {f1}\n2. {f2}\n3. Equal")
    res = int(input())
    return res

films = open("largereptile_films.txt", "r", encoding="utf8").readlines()
films = [film.split(" - ")[0] for film in films]
random.shuffle(films)

sorted_films = [x.strip("\n") for x in open("sorted_largereptile_films.txt", "r", encoding="utf8")]
# sorted_films = []
for film in films:
    if film in sorted_films:
        continue
    sorted_films = insert_film(sorted_films, film)

    with open("sorted_largereptile_films.txt", "w", encoding="utf8") as f:
        for film1 in sorted_films:
            f.write(f"{film1}\n")