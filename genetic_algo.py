import random
import string
from difflib import SequenceMatcher

TARGET = "poprawne" # target has to have a fixed legth and we have to stick with it, for now we keep it as a string without spaces, all lowercase
TARGET_LEN = len(TARGET)
GENES = string.ascii_lowercase





# SELECTION STAGE - find out best half of elements from population 
def find_best_from_generation(generation):

    best_half = sorted(generation, key=lambda string: SequenceMatcher(None, string, TARGET).ratio(), reverse=True)[:int(0.5*len(generation))]
    return best_half


# CROSSOVER STAGE - combine genetic traits from two parents, will be using single point crossover, meaning we will choose a random point and combine the genetic material (letters)
def crossover(potential_parents):
    
    desired_generation_size = 2*len(potential_parents)
    new_generation = []
    
    for parent in potential_parents:
        potential_parents_excluded = [i for i in potential_parents if i != parent]
        
        if len(new_generation) != desired_generation_size:
            parent1 = parent
            #print(f"parent1 to {parent1}")

            # how many offspring ?
            offspring_number = random.randint(1,3) # THIS HAS TO MAKE SURE THE NUMBER WONT EXCEED THE SIZE OF GENERATION
            
            for i in range(offspring_number):
                parent2 = random.choices(potential_parents_excluded, k=1)[0]
                #print(f"parent2 to {parent2}")
                crossover_point = random.randint(1,TARGET_LEN-1)

                offspring = parent1[:crossover_point] + parent2[crossover_point:]
                
                if len(new_generation) != desired_generation_size:
                    new_generation.append(offspring)



    return new_generation



population = ["".join(random.choices(GENES, k=TARGET_LEN)) for i in range(10)]

fajni = find_best_from_generation(population)
print("fajni", fajni)


nowi_fajni = crossover(fajni)
print("nowi fajni", nowi_fajni)