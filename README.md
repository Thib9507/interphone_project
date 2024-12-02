# interphone_project

# Demonstration

Voici une vidéo de démonstration du projet :
https://youtube.com/shorts/ggmPhYvfZKk

# Description

Ce projet est un système destiné à ouvrir une porte équipée d’une gâche électrique à la réception
d’un mot de passe par SMS en utilisant une Raspberry PI. La gâche de la porte s’ouvrant grace à la
présence d’un contact électrique, le script Python utilisé pour ce projet envoie un signal au GPIO 22
de la Raspberry pour ouvrir la gâche. Pour comprendre le fonctionnement d’une gâche classique,
voici une vidéo youtube montrant le montage d’un interphone (système fonctionnel à 20min53) :
https://youtu.be/QMOmKbfd9OQ?si=2MmwqsJjv4sskEza

**Attention** : La pin envoie une tension de 3.3V ce qui est faible : il faudra donc utiliser un relais
relié à une alimentation tierse correspondant aux caractéristiques de la gâche pour que le système
fonctionne.

# Installation du projet sur la raspberry

Pour installer ce projet, il suffit de télécharger le script python sur la raspberry. De le lancer en se
rendant dans le dossier où est stocké le script en executant la commande
_python_ **_nom_du_script_**
dans le terminal de la raspberry.

**Attention** : La Raspberry doit impérativement être connnectée à une connexion internet pour
pouvoir analyser les mails.

# Réception / analyse SMS

Pour analyser le mot de passe envoyé par SMS, on utilise la possibilité d’envoyer un SMS sur une
adresse mail afin d’éviter d’utiliser une carte sim sur la Raspberry PI.

**Attention** : Certains opérateurs ne prennent pas forcément en charge le transfert automatique des
SMS à une adresse mail. Renseignez-vous sur les services fournis par votre opérateur (l’opérateur
bouygues dispose de ce service).

Les différents opérateurs fonctionnent de la même manière pour transférer les SMS vers des mails :
ils stockent le contenu du SMS dans un txt qui est envoyé en pièce jointe du mail. Voici une vidéo
youtube le montrant (3min32) :
https://www.youtube.com/watch?v=K0LGjAdfX6s&ab_channel=KevinStratvert

L’adresse mail par défault utilisée pour recevoir les SMS est la suivante (valeur customisable dans
le script) :
_porte.eficia.interphone@gmail.com_


**_Customisation de l’adresse mail_**

Pour analyser les mails envoyés, le script python utilise le protocole IMAP. Il faut donc activer ce
protocole dans le paramétrage de l’adresse mail utilisé. Le mail peut aussi rendre impossible la
connexion via le script par manque de sécurité. Il est donc possible qu’il faille générer un mot de
passe spécifique pour le script. Voici pour exemple les étapes à suivre pour paramétrer une adresse
gmail :

## 1. Activer IMAP sur Gmail

- Connectez-vous à votre compte Gmail depuis un navigateur.
- Accédez aux **Paramètres** (icône d'engrenage en haut à droite) → **Voir tous les paramètres**.
- Allez dans l'onglet **Transfert et POP/IMAP**.
- Assurez-vous que l'accès IMAP est activé.
- Enregistrez les modifications.

## 2. Utiliser un mot de passe d'application

Google ne permet pas l'accès direct via mot de passe principal pour des applications moins

sécurisées. Vous devez générer un mot de passe d'application qui permet d’éviter les protocoles de

sécurité.

**Étapes pour générer un mot de passe d'application :**

```
1.Connectez-vous à votre compte Google.
2.Accédez à Sécurité → Connexion à Google.
3.Activez Validation en deux étapes (si ce n’est pas encore fait).
4.Une fois la validation activée, allez à Mots de passe d'application. (apppasswords en
anglais)
5.Sélectionnez l'application (par exemple, "Autre (nom personnalisé)") et donnez-lui un nom
(ex. "IMAP Python").
6.Google génère un mot de passe à 16 caractères (avec espace). Utilisez ce mot de passe à la
place de votre mot de passe principal dans votre script.
```

# Mot de passe

Le mot de passe par défault (case non sensitive) utilisé dans le script est le suivant (valeur
customisable dans le script) :
_ouvre la porte_

**Attention** : Le mot de passe est customisable mais ce dernier ce doit d’être inscrit en minuscule
dans le script (en raison de la méthode lower). Il est donc possible de rendre le mot de passe case
sensitive en remplaçant

if txt_content.lower() == 'ouvre la porte':

par

if txt_content == 'ouvre la porte':



