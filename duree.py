class Duree :
    def __init__(self,heure,min,sec):
        self.__heure =heure
        self.__min=min 
        self.__sec = sec 
    
    @property 
    def heure(self):
        return self.__heure
    @property
    def min(self):
        return self.__min 
    @property 
    def sec(self):
        return self.__sec
    @heure.setter 
    def heure(self,heure):
        self.heure=heure 
    @min.setter 
    def min(self, min):
        self.min = min 
    @sec.setter 
    def sec(self,sec):
        self.sec = sec
    def __repr__(self):
        return f"Duree({self.__heure},{self.__min}, {self.__sec})"
    def __str__(self):
        return f"heure:{self.__heure} min: {self.__min} sec: {self.__sec}"

    def __gt__(self, autre_duree):
        if(self.__heure> autre_duree.heure):
            return True
        elif(self.__heure < autre_duree.heure):
            return False
        else:
            if(self.__min >autre_duree.min):
                return True
            elif(self.__min < autre_duree.min):
                return False
            else: 
                if(self.__sec>autre_duree.sec):
                    return True 
                elif(self.__sec< autre_duree.sec):
                    return False 
                else:
                    return False

    def __lt__(self, autre_duree):
        return not(self.__gt__(autre_duree))

    def __eq__(self, autre_duree):
        return True if(
            self.__heure ==autre_duree.heure
            and self.__min == autre_duree.min
            and self.__sec == autre_duree.sec ) else False
    def __add__(self,autre_duree):
        sec =self.__sec+autre_duree.sec
        min=self.__min+autre_duree.min
        heure=self.__heure+autre_duree.heure
        return Duree.correct_duree(heure,min,sec)

    @classmethod
    def correct_duree(cls ,heure,min,sec):
        remain_min=0
        remain_heure=0
        total_sec = sec
        if(total_sec>=60 ):
            remain_min=total_sec//60
            sec = total_sec%60
        else: 
            sec=total_sec 
        total_min = min +remain_min
        if(total_min>60 ):
            remain_heure=total_min//60
            min = total_min%60
        else: 
            min = total_min
        heure =heure+remain_heure
        return Duree(heure=heure,min=min,sec=sec)



    @classmethod
    def duree(cls,duree_str):
        list_duree = duree_str.split(":")
        if(len(list_duree)==2):
            list_duree.insert(0,"0")
        return Duree.correct_duree(heure=int(list_duree[0]),min=int(list_duree[1]),sec=int(list_duree[2]))



            
d0=Duree(0,0,34)
d1=Duree(0,0,52)
print(d0+d1)
Duree.duree("6:19:20")
print(Duree.duree("70:70"))
print(Duree.correct_duree(1,0,70))