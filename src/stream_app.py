import streamlit as st
import pickle
import pandas as pd
import tkinter as tk


df = pd.read_csv('cleaned_data.csv')
# Load the pickled model
with open('modèles_previsions.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/1687147/pexels-photo-1687147.jpeg?auto=compress&cs=tinysrgb&w=1600");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
st.markdown("<h1 style='color: #256550 ; text-align:center;'> Mon Application d'éstimation de prix d'une voiture </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #256550 ; text-align:center;'>  </h2>", unsafe_allow_html=True)
  

# Définition des variables
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    etat_de_route = st.selectbox('Etat de route (donnez une note)', df['etat_de_route'].unique())
    carburant = st.selectbox('Le type de carburant', df['carburant'].unique())
    turbo = st.selectbox('Le type aspiration (turbo)', df['turbo'].unique())
    nombre_portes = st.selectbox('Le nombre de portes', df['nombre_portes'].unique())
    type_vehicule = st.selectbox('Style de carrosserie de la voiture', df['type_vehicule'].unique())
with col2:   
    transmission = st.selectbox('Le type de transmission', df['transmission'].unique())
    emplacement_moteur = st.selectbox("L'emplacement du moteur", df['emplacement_moteur'].unique())
    empattement = st.number_input('Empattement (en cm)')
    longueur_voiture = st.number_input('La longueur de la voiture (en cm)')
    largeur_voiture = st.number_input('La largeur de la voiture (en cm)')
with col3:
    hauteur_voiture = st.number_input('La hauteur de la voiture (en cm)')
    poids_vehicule = st.number_input('Le poids du vehicule (en Kg)')
    type_moteur = st.selectbox('Le type du moteur', df['type_moteur'].unique())
    nombre_cylindres = st.selectbox('Le nombre des cylindres', df['nombre_cylindres'].unique())
    taille_moteur = st.number_input('La taille du moteur en (cm cubes)')
with col4:
    systeme_carburant = st.selectbox('Le systeme carburant', df['systeme_carburant'].unique())
    taux_alésage = st.number_input("Le taux d'alésage (en millimètre)")
    course = st.number_input('La distance parcourue par le piston (en millimètre)')
    taux_compression = st.number_input('Le taux  de compression')
    chevaux = st.number_input('chevaux (en cv)')
with col5:
    tour_moteur = st.number_input('Tour moteur')
    consommation_ville = st.number_input('Consommation ville(en L per 100km)')
    consommation_autoroute = st.number_input('Consommation autoroute(en L per 100km)')
    marque_de_voiture = st.selectbox('La marque de voiture', df['marque_de_voiture'].unique())
    
    
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

        root = tk.Tk()
        root.title('Predicted price ')
        root.geometry('500x100')

        label = tk.Label(root, text=f'Le prix estimé de la voiture est : {predicted_price:.2f} $')
        label.config(bg='#86aa9f', fg='white', font=('Arial', 16), padx=10, pady=10)
        label.pack(fill=tk.BOTH, expand=True)

        root.mainloop()

         #st.info(f'Predicted price: {predicted_price:.2f} $')
    else:
        st.info('The trained data is not reasonable.')

