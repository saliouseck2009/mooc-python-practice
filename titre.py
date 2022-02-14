import sys
#sys.path.append(".")
from duree import Duree

class Titre :

    def __init__(self,titre:str,album:str,annee:str, duree:Duree):
        self.__titre= titre 
        self.__album= album 
        self.__annee = annee 
        self.__duree = duree 
    @property 
    def titre(self):
        return self.__titre
    @property 
    def album(self): 
        return self.__album
    @property 
    def annee(self): 
        return self.__annee
    @property 
    def duree(self):
        return self.__duree
    @titre.setter 
    def titre(self,titre):
        self.__titre = titre 
    @album.setter 
    def album(self, album):
        self.__album = album
    @annee.setter 
    def annee(self,annee):
        self.__annee = annee 
    @duree.setter 
    def duree(self, duree):
        self.__duree = duree
    def __repr__(self):
        return f"Titre({self.__titre},{self.__album}, {self.__annee}, {self.__duree})"
    def __str__(self):
        return f"Titre({self.__titre},{self.__album}, {self.__annee}, {self.__duree})"
    def __eq__(self, autre_titre: object) -> bool:
        return True if (self.__titre == autre_titre.titre and  self.__album ==autre_titre.album and  self.__annee == autre_titre.annee and self.__duree==autre_titre.duree ) else False
    @classmethod 
    def str_to_title(self,title_str):
        title_list =title_str.split(";")
        return Titre(titre=title_list[2],album=title_list[1],annee=title_list[0],duree=Duree.duree(title_list[3]))
    @classmethod
    def loadData(self):
        loaded = list()
        with open("pink_floyd_durees.csv",'r',encoding="utf-8") as f:
            for line in f:
                loaded.append(Titre.str_to_title(line))
        return loaded

title ="1971;Meddle;San Tropez;3:43"
PINK_FLOYD=Titre.loadData()