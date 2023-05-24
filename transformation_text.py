import nltk
import os
import re
from collections import defaultdict

class TransformationText: 
    def __init__(self, path):
        self.path=path
        self.stopwords = set(nltk.corpus.stopwords.words('english'))
        pass

    def read_files(self, filePath):
        docs = {}
        for file in os.listdir(filePath):
            with open(os.path.join(filePath, file), "r", encoding="utf-8") as f:
                docs[file] = f.read()
        return docs


    def preprocess(self, doc):
        doc = doc.lower()  # Convertir en minuscules
        doc = re.sub(r'[^\w\s]', '', doc)  # Supprimer les caractères spéciaux
        doc = " ".join([word for word in doc.split() if word not in self.stopwords])  # Supprimer les stopwords
        return doc

    def transform(self):
        docs = self.read_files(self.path)
        preprocessed_docs = {}
        index = defaultdict(list)
        for doc_name, doc_content in docs.items():
            preprocessed_docs[doc_name] = self.preprocess(doc_content)
        for doc_name, doc_content in preprocessed_docs.items():
            for word in doc_content.split():
                index[word].append(doc_name)
        return index

    # def search(self, query):
    #     query = self.preprocess(query)
    #     result = set()
    #     for word in query.split():
    #         result.update(self.index[word])
    #     return result


if(__name__=='__main__') :
    TT=TransformationText('./des_ documents_ texte de voitures')
    TT.transform()

    # result = TT.search('polo')
    print(TT.index)

