import random
import collections
import math
media = open("../manga.txt", "r").read().splitlines()

n = len(media)
n_matchups = n * math.log(n)
print(n_matchups)

pairs = [(x, y) for x in media for y in media if x != y]

final_matches = []
for m in media:
    p = list(filter(lambda x: x[0] == m, pairs))
    random.shuffle(p)
    final_matches += [match for match in p if match not in final_matches and (match[1], match[0]) not in final_matches][:n_matchups]

random.shuffle(final_matches)
scores = collections.defaultdict(list)

for match in final_matches:
    print(f"Which do you prefer?\n1: {match[0]}, 2: {match[1]}")
    score = int(input())
    if score == 1:
        scores[match[0]].append(1)
        scores[match[1]].append(0)
    if score == 2:
        scores[match[0]].append(0)
        scores[match[1]].append(1)

final_scores = collections.defaultdict(float)

win_rates = collections.defaultdict(float)

for media, totals in scores.items():
    if media not in win_rates.keys():
        win_rates[media] = len([i for i in totals if i == 1]) / len(totals)
    enemy_wr = []
    for enemy in scores:
        if enemy != media:
            if enemy in win_rates.keys():
                enemy_wr.append(win_rates[enemy])
            else:
                win_rates[enemy] = len([i for i in scores[enemy] if i == 1]) / len(scores[enemy])
                enemy_wr.append(win_rates[enemy])
    enemy_wr = sum(enemy_wr) / len(enemy_wr)
    final_scores[media] = win_rates[media] * (1/enemy_wr)

final_scores = list(sorted([(k, v) for k, v in final_scores.items()], key=lambda x: x[1], reverse=True))

for i, (name, score) in enumerate(final_scores):
    print(f"{i}: {name} - {score}")