from fastapi import FastAPI
from starlette.responses import RedirectResponse
import pandas as pd
import numpy as np

app = FastAPI()

@app.get('/')
def raiz():
    return RedirectResponse(url="/docs/")

@app.get("/promedio_precio/")
async def promedio_precio(sucursal_id:str):
    df = pd.read_csv('app/Datasets/df.csv')
    precio_promedio1 = df[df['sucursal_id'] == sucursal_id]['precio'].mean()
    return {'promedio de precio': precio_promedio1}


#query 2: calcular el precio promedio de la marca DOVE
@app.get("/precio_promedio_marca/")
async def precio_promedio_marca(marca:str):
    df = pd.read_csv('app/Datasets/df.csv')
    precio_promedio_marca = df[df['marca'] == marca]['precio'].mean()
    return {"precio promedio de la marca DOVE:": precio_promedio_marca}


#query3: cantidad de veces que se vendio el producto_id mas vendido de la sucursaltipo 'Supermercado'
@app.get("/producto_mas_vendido/")
async def producto_mas_vendido(Supermercado:str):
    df = pd.read_csv('app/Datasets/df.csv')
    supermercado_df = df[(df['sucursaltipo']==Supermercado)]
    producto_mas_vendido = supermercado_df['producto_id'].value_counts().idxmax()
    cantidad_mas_vendida = supermercado_df['producto_id'].value_counts().max() 
    return {'producto más vendido': producto_mas_vendido, 'Cantidad de veces que se vendió':cantidad_mas_vendida}
