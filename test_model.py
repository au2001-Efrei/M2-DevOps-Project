import pandas as pd
import joblib

max_delta = 0.1

def load_houses():
    return pd.read_csv('houses.csv')

def load_model():
    return joblib.load('regression.joblib')

def test_houses():
    model = load_model()
    houses = load_houses()

    for _, house in houses.iterrows():
        x = [house[['size', 'nb_rooms', 'garden']]]
        prediction, = model.predict(x)

        assert prediction >= house['price'] * (1 - max_delta)
        assert prediction <= house['price'] * (1 + max_delta)
