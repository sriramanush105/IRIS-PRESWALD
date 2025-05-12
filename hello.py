import pandas as pd
from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px


connect()

# Load Iris dataset (CSV 
df = get_df("IRIS")

# Display title
text("# Iris Data Explorer")

# Showing original data table
table(df, title="📋 Full Iris Dataset")

# Filtering using SQL
sql = "SELECT * FROM IRIS WHERE species = 'Iris-setosa' "
filtered_df =query(sql,"IRIS")

# Display filtered data
text("## Filtered Iris Data of Iris-setosa")
table(filtered_df)

# Scatter plot: Sepal Length vs Petal Length, color by species
text("## 📈 Sepal Length vs Petal Length by Species")
fig = px.scatter(
    df,
    x="sepal_length",
    y="petal_length",
    color="species",

)
plotly(fig)
