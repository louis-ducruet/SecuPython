import src.securite as securite
import src.fichier as fichier
import src.couleur as couleur
import src.app as app
import os

# Enable print color for windows terminal
os.system("color")


def start():
    chiffrement = securite.Securite([[13, 24], [8, 14]], [[-7 / 5, 12 / 5], [4 / 5, -13 / 10]])
    editeur = fichier.Fichier("input", "output")
    terminal = couleur.Couleur()

    app.efface(terminal)

    print(editeur.dossierExiste())
    print(editeur.fichierExiste("test.txt"))
    message = editeur.contenuFichier("test.txt")
    message = chiffrement.chiffrement(message, True)
    print(message)
    editeur.ecrireFichier("test.txt", message)
    message = chiffrement.chiffrement(message, False)
    print(message)
    input(f"Presser {terminal.bNoir}{terminal.fJaune}ENTRER{terminal.annule} pour quitter le programme.")


start()
