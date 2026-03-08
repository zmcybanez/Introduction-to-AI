import random

population = [random.randint(0,10) for _ in range(6)]

def fitness(x):
    return x*x

for generation in range(5):
    population = sorted(population, key=fitness, reverse=True)
    population = population[:3]

    offspring = [p + random.randint(-1,1) for p in population]
    population += offspring

print(population)