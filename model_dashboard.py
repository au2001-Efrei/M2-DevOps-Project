import streamlit as st
import joblib

@st.cache
def load_model():
    return joblib.load('regression.joblib')

st.title('Prédiction de prix de maison')

taille = st.number_input('Taille maison')
nb_rooms = st.number_input('Nombre de chambre')
garden = st.number_input('Y a un jardin')

model = load_model()

if taille <= 0:
    st.write('mettre taille correcte')
if nb_rooms <= 0:
    st.write('mettre nombre de chambre correct')

if taille > 0 and nb_rooms > 0:
    X = [[taille, nb_rooms, garden]]
    prediction = model.predict(X)

    ## afficher la prediction
    st.write('le prix de la maison est : <span id="result">{}</span>'.format(prediction[0]), unsafe_allow_html=True)
