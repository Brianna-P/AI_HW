import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import random


random_seed = 42
np.random.seed(random_seed)
random.seed(random_seed)

def er_w(w, x, y):
    f = x.dot(w)
    result = np.mean((f - y) ** 2)
    return result

def get_all_neighbors(w):
    neighbors = []
    for i in range(len(w)):
        w_copy = w.copy()
        w_copy[i] *= -1
        neighbors.append(w_copy)
    return neighbors

def hill_climb_algo(x, y, max_iter=100):
    #step 1
    w = np.array([random.choice([-1, 1]) for _ in range(6)])
    er = er_w(w, x, y)
    errors = [er]

    #step 2
    for _ in range(max_iter):
        neigbors = get_all_neighbors(w)
        best_neighbor = w
        best_er = er_w(w, x, y)
        for n in neigbors:
            neighbor_er = er_w(n, x, y)
            if neighbor_er < best_er:
                best_neighbor = n
                best_er = neighbor_er
    #step 3
        if best_er < er:
            w = best_neighbor
            er = best_er
            errors.append(er)
        else:
            break
    return w, er, errors

df = pd.read_csv("CreditCard.csv")
#CreditApprove column done
df["Gender"] = df["Gender"].map({"M": 1, "F": 0})
df["CarOwner"] = df["CarOwner"].map({"Y": 1, "N": 0})
df["PropertyOwner"] = df["PropertyOwner"].map({"Y": 1, "N": 0})


x = df[["Gender", "CarOwner", "PropertyOwner", "#Children", "WorkPhone", "Email_ID"]]
y = df["CreditApprove"]
x= x.to_numpy()
y = y.to_numpy()

w, er, errors = hill_climb_algo(x, y)
print("Best w:", w.tolist())

print("Error:", er)


plt.plot(errors)
plt.xlabel("Round of search")
plt.ylabel("er(w)")
plt.title("Hill Climb Search")
plt.savefig("Figure2_LocalSearch.png")
plt.show()
