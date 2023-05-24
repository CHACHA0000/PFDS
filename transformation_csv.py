import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder

class TransformationCsv:
    def __init__(self, filePath):
        self.df_voitures=pd.read_csv(filePath, names=('immat','marque','km','date_cir'),sep=';')
        self.liste_voiture=self.df_voitures['immat']
        self.ordinalEncoder=OrdinalEncoder()
        pass

    def transform(self):
        matrice_voiture=self.df_voitures.copy()
        matrice_voiture.set_index('immat', inplace=True)
        self.ordinalEncoder.fit_transform(matrice_voiture[['marque']])
        matrice_voiture['marque']=self.ordinalEncoder.transform(matrice_voiture[['marque']])
        matrice_voiture['date_cir']=pd.to_datetime(matrice_voiture['date_cir'], dayfirst=True)
        matrice_voiture['date_cir']=matrice_voiture['date_cir'].apply(lambda date : date.year)
        return np.array(matrice_voiture)
    
if(__name__=='__main__') :
    X=TransformationCsv('voitures.csv')
    y=X.transform()
    print(X.liste_voiture)

    print(y)
