import matplotlib.pyplot as plt

data = {'IT24': 1.0, 'IT20': 2.5, 'IT25': 3, 'IT21': 1.25}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)

# Plotting each type of chart on its respective subplot
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)

# Adding a title to the entire figure
fig.suptitle('Categorical Plotting')

# Displaying the plots
plt.show()
