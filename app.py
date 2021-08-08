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



# call function to create model
profits = {'hammer':8, 'wrench':3, 'screwdriver':6, 'towel':11}
weights = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3}
ITEMS = profits.keys()


def create_model_concrete(ITEMS, profits, weights, capacity):
    # create the model
    model = ConcreteModel(name="Knapsack")
    # Create set of items
    model.ITEMS = Set(initialize = ITEMS)
    # Create parameters
    model.profits = Param(model.ITEMS, initialize = profits)
    model.weights = Param(model.ITEMS, initialize=weights)
    model.capacity = Param(initialize=capacity)

    # create the variables
    model.x = Var(model.ITEMS, within=Binary)
    # Define objective funtion
    def obj_rule(model):
        return sum(model.profits[i]*model.x[i] for i in model.ITEMS)
    model.obj = Objective(rule=obj_rule, sense=maximize)

    # Defines constraint
    def weight_rule(model):
        return sum(model.weights[i] * model.x[i] for i in model.ITEMS) <= model.capacity
    model.weight = Constraint(rule=weight_rule)

    return model


# 1. Concrete model
# Creates a concrete model
model = kp.create_model_concrete(ITEMS, profits, weights, 14)

# run the model
solver.solve(model)
objvalue = value(model.obj)

# print solution of decision variables
#print("1. print")
#model.pprint()
#
# #2. Abstract Model
# # Creates an abstract model
# model = kp.create_model_abstract()
#
# data_init= {None: dict(
#         ITEMS = ITEMS,
#         profits = {'hammer':8, 'wrench':3, 'screwdriver':6, 'towel':11},
#         weights = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3},
#         capacity = {None: 14}
#         )}
#
# # Creates am instance of the abstract model
# instance = model.create_instance(data_init)
# # run the model
# solver.solve(instance)
#
# # print solution of decision variables
# print("2 print")
# instance.pprint()
#
# #3. Read external data
# filepath = os.path.dirname(os.getcwd()) + "/data/"
# filename = 'data_nb.csv'
# df = pd.read_csv(filepath + filename)
# ITEMS = df['item']
# profits = {df.loc[i,'item']: df.loc[i,'profit'] for i in range(len(df['item']))}
# weights = {df.loc[i,'item']: df.loc[i,'weight'] for i in range(len(df['item']))}
#
# # Creates a concrete model
# model = kp.create_model_concrete(ITEMS, profits, weights, 100)
# model.pprint()
# # run the model
# solver.solve(model)
#
# # print solution of decision variables
# print("3. print")
# print('objective value')
# print(value(model.obj))

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

