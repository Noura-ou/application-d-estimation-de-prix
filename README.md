# Réaliser une application d'estimation de prix d'une voiture
L'objectif est de réaliser une application d'estimation de prix d'une voiture (Votre client, un revendeur de voiture, souhaite la création d'une application pouvant estimer le prix d'une voiture)

Developing a end-to-end prediction system

To develop end-to-end prediction based project we have to perform following sequence of activities.

    Data Collection
    EDA and Data Preprocessing
    Model Building
    Performance Evaluation and Draw Conclusion
    Deployment


#### La Base de Données :

    car_ID : un identifiant unique pour chaque voiture dans l'ensemble de données.
    symboling (etat_de_route) : le niveau de risque d'assurance de la voiture, où -2 est le plus risqué et +3 est le moins risqué.
    CarName (marque_voiture): le nom de la voiture, comprenant à la fois la marque et le modèle.
    fueltype (carburant) : le type de carburant utilisé par la voiture (soit "essence" ou "diesel").
    aspiration (turbo): si la voiture est à aspiration naturelle ou turbocompressée.
    doornumber (nombre_portes) : le nombre de portes de la voiture (soit "deux" ou "quatre").
    carbody (type_vehicule) : le style de carrosserie de la voiture (par exemple, berline, hatchback, convertible, etc.).
    drivewheel : le type de transmission utilisé par la voiture (par exemple, transmission à traction avant, transmission à propulsion arrière, transmission intégrale).
    enginelocation (emplacement_moteur) : l'emplacement du moteur (soit "avant" ou "arrière").
    wheelbase (empattement) : la distance entre les roues avant et arrière de la voiture.
    carlength (longueur_voiture) : la longueur totale de la voiture.
    carwidth (largeur_voiture) : la largeur totale de la voiture.
    carheight (hauteur_voiture ): la hauteur totale de la voiture.
    curbweight (poids_vehicule) : le poids de la voiture sans aucun occupant ni cargaison.
    enginetype (type_moteur) : le type de moteur utilisé par la voiture (par exemple, quatre cylindres, six cylindres, rotatif, etc.).
    cylindernumber (nombre_cylindres) : le nombre de cylindres dans le moteur de la voiture.
    enginesize (taille_moteur) : la taille du moteur de la voiture en centimètres cubes (cc).
    fuelsystem (systeme_carburant) : le type de système de carburant utilisé par la voiture (par exemple, carburé, à injection de carburant).
    boreratio (taux_alésage) : le rapport du diamètre des cylindres du moteur à leur longueur.
    stroke (course) : la distance parcourue par le piston en montée et en descente dans les cylindres du moteur.
    compressionratio (taux_compression) : le rapport du volume de la chambre de combustion du moteur lorsque le piston est en bas de sa course par rapport à lorsqu'il est en haut de sa course.
    horsepower (chevaux) : la puissance du moteur de la voiture en chevaux-vapeur (cv).
    peakrpm (tour_moteur) : la vitesse de rotation du moteur à laquelle la puissance maximale de la voiture est produite.
    citympg (consommation_ville) : l'économie de carburant de la voiture en miles par gallon (mpg) en conditions de conduite en ville.
    highwaympg (consommation_autoroute) : l'économie de carburant de la voiture en miles par gallon (mpg) en conditions de conduite sur autoroute.
    price (prix) : le prix de détail suggéré par le fabricant (MSRP) de la voiture en dollars américains.



#### Les conversions effectuées sur les variables : 


    empattement : en centimètre (1 pouce = 0,0254 mètre)
    longueur : en centimètre
    largeur : en centimètre
    hauteur : en centimètre
    poids_vehicule : en kilogramme (1 livre = 0,453592 kilogramme)
    taille_moteur : en centimètre cube (1 pouce cube = 0,0163871 litre)
    taux_alésage : en millimètre (1 pouce = 25,4 millimètres)
    course : en millimètre
    taux_compression : en ratio (pas de conversion nécessaire)
    tour_moteur : en tours par minute (pas de conversion nécessaire)
    consommation_ville : en litres aux 100 km (1 mile par gallon = 0,425 km par litre)
    consommation_autoroute : en litres aux 100 km




Bonus :

    Rendre le modèle accessible via une API


## Features
 ⚠️ - Done


## Run the project Locally

Clone the project

```bash
git clone git@github.com:Noura-ou/application-d-estimation-de-prix.git
````

Go to the project directory :

```bash
  cd my-project
```


## Useful Documentation

- [Learning Curves IN Python SKlearn](https://vitalflux.com/learning-curves-explained-python-sklearn-example/)
- [Encodage et Normalisation](https://www.youtube.com/watch?v=OGWwzm304Xs&list=PLO_fdPEVlfKqMDNmCFzQISI2H_nJcEDJq&index=25) 
- [Bonus Piplines](https://www.youtube.com/watch?v=41mnga4ptso&list=PLO_fdPEVlfKqMDNmCFzQISI2H_nJcEDJq&index=26)
- [Les métriques de régression](https://www.youtube.com/watch?v=_TE9fDgtOaE&list=PLO_fdPEVlfKqMDNmCFzQISI2H_nJcEDJq&index=24)



## Authors

- [@noura-ou](https://github.com/Noura-ou)