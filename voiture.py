import numpy as np
from datetime import datetime

marques={'kia':1,'peugeot':2,'mercedes':3,'bmw':4,'clio':5}

class Voiture:
    def __init__(self,mat='',marque='',kilom=0, date_circulation=datetime.now()):
        self.mat=mat
        self.marque=marque
        self.kilom=kilom
        self.date_circulation=date_circulation
    
    def saisir(self) :
        self.mat=input('donner la matricule de voiture ')  
        self.marque=input('donner la marque de voiture ') 
        self.kilom=int(input('la kilometrage de la voiture '))
        s=input('donner la date de circulation ')
        self.date_circulation=datetime.strptime(s.strip(), '%d/%m/%Y')
    
    def afficher(self):
        print ('%-15s|%-10s|%-8d|%-15s' %(self.mat,self.marque,self.kilom,self.date_circulation.strftime('%d/%m/%Y')))
        # self.date_circulation.strftime('%d/%m/%y')
    
    def convertir_en_vecteur(self): 
       # vecteur=np.array([marques[self.marque],self.kilom,self.date_circulation.year])
        vecteur = np.array([self.marque, self.kilom, self.date_circulation.year])
    
        return vecteur

    


if(__name__=='__main__'):
    v=Voiture()
    v.saisir()
    v.afficher()
    print(v.convertir_en_vecteur())
