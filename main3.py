import random

media = open("manga.txt", "r").read().splitlines()

random.shuffle(media)

sorted_media = []

def insert_media(media_list, m):
    print(media_list)
    start_i = 0
    end_i = len(media_list) - 1
    if not media_list:
        media_list.append(m)
        return media_list
    middle = end_i - (round(end_i - start_i / 2))
    print(f"1: {media_list[middle]} vs 2: {m}")
    f = int(input())
    if f == 1:
        first_half = media_list[start_i:middle + 1]
        second_half = insert_media(media_list[middle + 1:end_i + 1], m)
        return first_half + second_half
    if f == 2:
        first_half = insert_media(media_list[start_i:middle + 1], m)
        second_half = media_list[middle:end_i + 1]
        return first_half + second_half


for m in media:
    sorted_media = insert_media(sorted_media, m)

