import plotly.express as px

data = [i*i*i for i in range(1,6)]

fig = px.bar(x=list(range(1,6)),y=data)
fig.show()

data = [i*i*i for i in range(1,5001)]
fig = px.bar(x=list(range(1,5001)),y=data)
fig.show()