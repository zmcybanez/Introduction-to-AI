import random

target = 25

def fitness(x):
    return abs(target-x)

population = [random.randint(0,50) for _ in range(10)]

for _ in range(20):
    population.sort(key=fitness)
    population = population[:5]
    population += [p + random.randint(-3,3) for p in population]

print("Best solution:", population[0])