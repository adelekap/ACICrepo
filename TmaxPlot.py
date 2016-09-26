#!/usr/bin/python
from netCDF4 import Dataset
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in("adelekoutia", "fnb2954bbn")
import os

with Dataset("/data/tmax.nc", "r") as tmax:
    tempMaxJ = tmax.variables["tmax"][0]
    tempMaxA = tmax.variables["tmax"][91]
    tempMaxY = tmax.variables["tmax"][182]
    tempMaxO = tmax.variables["tmax"][274]

    dataJ = [go.Heatmap(
        z=tempMaxJ,
        zmin=-7,
        zmax=27,
    )]
    py.image.save_as(dataJ, "J_Max.png")

    dataA = [go.Heatmap(
        z=tempMaxA,
        zmin=-7,
        zmax=27,
    )]
    py.image.save_as(dataA, "A_Max.png")

    dataY = [go.Heatmap(
        z=tempMaxY,
        zmin=-7,
        zmax=27,
    )]
    py.image.save_as(dataY, "Y_Max.png")

    dataO = [go.Heatmap(
        z=tempMaxO,
        zmin=-7,
        zmax=27,
    )]
    py.image.save_as(dataO, "O_Max.png")

