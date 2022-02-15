from duree import Duree
from titre import PINK_FLOYD


class PlayList:
    def __init__(self, base:list, ids:set):
        self.__base = base 
        self.__ids = set(ids)

    @property
    def base(self):
        return self.__base
    @property
    def ids(self):
        return self.__ids
    @base.setter 
    def base(self,base):
        self.__base= base 
    @ids.setter 
    def ids(self,ids):
        self.__ids = ids

    def titre(self,id_titre):
        return self.__base[id_titre]
    def duree(self,):
        duree_init = Duree(0,0,0)
        for id in self.__ids :
            duree_init=duree_init+self.__base[id].duree
        return duree_init
    def commun(self,playlist):
        return PlayList(self.__base, self.ids & playlist.ids)
    # def commun(self,autre_playlist):
    #     new_titre = list()
    #     for titre in self._base:
    #         for autre_titre in autre_playlist.base:
    #             if autre_titre==titre :
    #                 new_titre.append(autre_titre) 
    #     return PlayList(new_titre,)
    def __str__(self)-> str:
        chaine =""
        for id in self.__ids:
            chaine = chaine +(f"{id} [{self.__base[id].duree.min:02}:{self.__base[id].duree.sec:02}] {self.__base[id].titre} ({self.base[id].album}, {self.__base[id].annee})"+"\n")
        return chaine

## test playlist 
small = PlayList(PINK_FLOYD, {45, 32, 120})
print(small)
print(small.duree())


#!Créer xuan, bob et inaya, les PlayList des trois ami-es.


XUAN = {60, 45, 107, 10, 51, 5, 30, 83, 94, 22, 4, 136, 145, 52, 133, 125, 86, 31, 87, 118, 82, 32, 43, 3, 27, 97, 150, 79, 152, 114, 54, 53, 93, 80, 141, 18, 115, 105, 72, 142, 81, 149, 17, 104, 102, 39, 11, 36, 91, 147, 134, 84, 117, 15, 128, 89, 50, 113, 33, 61, 124, 23, 59, 40, 111, 26, 100, 112, 19, 135, 123, 44, 119, 62, 155, 78, 7, 110, 157, 98, 99, 34, 65, 58, 139, 77, 47, 46, 8, 88, 1, 49, 95, 16, 41}

BOB = {129, 134, 58, 65, 67, 0, 102, 140, 74, 34, 85, 73, 28, 40, 56, 101, 12, 25, 35, 68, 39, 55, 124, 37, 26, 49, 59, 146, 108, 36, 106, 21, 3, 117, 123, 143, 100, 64, 9, 22, 156, 76, 19, 4, 122, 79, 109, 62, 113, 142, 89, 152, 1, 128, 43, 81, 126, 94, 135, 118, 7, 136, 141, 93, 11, 114, 20, 95, 155, 53, 138, 42, 2, 78, 61, 10, 32, 132, 5, 110, 125, 72, 45, 111, 92, 88, 145, 121, 149, 150, 51, 41, 57, 69, 98, 63, 104, 47, 90, 48, 24, 120, 31, 130, 70}

INAYA = {57, 41, 29, 83, 72, 2, 38, 25, 132, 60, 14, 136, 140, 127, 152, 54, 13, 17, 16, 116, 119, 101, 133, 129, 95, 130, 18, 63, 15, 64, 156, 52, 39, 123, 10, 73, 157, 107, 7, 58, 103, 75, 154, 61, 86, 137, 87, 111, 12, 47, 24, 23, 8, 117, 35, 108, 150, 118, 44, 42, 26, 55, 3, 32, 30, 59, 97, 74, 67, 99, 69, 88, 135, 131, 46, 53, 128, 112, 145, 125, 82, 147, 71, 68, 93, 113, 36, 4, 141, 65, 40, 50, 20, 94, 19, 122, 56, 11, 49, 76, 34, 153, 79, 9, 0, 5, 28, 70, 138, 151, 110, 144, 77, 33, 22, 100, 90, 143, 155, 126}
playlist_XUAN= PlayList(PINK_FLOYD, XUAN)
playlist_BOB= PlayList(PINK_FLOYD, BOB)
playlist_INAYA= PlayList(PINK_FLOYD, INAYA)
#!Créer la PlayList commune aux trois personnes.
plalist_commune=playlist_XUAN.commun(playlist_BOB.commun(playlist_INAYA))
playlist_only_bob=PlayList(PINK_FLOYD, XUAN-BOB-INAYA)
print(playlist_only_bob)