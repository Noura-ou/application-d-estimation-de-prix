import streamlit as st
import pickle
import numpy as np
import pandas as pd


df = pd.read_csv('cleaned_data.csv')
# Load the pickled model
with open('modèles_previsions.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("<h1 style='color: #256550 ; text-align:center;'> Mon Application d'éstimation de prix d'une voiture </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #256550 ; text-align:center;'>  </h2>", unsafe_allow_html=True)
  
# st.markdown(f"<h2 style='color: green;'>Les plus longs films : </h2>", unsafe_allow_html=True)


categorical_features = ['etat_de_route', 'carburant', 'turbo', 'nombre_portes', 'type_vehicule', 'transmission', 'emplacement_moteur', 'type_moteur',
                         'nombre_cylindres', 'systeme_carburant', 'marque_de_voiture']
numeric_features = ['empattement', 'longueur_voiture', 'largeur_voiture', 'hauteur_voiture', 'poids_vehicule', 'taille_moteur', 
                    'taux_alésage', 'course', 'taux_compression', 'chevaux', 'tour_moteur', 'consommation_ville', 'consommation_autoroute']

# Définition des variables
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    etat_de_route = st.selectbox('etat_de_route', df['etat_de_route'].unique())
    carburant = st.selectbox('carburant', df['carburant'].unique())
    turbo = st.selectbox('turbo', df['turbo'].unique())
    nombre_portes = st.selectbox('nombre_portes', df['nombre_portes'].unique())
    type_vehicule = st.selectbox('type_vehicule', df['type_vehicule'].unique())
with col2:   
    transmission = st.selectbox('transmission', df['transmission'].unique())
    emplacement_moteur = st.selectbox('emplacement_moteur', df['emplacement_moteur'].unique())
    empattement = st.number_input('empattement')
    longueur_voiture = st.number_input('longueur_voiture')
    largeur_voiture = st.number_input('largeur_voiture')
with col3:
    hauteur_voiture = st.number_input('hauteur_voiture')
    poids_vehicule = st.number_input('poids_vehicule')
    type_moteur = st.selectbox('type_moteur', df['type_moteur'].unique())
    nombre_cylindres = st.selectbox('nombre_cylindres', df['nombre_cylindres'].unique())
    taille_moteur = st.number_input('taille_moteur')
with col4:
    systeme_carburant = st.selectbox('systeme_carburant', df['systeme_carburant'].unique())
    taux_alésage = st.number_input('taux_alésage')
    course = st.number_input('course')
    taux_compression = st.number_input('taux_compression')
    chevaux = st.number_input('chevaux')
with col5:
    tour_moteur = st.number_input('tour_moteur')
    consommation_ville = st.number_input('consommation_ville')
    consommation_autoroute = st.number_input('consommation_autoroute')
    marque_de_voiture = st.selectbox('marque_de_voiture', df['marque_de_voiture'].unique())
    
    
# add a button to trigger prediction

    
if st.button('Predict Price'):
    # create a dictionary with user inputs
    input_data = {
        'etat_de_route': etat_de_route,
        'carburant': carburant,
        'turbo': turbo,
        'nombre_portes': nombre_portes,
        'type_vehicule': type_vehicule,
        'transmission': transmission,
        'emplacement_moteur': emplacement_moteur,
        'type_moteur': type_moteur,
        'systeme_carburant': systeme_carburant,
        'marque_de_voiture': marque_de_voiture,
        'empattement': empattement,
        'longueur_voiture': longueur_voiture,
        'largeur_voiture': largeur_voiture,
        'hauteur_voiture': hauteur_voiture,
        'poids_vehicule': poids_vehicule,
        'taille_moteur': taille_moteur,
        'taux_alésage': taux_alésage,
        'course': course,
        'taux_compression': taux_compression,
        'chevaux': chevaux,
        'tour_moteur': tour_moteur,
        'consommation_ville': consommation_ville,
        'consommation_autoroute': consommation_autoroute,
        'nombre_cylindres': nombre_cylindres
    }
    
    # convert the dictionary to a dataframe
    input_df = pd.DataFrame([input_data])
    
    # use the pre-trained model to predict the price
    predicted_price = model.predict(input_df)[0]
    
    # show the predicted price on the app
    if predicted_price>0:
         st.info(f'Predicted price: {predicted_price:.2f} $')
    else:
        st.info('The trained data is not reasonable.')


#____________________________________________________________________________________________________________________________________
# Load the pickled model
# with open('modèles_previsions.pkl', 'rb') as file:
#     model = pickle.load(file)


# # Create a function to make predictions using the loaded model
# def predict(model, input):
#     input_array = np.array
#     prediction = model.predict(input_array.reshape(1, -1))
#     return prediction[0]



# # Define categorical and numerical features
# categorical_features = ['etat_de_route', 'carburant', 'turbo', 'nombre_portes', 'type_vehicule', 'transmission', 'emplacement_moteur', 'type_moteur', 'nombre_cylindres', 'systeme_carburant', 'marque_de_voiture']
# numeric_features = ['empattement', 'longueur_voiture', 'largeur_voiture', 'hauteur_voiture', 'poids_vehicule', 'taille_moteur', 'taux_alésage', 'course', 'taux_compression', 'chevaux', 'tour_moteur', 'consommation_ville', 'consommation_autoroute']

# # Create a form for the user input
# with st.form(key='my-form'):
#     # Create selectbox for each feature
#     # Create a dictionary that maps each feature to its options
#     options = {
#         'nombre_portes': ['two', 'four'],
#         'nombre_cylindres': ['four', 'six', 'five', 'three', 'twelve', 'two', 'eight'],
#         'systeme_carburant': ['mpfi', '2bbl', 'mfi', '1bbl', 'spfi', '4bbl', 'idi', 'spdi'],
#         'type_moteur': ['dohc', 'ohcv', 'ohc', 'l', 'rotor', 'ohcf', 'dohcv'],
#         'transmission': ['rwd', 'fwd', '4wd'],
#         'emplacement_moteur': ['front', 'rear'],
#         'etat_de_route': [3, 1, 2, 0, -1, -2],
#         'marque_de_voiture': ['alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda', 'isuzu', 'jaguar', 'mazda', 'buick', 'mercury', 'mitsubishi', 'nissan', 'peugeot', 'plymouth', 'porsche', 'renault', 'saab', 'subaru', 'toyota', 'volkswagen', 'volvo'],
#         'carburant': ['gas', 'diesel'],
#         'turbo': ['std', 'turbo'],
#         'type_vehicule': ['convertible', 'hatchback', 'sedan', 'wagon', 'hardtop']
#     }

#     input = {}
#     for feature in categorical_features:
#         input[feature] = st.selectbox(f"Select {feature}", options=options[feature])
#     for feature in numeric_features:
#         input[feature] = st.number_input(f'Enter {feature}')

#     # Add a button to trigger the prediction
#     submit_button = st.form_submit_button(label='Make Prediction')

# # Call the prediction function and display the result
# if submit_button:
#     prediction = predict(model, input)
#     st.write('The prediction is:', prediction)



