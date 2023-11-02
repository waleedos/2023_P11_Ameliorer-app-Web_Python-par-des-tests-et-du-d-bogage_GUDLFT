<h1 align="center">OpenClassrooms Project N°11</h1>
<h2 align="center">P11_Améliorez une application Web Python par des tests et du débogage</h1>

![Logo LITReview](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/logo-entete.png)


## Technologies
* Python (Version 3.11.5)
* Flask (Version 3.0.0)
* Werkzeug (Version 3.0.0)
* Pytest (Version 7.4.3)
* Locust (Version 2.18.1)


## Contribuer au projet
GUDLFT Système de réservation de places pour les clubs sportif dans les compétitions est un projet open-source. N'hésitez pas à forker le code source et à contribuer avec vos propres fonctionnalités.

## Auteurs
L'équipe est composée de EL-WALID EL-KHABOU et de son mentor OpenClassRooms.

## Licence
Logiciel gratuit.

## Mission

Güdlft a mis sur pied une équipe appelée Régional « Outreach » chargée de créer une version plus légère (et moins coûteuse) de leur plateforme actuelle pour les organisateurs régionaux; L'objectif de l'application est de rationaliser la gestion des compétitions entre les clubs (hébergement, inscriptions, frais et administration).

L'équipe a dressé une liste de spécifications fonctionnelles pour un prototype, réparties en plusieurs phases et a mis déjà en œuvre la phase 1 du prototype.

Le rapport de QA pour cette phase 1 du projet montre qu’Il y a plusieurs bogues, dont un qui fait planter l'application ! Malheureusement.

Afin de résoudre tous les bogues de cette phase 1 déjà établie, et terminer la phase 2, Vous devrez cloner et forker le repo et le mettre en place sur votre machine locale (tout ce dont vous avez besoin se trouve dans ce fichier README). Ensuite, passez en revue les bogues dans la section des problèmes, puis essayez de reproduire les problèmes sur votre machine locale pour résoudre les bogues et ajouter la gestion des erreurs. 

Pour gagner du temps de configuration, nous utilisons Flask et JSON pour éviter d'utiliser une base de données. La plupart des outils dont vous aurez besoin se trouvent dans le fichier requirements.txt dans le repo, mais vous devrez installer Flask et notre framework de test préféré, pytest, ainsi que notre outil de test de performance, Locust.

Vous devrez également préparer un rapport de test et un rapport de performances, conformément au
guide de développement à la fin des spécifications fonctionnelles ci-jointes. 

Dans toute cette démarche, il est impératif de suivre toutes les directives, car le QA nous reproche de ne pas respecter les normes. Vous devez tester de manière approfondie les résultats requis pour toutes les fonctionnalités de l'application. Je vous encourage également à adopter une approche de TDD (Test Driven Development), car c’est le meilleur moyen pour rationaliser votre travail.

Une fois que vous aurez terminé, nous ferons un examen de ce que vous avez dans la branche QA du code. Nous examinerons les rapports et la manière dont vous avez résolu les problèmes, nous examinerons votre code et nous testerons la couverture de la nouvelle fonctionnalité.


## Liste des documents fournis dans le dossier docs de ce projet :

1. [La mission de ce projet]().

2. [Les spécifications fonctionnelles & le guide de développement]().

3. [Liste des Bogues de la version 1 de ce projet](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues).

4. [La structure finale et actuelle de ce projet finie]().


## Comment cloner ce référentiel GitHub: 

Vous devrez cloner et forker le repo en totalité avec toutes les branches existantes:
``` 
git clone https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT.git
```

### Se déplacer dans le projet:
```
cd 2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT
```

### Créer un environnement virtuel Python:
```
python -m venv venv
```

### Activer l'environnement virtuel Python:
```
source venv/bin/activate
```

### Importer les modules:
```
pip install -r requirements.txt
```

### Lancer le serveur Flask:
```
flask run
```

### les Branches existantes dans ce projet:

1.  1-Amelioration/ajout_de_CSS_pour_les_3_pages_html_de_depart
2.  2-Bug/Entering_unknown_email_crashes_the_app
3.  3-Bug/should_not_be_able_to_use_more_than_points_collected
4.  4-Bug/max_12_places_for_booking_per_competition
5.  5-bug/booking-places-past-competitions
6.  6-Amelioration/ajout_club_table
7.  QA
8.  Tests/Ajout_de_tous_les_tests_fonctionnels
9.  Tests/Ajout_de_tous_les_tests_integration
10. Tests/Ajout_de_tous_les_tests_performance
11. Tests/Ajout_de_tous_les_tests_unitaires
12. main


6. Testing
    
    The tests have been written for the pytest tools (unitary/integration/functional) and for locust (performances). These tools should be installed automatically from  requirements.txt. If not, the following commands can be launched:

    ```
    $ pip install pytest
    $ pip install pytest-flask
    $ pip install coverage
    $ pip install pytest-cov
    $ pip install locust
    ```

    And the tests can be started from the main folder with either of the following commands (adding coverage/reports):

    ```
    $ pytest
    $ pytest --cov=.
    $ pytest --cov=. --cov-report html
    ```

    locust can also be launched from the test folder.
    The coverage of the code with pytest is 100%.