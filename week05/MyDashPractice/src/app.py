'''
 # @ Create Time: 2022-09-05 16:55:05.922032
'''

import pathlib
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__, title="MyDashPractice")

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

def load_data(data_file: str) -> pd.DataFrame:
    '''
    Load data from /data directory
    '''
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("data").resolve()
    return pd.read_csv(DATA_PATH.joinpath(data_file))

# replace with your own data source
df_org = load_data("all_currencies.csv")
df = df_org.copy()
df = df[['Date', 'Symbol', 'Open', 'High', 'Low', 'Close',
       'Volume', 'Market Cap']]
df['Volume'] = df['Volume'].fillna(round(df['Volume'].mean(),0))
df['Market Cap'] = df['Market Cap'].fillna(round(df['Market Cap'].mean(),0))

app.layout = html.Div([
    html.H4('Simple stock plot with adjustable axis'),
    html.Button("Switch Axis", n_clicks=0,
                id='button'),

    for _ in ALLOWED_TYPES
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"),
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    
    df_plot = df.groupby('Symbol').size().to_frame().reset_index()
    df_plot.columns = ['Symbol', 'Count']
    df_plot = df_plot.sort_values(by='Count', ascending=False)
    fig = px.histogram(df_plot[:10], x='Symbol', y='Count')
    

    
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
