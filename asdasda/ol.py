from cla import Pet
import time
panda = Pet('Panda', 0.0, 'Snail')
fishy = Pet('Fishy', 0.0, 'Fish')

pets = [panda, fishy]

for i in pets:
    while True:
        i.Age += 0.1
        print(i.Age)
        if i.Age >= 2.0:
            print("Your pet died :(")
            i.Status = 'Dead'
            break
        else:
            time.sleep(1)
    time.sleep(2)
