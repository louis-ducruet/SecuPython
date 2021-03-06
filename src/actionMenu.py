import src.app as app
import src.classe.affichage as affichage
import src.classe.email as email
import src.classe.fichier as fichier
import src.classe.securite as securite
import src.classe.user as user
import src.parametres as parametres


def action(terminal: affichage.Affichage, dossier: fichier.Fichier, chiffrement: securite.Securite,
           messagerie: email.Email, utilisateur: user.User):
    menu = input(terminal.input("un", "numéro", "correspondant à un menu"))
    if menu not in ["1", "2", "3", "4", "5"]:
        print(terminal.attention("Le menu \"{}\" n'existe pas".format(menu)))
        input(terminal.attendre("pour continuer"))
        return False
    app.efface(terminal)
    menu = int(menu)
    if menu % 2 == 0:
        if menu == 2:
            chiffrementTxt(terminal, dossier, chiffrement, False)
            return False
        else:
            while True:
                app.efface(terminal)
                app.afficheParametre(terminal)
                if parametres.action(terminal, messagerie, utilisateur):
                    return False
    else:
        if menu == 1:
            chiffrementTxt(terminal, dossier, chiffrement, True)
            return False
        if menu == 3:
            chiffrementImg(terminal, dossier, chiffrement)
            return False
        else:
            print(terminal.info("Vous êtes déconnecté(e)"))
            return True


def chiffrementTxt(terminal: affichage.Affichage, dossier: fichier.Fichier, chiffrement: securite.Securite, chiffre):
    # Affiche le titre du menu
    menuName = "Chiffrer" if chiffre else "Déchiffrer"
    print(terminal.info(menuName + " (.txt)"))
    # Demande le fichier et vérifie s'il existe
    file = input(
        terminal.input("le nom du fichier à {} dans le dossier".format(menuName.lower()), "{}".format(dossier.entree),
                       ""))
    print("")
    if dossier.fichierExiste(file) and file.endswith(".txt"):
        # Chiffre le fichier
        msg = chiffrement.chiffrementTxt(dossier.contenuFichier(file), chiffre)
        dossier.ecrireFichier(file, msg)
        print(terminal.info("Fichier {} disponible dans le dossier {}".format(menuName.lower(), dossier.sortie)))
    else:
        # Affiche qu'il n'existe pas
        print(terminal.attention("Le fichier {} n'existe pas ou n'est pas un .txt".format(file)))
    input(terminal.attendre("pour continuer."))


def chiffrementImg(terminal: affichage.Affichage, dossier: fichier.Fichier, chiffrement: securite.Securite):
    # Affiche le titre du menu
    print(terminal.info("Chiffrer/Déchiffrer" + " (.jpg, .jpeg, .png)"))
    # Demande le fichier et vérifie s'il existe
    file = input(
        terminal.input("le nom du fichier à chiffrer/déchiffrer dans le dossier", "{}".format(dossier.entree),
                       ""))
    if dossier.fichierExiste(file) and (file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")):
        # Chiffre le fichier
        msg = chiffrement.chiffrementImg(dossier.contenuImage(file))
        dossier.ecrireImage(file, msg)
        print(terminal.info("Fichier chiffrer/déchiffrer disponible dans le dossier {}".format(dossier.sortie)))
    else:
        # Affiche qu'il n'existe pas
        print(terminal.attention("Le fichier {} n'existe pas ou n'est pas un .jpg ou .jpeg ou .png".format(file)))
    input(terminal.attendre("pour continuer."))
