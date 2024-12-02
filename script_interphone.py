import imaplib
import email
import RPi.GPIO as GPIO
import time

from email.policy import default

################################################################################################################
#######                          Initialization                   ##############################################
################################################################################################################
                                                                                                              ##
lastest_id_analysed = -1 # init lastest_id_analysed avec une valeur qui ne matchera jamais avec un mail id    ##
                                                                                                              ##
txt_content='random' # init txt_content si au moment du lancement le dernier mail n'a pas de txt              ##
                                                                                                              ##
################################################################################################################

# Connexion au serveur IMAP
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('porte.eficia.interphone@gmail.com', 'nnon wfpv napi bymq')          #   !!!! définition de l'adresse mail !!!!

lastest_id_analysed = 0


# boucle infinie dont il faut pas sortir sinon fin de script
while 1:

    mail.select('inbox')                                 # Sélectionner la boîte de réception

    status, messages = mail.search(None, 'ALL')          # Rechercher tous les e-mails

    latest_email_id = messages[0].split()[-1]            # Obtenir le numéro du dernier e-mail

    # Décoder l'ID du dernier e-mail en chaîne de caractères
    latest_email_id_str = latest_email_id.decode('utf-8')
    print(f"ID du dernier message recu : {latest_email_id_str}")


    if latest_email_id_str != lastest_id_analysed:

        print('Analyse du message')

        # Récupérer les datas du dernier e-mail
        status, msg_data = mail.fetch(latest_email_id_str, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1], policy=default)

        for part in msg.iter_attachments():                 # Vérifiez l'ensemble des pièces jointes 1 à 1
            if part.get_content_type() == 'text/plain':     # Vérifier si la PJ en cours d'analyse est un txt
                txt_content = part.get_content()            # Récupérer le contenu de la pièce jointe


        print(f'Voici le contenu du message : {txt_content}')

        if txt_content.lower() == 'ouvre la porte':            # !!!!!!! définition du mot de passe (lower utilisé pour ne pas etre case sensitive)  !!!!!!

            # Configuration du mode de numérotation des GPIO (BCM ou BOARD)
            GPIO.setmode(GPIO.BCM)                     # BCM utilise les numéros GPIO (comme GPIO 22)
            GPIO.setup(22, GPIO.OUT)                   # Configuration du GPIO 22 comme sortie

            # Activation du GPIO 22 (HIGH, 3.3V)
            GPIO.output(22, GPIO.HIGH)
            print("Porte ouverte")


            time.sleep(5)                              # Durée d'ouverture de la porte


            # Désactivation du GPIO 22 (LOW, 0V)
            print("Fermeture porte")
            GPIO.output(22, GPIO.LOW)

            # Nettoyage des configurations GPIO
            GPIO.cleanup()                             # Nettoyage des configurations GPIO

        else:
            print('Mot de passe incorrect')

        lastest_id_analysed = latest_email_id_str      # id traité sauvegardé

    else:
        print('Pas de nouveau message, aucune analyse lancée')

    # Attente de 2 secondes pour temporiser --> plus facile pour dev
    #time.sleep(2)
    print('\n \n')


mail.logout()        # Déconnexion
