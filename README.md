### What is Genetic Algorithm and how does it work?

Genetic Algorithm is a **5 step** algorithm which simulates the process of evolution to find optimal or near-optimal solutions for complex problems.

##### Steps
1. Initial population
2. Selection
3. Crossover
4. Mutation
5. Evolved population




##### TODO
- find out how to properly set parameters like POPULATION_SIZE, MUTATION_RATE, HOW_MANY_OFFSPRING_PER_PARENT, NUMBER_OF_NEW_GENERATIONS(this should be just a while true loop)
- maybe a SequenceMatcher is not the best algo, ratio() is probably not a good choice, maybe we should look for how many letters are not correct?
- there is NEVER a situation when og_gen is better than the new one, shouldnt it happen from time to time?




takeway:
while using difflib SequenceMatcher, with MUTATION_RATE=0.5, generation_len=50, off_per_parent=(1,3), sometimes even
1000 iterations were not enough
using RATIO to measure how close we are, is really not effective, we should definitely use Levenshtein distance, meaning we should look how many operations we need to perform on a string to achieve desired TARGET