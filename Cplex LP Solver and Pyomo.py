# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 21:53:28 2021

@author: Asus
"""

import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
model=pyo.ConcreteModel()
model.x=pyo.Var(bounds=(0,10))
x=model.x
model.y=pyo.Var(bounds=(0,10))
y=model.y
model.C1=pyo.Constraint(expr= -x +2*y <=8)
model.C2=pyo.Constraint(expr= 2*x+y<=14 )
model.C3=pyo.Constraint(expr=2*x-y<=10)
model.obj=pyo.Objective(expr=x+y, sense= maximize)
opt=SolverFactory("cplex")
opt.solve(model)

model.pprint()


x_value=pyo.value(x)