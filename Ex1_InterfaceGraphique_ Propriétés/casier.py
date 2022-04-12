import taillecasier
from taillecasier import TaillCasier

class Casier:
    """
    Calsse Casier
    """
    def __init__(self, p_num_casier:str = "" , p_taille_casier:str = "", p_localisation_casier:str = "-1", p_prix_casier:float = 20.00 ):
        self.__num_casier = p_num_casier
        self.Taille_casier = p_taille_casier
        self.Localisation_casier = p_localisation_casier
        self.__prix = p_prix_casier

    def _get_num_casier(self) -> str:
        return self.__num_casier
    def _set_num_casier(self, p_num_casier):
        if len(p_num_casier) == 5:
            print("p_num_casier[0].isalpha() and p_num_casier[1:].isnumeric()")
            if p_num_casier[0].isalpha() and p_num_casier[1:].isnumeric():
                print("++")
                self.__num_casier = p_num_casier

    Num_casier = property(_get_num_casier, _set_num_casier)

    def _get_prix(self)->float:
        return self.__prix

    def _set_prix(self, p_pix: float):
        if p_pix >= 0:
            self.__prix = p_pix

    Prix = property(_get_prix, _set_prix)


