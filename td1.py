import numpy as np 

# Matrice de transition des états
transition = np.array([[0.7, 0.2, 0.1], [0.5, 0.3, 0.2], [0.4, 0.3, 0.3]])

# Etat initial ensoleillé
initial = np.array([1, 0, 0])

print("\n La matrice de transition est : \n", transition)
print("\n Le vecteur initial est : \n", initial)

# Matrice de transition dans 2 jours
dans_deux_jours = np.dot(transition, transition)


# Proba des états dans deux jours avec la formule : initial * dans_deux_jours
proba_etat_2 = np.dot(initial, dans_deux_jours)

print("\nLa probabilité qu'il fasse ensolleillé dans deux jours est de : ", proba_etat_2[0])
print("La probabilité qu'il fasse nuageux dans deux jours est de : {proba_nuageux:.2f}".format(proba_nuageux = proba_etat_2[1]))
print("La probabilité qu'il fasse pluvieux dans deux jours est de : ", proba_etat_2[2])


# Simulation temporelle
def simulation(n) :
    pluvieux = np.array([0, 0, 1])   

    resultat_simulation = ""
    puissance = transition
    passage = np.dot(initial, puissance)

    for i in range(2, n+1):
        if (i==1) :
            stockage = np.dot(initial, puissance)
        else :
            puissance = np.dot(transition, puissance)
            stockage = np.dot(initial, puissance)
        