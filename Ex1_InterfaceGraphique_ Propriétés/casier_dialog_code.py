# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue
import casier
import casier_dialog

from logic import ls_Etudiants

def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
    """
    objet.label_erreur_numero_casier.setVisible(False)
    objet.label_erreur_numero_casier_2.setVisible(False)

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class FenetreCasier(QtWidgets.QDialog, casier_dialog.Ui_Dialog):
    def __init__(self,etudiant ,parent=None):
        super(FenetreCasier, self).__init__(parent)
        self.setupUi(self)
        self.etudiant = etudiant
        if etudiant.Casier.Num_casier != "":
            self.lineEdit_numero_casier.setText(etudiant.Casier.Num_casier)
            self.comboBox_localisation.setCurrentText(etudiant.Casier.Localisation_casier)
            self.comboBox_casier.setCurrentText(etudiant.Casier.Taille_casier)

        cacher_labels_erreur(self)
        """
                if self.etudiant.Casier != "":
            self.label_numero_casier.setText(self.etudiant.Casier.Num_casier)
        """



        self.setWindowTitle("Casier")

    @pyqtSlot()
    def on_pushButton_casier_clicked(self):

        is_valide = True
        nouv_c = casier.Casier()

        nouv_c.Num_casier = self.lineEdit_numero_casier.text()
        nouv_c.Taille_casier = self.comboBox_casier.currentText()
        nouv_c.Localisation_casier = self.comboBox_localisation.currentText()


        if nouv_c.Num_casier == "":

            is_valide = False
            self.label_erreur_numero_casier.setVisible(True)
        else:

            for e in ls_Etudiants:

                if self.etudiant.Casier.Num_casier != "":
                    if e.Casier.Num_casier == nouv_c.Num_casier:
                        is_valide = False
                        self.label_erreur_numero_casier_2.setVisible(True)

        print("isvalid")
        if is_valide:

            self.etudiant.Casier = nouv_c

            self.close()

