from fastapi import FastAPI
import pickle, joblib
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    feature1: str
    feature2: float
    feature3: int

pickle_in = open("../../models/model.pkl", "rb")
print(pickle_in.read)
ml_model = joblib.load(pickle_in)

@app.post('/predict')
def predict(data: Item):
    data = data.dict()
    feature1 = data['feature1']
    feature2 = data['feature2']
    feature3 = data['feature3']

    prediction = ml_model.predict([[feature1, feature2, feature3]])

    return {'pediction': prediction}