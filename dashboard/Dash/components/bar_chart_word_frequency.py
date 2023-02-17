import plotly.express as px

long_df = px.data.medals_long()

print(long_df.head)

fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
fig.show()