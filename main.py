from typing import Optional
from joblib import load
from fastapi import FastAPI
from DataModel import DataModel2
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel:DataModel2):
   newDict=dataModel.dict()
   newDict=modificar_clave(newDict, "university_rating", "University Rating")
   newDict=modificar_clave(newDict, "cgpa", "CGPA")
   df = pd.DataFrame(newDict, columns=newDict.keys(), index=[0])
   g=list(df.columns)
   #df.columns = dataModel.columns()
   model = load("assets/lab4.joblib")
   result = model.predict(df) 
   res=float(result[0])
   return res

def modificar_clave(diccionario, vieja_clave, nueva_clave):
    return {clave if clave != vieja_clave else nueva_clave: valor for clave, valor in diccionario.items()}