#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']
names = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

bottom = np.zeros(3)
for i in range(4):
    plt.bar(people, fruit[i], width=0.5, bottom=bottom,
            color=colors[i], label=names[i])
    bottom = bottom + fruit[i]

plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.legend()
plt.show()
