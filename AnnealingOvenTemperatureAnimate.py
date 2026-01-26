import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns

def animate(i):
    AnnealingOvenTemperature = pd.read_csv('UAAnnealingOvenTemperature.csv', index_col=0)
    sns.scatterplot(x='Time (hours)', y='Temperature (C)', data=AnnealingOvenTemperature, marker='o', color='b')

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.show()
