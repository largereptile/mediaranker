import random
import sys

# imagine the film is in a list where first is most preferred and last is least preferred
def insert_film(film_list, film_title):
    # If the list doesnt exist, we can create a list of just the film by itself
    if not film_list:
        return [film_title]
    
    # Initialise both low and high values
    low, high = 0, len(film_list) - 1

    while low <= high:
        mid = (low + high) // 2
        res = compare_films(film_title, film_list[mid])

        # New film is better
        if res == 1:
            high = mid - 1
        # Other film is better
        elif res == 2:
            low = mid + 1
        # Films are qual
        else:
            film_list[mid] = f"{film_list[mid]}, {film_title}"
            return film_list
        
    return film_list[:low] + [film_title] + film_list[low:]


def compare_films(f1, f2):
    print(f"Prefer:\n1. {f1}\n2. {f2}\n3. Equal")
    res = int(input())
    return res

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python media-sorter.py <username>")
        sys.exit(1)

    target_user = sys.argv[1]

    films_filename = f"{target_user}_films.txt"
    sorted_films_filename = f"sorted_{target_user}_films.txt"

    films = open(films_filename, "r", encoding="utf8").readlines()
    films = [film.split(" - ")[0] for film in films]
    random.shuffle(films)

    try:
        sorted_films = [x.strip("\n") for x in open(sorted_films_filename, "r", encoding="utf8")]
    except FileNotFoundError:
        # In case new account sorting, we initialise
        sorted_films = []
    
    for film in films:
      dupe = False
      for f2 in sorted_films:
          if film in f2:
              dupe = True
              break
      if dupe or not film:
          continue
      sorted_films = insert_film(sorted_films, film
      with open(sorted_films_filename, "w", encoding="utf8") as f:
          for film1 in sorted_films:
              f.write(f"{film1}\n")