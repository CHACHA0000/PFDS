from voiture import Voiture 
from datetime import datetime
from transformation_images import TransformationImages
from transformation_text import TransformationText
from transformation_csv import TransformationCsv
import pandas as pd
import numpy as np
from PIL import Image
import math

class Agence:

    def __init__(self) :
        self.ImageTransformer=TransformationImages('./Image_voitures')
        self.TextTransfomer=TransformationText('./des_ documents_ texte de voitures')
        self.VoitureTransformer=TransformationCsv('./voitures.csv')


    # def ajouter(self,v):
    #     self.voitures.append(v)  
    
    # def afficher(self) :
    #     for v in self.voitures : 
    #         v.afficher()
    
    # fonction principal qui affiche les options de recherche
    # l'utilisateur doit choisir un des 3 méthodes affiché sur la ligne de commande
    def rechercher (self)  :
        option_recherch = input("selectioner les type de recherche (1: voiture, 2: description, 3: image) ")
        if (option_recherch == "1"):
            print(self.recherche_csv())
        
        if (option_recherch == "2"):
            print(self.recherche_text())

        if (option_recherch == "3"):
            print(self.recherche_image())

        pass
    
    # fonction pour caluculer la distance entre un requete (text, image, attribut_voiture) et un base de données
    def calcul_distances(self, index_req, base_de_donnee) :
        distances = []
        for i in range(len(base_de_donnee)):  
                distance = np.linalg.norm(base_de_donnee[i] - index_req)
                distances.append(math.sqrt(distance))
        return distances
    
    # fonction pour trier les vecteurs selon la distance par rapport à la requete
    def trier_vecteurs_par_distance(self, index_req, base_de_donnee):
        vecteurs_tries = sorted(base_de_donnee, key=lambda v: self.calcul_distances(index_req, base_de_donnee))
        return vecteurs_tries
    
    #fonction pour trier les vecteurs et affiche le nom du fichier
    def trier_par_distance(self, req, base_de_donnee, liste): 
        distance=self.calcul_distances(req, base_de_donnee)
        return [liste[i[0]] for i in sorted(enumerate(distance), key=lambda x:x[1])]
        

    # fonction pour saisir et rechercher un voiture dans un ficher csv
    # retourne une liste des immatriculations trié selon les distance caluculé par rapport à la requéte 
    def recherche_csv(self):
        req_voiture = Voiture()
        req_voiture.saisir()
        req = req_voiture.convertir_en_vecteur()
        df_req = pd.DataFrame(data=[req], columns=['marque','km','date_cir'])
        df_req['marque'] = self.VoitureTransformer.ordinalEncoder.transform(df_req[['marque']])
        liste_voiture = self.VoitureTransformer.liste_voiture
        return self.trier_par_distance(np.array(df_req).astype(float), self.BD_voiture, liste_voiture)

    # fonction pour saisir et rechercher un voiture grace à son image dans un dossier contenant des images de voitures
    # retourne une liste des nom des fichier trié selon les distance caluculé par rapport à la requéte 
    def recherche_image(self): 
        path_image_voiture = input("Veuillez saisir l'emplacement de votre image ")
        req_image = self.ImageTransformer.transform_image(path_image_voiture)
        liste_image = self.ImageTransformer.images_paths
        return self.trier_par_distance(req_image, self.BD_images, liste_image)

    # fonction pour saisir et rechercher un voiture grace à sa description dans un dossier contenant des documents texte
    # retourne une liste des nom des fichier trié selon les distance caluculé par rapport à la requéte 
    def recherche_text(self):
        description_voiture = input("veuillez decrire le vehicule ")
        query = self.TextTransfomer.preprocess(description_voiture)
        result = set()
        for word in query.split():
            result.update(self.BD_document[word])
        return result

        
    # transforme les données en matrice et les sauvegarde dans des variables
    def transform(self):
        self.BD_images = self.ImageTransformer.transform()
        self.BD_voiture = self.VoitureTransformer.transform()
        self.BD_document = self.TextTransfomer.transform()

            
            










if(__name__=='__main__') :
    a=Agence()
    a.transform()
    a.rechercher()
      
           





