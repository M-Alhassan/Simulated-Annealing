import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def handshake(n):
    if (n == 0):
        return 0
    else:
        return (n - 1) + handshake(n - 1)


def objective_function(state):
    N = len(state)    

    # check for sideway attacks
    side_attacks = 0
    visited = []
    for queen in state:
        if queen not in visited:
            visited.append(queen)
    
    for unique_queen in visited:
        side_attacks += handshake(state.count(unique_queen))

    # check for diagonal attacks
    diagonal_attacks = 0
    for i in range(N):
        for j in range(i+1, N):
            row_a = state[i]
            col_a = i+1
            row_b = state[j]
            col_b = j+1
            if abs(row_a - row_b) == abs(col_a - col_b):
                diagonal_attacks +=1
    
    return side_attacks + diagonal_attacks


def is_goal(state):
    if (objective_function(state) == 0):
        return True
    else:
        return False

def simulated_annealing(initial_state, initial_T=1000):
    current = initial_state
    T = initial_T
    iters = -1
    while(T >= 1e-14):
        iters +=1
        T=T*0.95
        rnd_queen = np.random.choice(range(len(current)))   # select a random queen
        rnd_val = np.random.choice([i for i in range(len(current)) if i != current[rnd_queen]]) # change it to a random position
        current_list = list(current)
        current_list[rnd_queen] = rnd_val  # new queen position
        successor = tuple(current_list)    # new state
        deltaE = objective_function(current) - objective_function(successor)
        if deltaE > 0:
            current = successor
        else:
            u = np.random.uniform()
            # probability of taking the successor
            if u <= np.exp(deltaE/T):     
                current = successor
        
    return (current, iters)

def visualize_nqueens_solution(n_queens, file_name):
    n_queens = list(n_queens)
    N = len(n_queens)
    arr = [[0 for col in range(N)] for row in range(N)]

    for row in range(0, N):
        if row in n_queens:
            arr[row][n_queens.index(row)] = 1
    
    nqueens_array = arr
    plt.figure(figsize=(N, N))
    hm = sns.heatmap(data=nqueens_array, cmap='Purples', linewidths=1.5,linecolor='k',cbar=False)
    hm.invert_yaxis()
    plt.savefig(file_name)
