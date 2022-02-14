from duree import Duree


class PlayList:
    def __init__(self, base:list, ids:set):
        __base = base 
        __ids = set(ids)

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
        for titre in self.__base :
            duree_init=duree_init+titre.duree
        return duree_init
    def commun(self,playlist):
        return PlayList(self.base, self.ids & playlist.ids)
    # def commun(self,autre_playlist):
    #     new_titre = list()
    #     for titre in self._base:
    #         for autre_titre in autre_playlist.base:
    #             if autre_titre==titre :
    #                 new_titre.append(autre_titre) 
    #     return PlayList(new_titre,)
