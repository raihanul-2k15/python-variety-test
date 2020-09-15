import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('pressure.csv', skiprows=1)
df['Pressure (MPa)'] = df['Pressure (Pa)'] / 1_000_000

x = df['KP (m)']
y = df['Pressure (MPa)']

plt.xlabel('KP (m)')
plt.ylabel('Pressure (MPa)')
plt.title('Pressure (MPa) vs KP (m)')
plt.plot(x, y)
plt.savefig('plot.png')
plt.show()
