#!/usr/bin/python
from netCDF4 import Dataset
import plotly.plotly as py
import plotly.graph_objs as go
import os

username = raw_input("What is your plotly username?")
APIkey = raw_input("What is your API key?")

py.sign_in(str(username), str(APIkey))


with Dataset("/data/tmin.nc", "r") as tmin:
    tempMinJ = tmin.variables["tmin"][0]
    tempMinA = tmin.variables["tmin"][91]
    tempMinY = tmin.variables["tmin"][182]
    tempMinO = tmin.variables["tmin"][274]

    dataJ = [go.Heatmap(
        z=tempMinJ,
        zmin=-7,
        zmax=27,
    )]
    py.image.save_as(dataJ, "J_Min.png")

    dataA = [go.Heatmap(
        z=tempMinA,
        zmin=-7,
        zmax=27,
    )]
    py.image.save_as(dataA, "A_Min.png")

    dataY = [go.Heatmap(
        z=tempMinY,
        zmin=-7,
        zmax=27,
    )]
    py.image.save_as(dataY, "Y_Min.png")

    dataO = [go.Heatmap(
        z=tempMinO,
        zmin=-7,
        zmax=27,
    )]
    py.image.save_as(dataO, "O_Min.png")

