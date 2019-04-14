import random

NUM_LOOP = 100000
NUM_ATTENDEE = 100
NUM_PRIZE = 10
ME = 0

prize_count = [0] * NUM_PRIZE
no_prize = 0

for i in range(NUM_LOOP):
    hit = 0
    for prize in range(NUM_PRIZE)[::-1]:
        winner = random.randrange(NUM_ATTENDEE)
        if winner == ME:
            hit = 1
            prize_count[prize] = prize_count[prize] + 1
            break
    if hit == 0:
        no_prize = no_prize + 1

for number in range(NUM_PRIZE):
    print("Prize {} : {}".format(number + 1, prize_count[number]))

print("No prize: {}".format(no_prize))
