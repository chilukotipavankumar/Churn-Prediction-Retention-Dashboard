import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/customer_churn.csv')

app = dash.Dash(__name__)
fig = px.histogram(df, x='MonthlyCharges', color='Churn')

app.layout = html.Div([
    html.H1("Churn Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
