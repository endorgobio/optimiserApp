from pyomo.environ import *

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

def create_model_abstract():
    # create the model
    model = AbstractModel()

    # Define sets and parameters
    model.ITEMS = Set(ordered = False)
    model.profits = Param(model.ITEMS, within=PositiveReals)
    model.weights = Param(model.ITEMS, within=PositiveReals)
    model.capacity = Param(within=PositiveReals)

    # Define variables
    model.x = Var(model.ITEMS, within=Binary)

    # Define objective
    def value_rule(model):
        return sum(model.profits[i] * model.x[i] for i in model.ITEMS)
    model.value = Objective(sense=maximize, rule=value_rule)

    # Define constraint
    def weight_rule(model):
        return sum(model.weights[i] * model.x[i] for i in model.ITEMS) <= model.capacity
    model.weight = Constraint(rule=weight_rule)

    return model