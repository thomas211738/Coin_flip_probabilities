import numpy as np
import matplotlib.pyplot as plt

# Binomial Distribution
# Formula: P(X=x)= (n choose k) * P^x * (1 - P)^(n - x)
#
# Edit this and see the results
flips = 432 # Flipping a coin 100 times
heads = 209 # Number of Heads in the number of flips

def Binomial_Distribution(flips, heads):
    
    fair_coin_prob = 0.5
    
    n_choose_k = np.math.comb(flips,heads)
    p_pow_k = np.power(fair_coin_prob,heads)
    q_pow_r = np.power(fair_coin_prob,(flips - heads))
    
    probability = n_choose_k * p_pow_k * q_pow_r
    
    return probability

def Cumulative_Distribution_Function(flips, heads):
    fair_coin_prob = 0.5

    cumulative_probability = 0
    for k in range(heads + 1):
        n_choose_k = np.math.comb(flips, k)
        p_pow_k = np.power(fair_coin_prob, k)
        q_pow_r = np.power(1 - fair_coin_prob, flips - k)
        cumulative_probability += n_choose_k * p_pow_k * q_pow_r
    
    p_value = cumulative_probability
    
#     if flips/2 < heads:
#         p_value = 1 - cumulative_probability
    return p_value

x = []
y = []
y2 = []

# Calculating P-Values all number of heads
for i in range(flips + 1):
    x.append(i)
    y.append(Cumulative_Distribution_Function(flips, i))
    y2.append(Binomial_Distribution(flips, i))
    
sig = [x > 0.05 and x < 0.95 for x in y]    
selected_values = [value for value, is_true in zip(x, sig) if is_true]

y3 = np.array(y2)
mu = round(np.mean(y3),2)
sigma = round(np.std(y3),2)


#Plotting
fig, ax = plt.subplots(2, 1, figsize=(7, 12))

ax[0].axhline(y=0.05, color='r', linestyle='--',label ='P-Value = 0.05')
ax[0].axhline(y=0.95, color='r', linestyle='--',label ='P-Value = 0.95')
ax[0].axvline(x=selected_values[0], color='g', linestyle='--',label = f'x = {selected_values[0]}')
ax[0].axvline(x=selected_values[-1], color='g', linestyle='--',label = f'x = {selected_values[-1]}')
ax[0].plot(x, y,label ='Distribution',linewidth=3,zorder=1)
ax[0].scatter(heads, y[heads-1],c='r', marker='o',zorder=2)
ax[0].set_xlabel('Number of Heads (n)')
ax[0].set_ylabel('P-Value')
ax[0].set_title(f'P-Values for n or less Heads given {flips} flips')

ax[1].plot(x, y2,linewidth=3,zorder=1,label ='Distribution')
ax[1].scatter(heads, y2[heads-1],c='r', marker='o',zorder=2)
ax[1].set_xlabel('Number of Heads (n)')
ax[1].set_ylabel('Probability')
ax[1].set_title(f'Probability of Number of heads given {flips} flips')
ax[1].axvline(x=selected_values[0], color='g', linestyle='--',label = f'x = {selected_values[0]}')
ax[1].axvline(x=selected_values[-1], color='g', linestyle='--',label = f'x = {selected_values[-1]}')

ax[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
ax[1].legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()    
probability = round(100 * y[heads - 1],2)
probability2 = round(100 * y2[heads - 1],2)

print(f'Probability of {heads} or less heads in {flips} flips is {probability}%')
print(f'Probability of exactly {heads} in {flips} flips is {probability2}%')
print(f'Mean for graph 2: {mu}')
print(f'Standard Deviation for graph 2: {sigma}')

      
