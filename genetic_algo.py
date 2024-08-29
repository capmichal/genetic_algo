import random
import string
from difflib import SequenceMatcher

TARGET = "poprawne" # target has to have a fixed legth and we have to stick with it, for now we keep it as a string without spaces, all lowercase
TARGET_LEN = len(TARGET)
GENES = string.ascii_lowercase
MUTATION_RATE = 0.2 # how likely is the mutation




# SELECTION STAGE - find out best half of elements from population 
def find_best_from_generation(generation):

    best_half = sorted(generation, key=lambda string: SequenceMatcher(None, string, TARGET).ratio(), reverse=True)[:int(0.5*len(generation))]
    best_one = SequenceMatcher(None, best_half[0], TARGET).ratio()



    if best_one == 1.0:
        return "MAMY WINNERA"
    else:
        print(f"Najlepsze ratio tej generacji to {best_one}")

    return best_half


# initialy forgot about this stage, which resulted in copying parents forever
def mutation(single_offspring_instance):


    # czy dojdzie do mutacji, zalezy od przypadku
    if random.random() < MUTATION_RATE:
        gene_to_mutate = random.randint(0,len(single_offspring_instance)-1)
        gene_to_introduce = random.choices(GENES)[0]
        # python string are immutable, so we cannot modify them in place
        mutated_offspring = single_offspring_instance[:gene_to_mutate] + gene_to_introduce + single_offspring_instance[gene_to_mutate+1:]
        return mutated_offspring
    
    else:
        return single_offspring_instance


# CROSSOVER STAGE - combine genetic traits from two parents, will be using single point crossover, meaning we will choose a random point and combine the genetic material (letters)
def crossover(potential_parents):
    
    desired_generation_size = 2*len(potential_parents)
    new_generation = []
    

    while len(new_generation) < desired_generation_size:
        # dla KAZDEGO z dobych genowo rodziców wykonuje
        for parent in potential_parents:
            potential_parents_excluded = [i for i in potential_parents if i != parent]
            
            if len(new_generation) != desired_generation_size:
                parent1 = parent

                # how many offspring ?
                offspring_number = random.randint(1,3) # 
                
                for i in range(offspring_number):

                    # wybieram LOSOWEGO z pozostałych dobrych genowo rodziców
                    parent2 = random.choices(potential_parents_excluded, k=1)[0]

                    # single point crossover
                    crossover_point = random.randint(1,TARGET_LEN-1)
                    offspring = parent1[:crossover_point] + parent2[crossover_point:]
                    mutated_offspring = mutation(offspring)

                    # trzeba poprawić, dodać break statements żeby było wydajnie, bo teraz nie przerywa gdy już zapełni nową generację                
                    if len(new_generation) != desired_generation_size:
                        new_generation.append(mutated_offspring)



    return new_generation




population = ["".join(random.choices(GENES, k=TARGET_LEN)) for i in range(50)]

# fajni = find_best_from_generation(population)
# print("fajni", fajni)


# nowi_fajni = crossover(fajni)
# print("nowi fajni", nowi_fajni)



for i in range(1000):

    best_genes = find_best_from_generation(population)
    
    if best_genes == "MAMY WINNERA":
        print(best_genes)
        break
    else:
        print(f"najlepsze geny populacji nr. {i} --> {best_genes}")

    new_generation = crossover(best_genes)
    print(f"nowa generacja wywodząca się od populacji nr. {i} --> {new_generation}")
    population = new_generation

print("KONIEC")