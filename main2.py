total_fights = 0

class Fighter:
    def __init__(self, media):
        self.media = media

    def __lt__(self, other):
        return fight(self, other)

    def __repr__(self):
        return self.media


def fight(fighter1, fighter2):
    print(f"1: {fighter1} vs 2: {fighter2}")
    f = int(input())
    global total_fights
    total_fights += 1
    if f == 1:
        return True
    if f == 2:
        return False


media = open("manga.txt", "r").read().splitlines()

fighters = [Fighter(m) for m in media]

fighters.sort()

for i, (name, score) in enumerate(final_scores):
    print(f"{i}: {name} - {score}")