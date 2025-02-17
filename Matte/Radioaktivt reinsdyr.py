import matplotlib.pyplot as plt

x_list = []
y_list = []
total = 0

for i in range(999):
    x_list.append(i)
    y_list.append(total)
    total*=(1-0.035)
    total+=2.5*(10**(-13))
print(total)
plt.plot(x_list, y_list)
plt.show()
