import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


random_seed = 26
np.random.seed(random_seed)
random.seed(random_seed)
mutation_rate = 0.05

def er_w(w, x, y):
    #reused from task 1
    f = x.dot(w)
    result = np.mean((f - y) ** 2)
    return result

def fitness(w,x, y):
    return np.exp(-er_w(w, x, y))

def mutate(chrom):
    #print(chrom)
    chrom_copy = chrom.copy()
    for i in range(len(chrom_copy)):
        if random.random() < mutation_rate:
            chrom_copy[i] = -chrom_copy[i] 
    #print("mutated:", chrom_copy)
    return chrom_copy

def genetic_algorithm(x, y, population_size = 10, max_iter = 80):
    w = np.random.choice([-1, 1], size=(population_size, 6))
    errors = []
    best_w = None
    best_er = float("inf")

    for current_iter in range(max_iter):
        curr_errors = np.array([er_w(chrom, x, y) for chrom in w])
        curr_best_idx = np.argmin(curr_errors)
        curr_best_er = curr_errors[curr_best_idx]

        if curr_best_er < best_er:
            best_er = curr_best_er
            best_w = w[curr_best_idx].copy()

        errors.append(best_er)  

        fitness_scores = np.array([fitness(chrom, x, y) for chrom in w])
        probabilities = fitness_scores / np.sum(fitness_scores)
        new_population = []
        while len(new_population) < population_size:
            parents = np.random.choice(population_size, size=2, p=probabilities)
            parent1, parent2 = w[parents[0]], w[parents[1]]
            middle = 3
            child1 = np.concatenate((parent1[:middle], parent2[middle:]))
            child2 = np.concatenate((parent2[:middle], parent1[middle:]))
            #print("children before mutation:", child1, child2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            #print("children after mutation:", child1, child2)
            new_population.append(child1)
            new_population.append(child2)
        w = np.array(new_population)[:population_size]
    return best_w, best_er, errors


df = pd.read_csv("CreditCard.csv")
#CreditApprove column done
df["Gender"] = df["Gender"].map({"M": 1, "F": 0})
df["CarOwner"] = df["CarOwner"].map({"Y": 1, "N": 0})
df["PropertyOwner"] = df["PropertyOwner"].map({"Y": 1, "N": 0})


x = df[["Gender", "CarOwner", "PropertyOwner", "#Children", "WorkPhone", "Email_ID"]]
y = df["CreditApprove"]
x= x.to_numpy()
y = y.to_numpy()

w, er, errors = genetic_algorithm(x, y)
print("Best w:", w.tolist())
print("Error:", er)

plt.plot(range(1,len(errors)+1), errors)
plt.xlabel("Iteration")
plt.ylabel("er(w)")
plt.title("Genetic Algorithm (with GLOBAL best)")
plt.savefig("Figure3_GeneticAlgorithm.png") 
plt.show()