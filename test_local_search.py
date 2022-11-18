if __name__ == "__main__":
    import numpy as np
    from local_search import *
    
    # set random seed for reproducibility
    rand_seed=735122311
    np.random.seed(rand_seed)
    
    # helper function to generate random N-queens state
    def gen_rand_tuple(N=8):
        return tuple(np.random.randint(low=0, high=N, size=N))
        
    # tests 1
    rand_state = gen_rand_tuple()
    
    print('8-queens state: {}'.format(rand_state))
    print('f(s) = {}'.format(objective_function(rand_state)))
    print('{} is a goal? {}'.format(rand_state, is_goal(rand_state)))
    print('_______________________________________________________________________')
    
    goal_state = (2,0,3,1)
    print('4-queens state: {}'.format(goal_state))
    print('f(s) = {}'.format(objective_function(goal_state)))
    print('{} is a goal? {}'.format(goal_state, is_goal(goal_state)))
    print('_______________________________________________________________________')
    
    # tests run simulated annealing
    initial_state = gen_rand_tuple(N=8)
    initial_T = 1000
    final_state, iters = simulated_annealing(initial_state, initial_T=initial_T)
    print('Final state: {}'.format(final_state))
    print('Final state objective value: {}'.format(objective_function(final_state)))
    print('Final state is_goal?: {}'.format(is_goal(final_state)))
    print('# iterations: {}'.format(iters)) 
    
    initial_state = gen_rand_tuple(N=8)
    initial_T = 50000
    final_state, iters = simulated_annealing(initial_state, initial_T=initial_T)
    print('Final state: {}'.format(final_state))
    print('Final state objective value: {}'.format(objective_function(final_state)))
    print('Final state is_goal?: {}'.format(is_goal(final_state)))
    print('# iterations: {}'.format(iters)) 
    