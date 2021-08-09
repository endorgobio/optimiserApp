import pandas as pd
import pyomo
from pyomo.opt import SolverFactory
from pyomo.environ import *
import knapsack as kp
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc



# set the solver and its location
solvername='glpk'
solverpath_exe='C:\\glpk-4.65\\w64\\glpsol'
#solver=SolverFactory(solvername, executable=solverpath_exe)
solver=SolverFactory(solvername)

#solvername='gurobi'
#solver = SolverFactory(solvername)



# Data to create the model
profits = {'hammer':8, 'wrench':3, 'screwdriver':6, 'towel':11}
weights = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3}
ITEMS = profits.keys()

# Creates a concrete model
model = kp.create_model_concrete(ITEMS, profits, weights, 14)

# run the model
solver.solve(model)
objvalue = value(model.obj)

# Define the stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Creates the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                title="optimiser")
# need to run it in heroku
server = app.server

app.layout =html.Div(
            children=[objvalue]
)

# main to run the app
if __name__ == "__main__":
    app.run_server(debug=True)

