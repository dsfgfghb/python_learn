import plotly.express as px
import matplotlib.pyplot as plt

data = [i*i*i for i in range(1,5001)]

fig,ax = plt.subplots()
ax.plot(data,linewidth=3)
ax.scatter(range(1,5001),data,c=data,cmap=plt.cm.Blues,edgecolors='none',s=10)
plt.show()