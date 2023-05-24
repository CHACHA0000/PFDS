from skimage.io import imread
import os
from PIL import Image
import pandas as pd
import numpy  as np



class TransformationImages():
    def __init__(self,path):
        self.path=path
        self.images_paths = os.listdir(self.path)
        
    
    def transform_image(self, path_image):
        with Image.open(path_image) as img:
            I1 = img.resize((10, 20))
            I2 = np.array(I1).flatten()
            return I2
              
    def transform(self):
        matrice_images=[]
        for image in self.images_paths:
            path_image=os.path.join(self.path, image)
            matrice_images.append(self.transform_image(path_image))
        return matrice_images
        
        
        
if(__name__=='__main__') :
    
    path='./Image_voitures'
    
    X=TransformationImages(path)
    transformed_x=X.transform()

    print(transformed_x)














