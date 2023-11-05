<h1 align="center">OpenClassrooms Project N°11</h1>
<h2 align="center">P11_Améliorez une application Web Python par des tests et du débogage</h1>

![Logo LITReview](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/photos/logo-entete.png)


## Compétences aquises et évaluées de ce projet : 
* Implémentez une suite de tests Python.
* Debugger le code d’une application Python.
* Gérer les erreurs et les exceptions en Python


## Technologies utilisées :
* Python        (Version 3.11.5).
* Flask         (Version 3.0.0).
* Werkzeug      (Version 3.0.0).
* Pytest        (Version 7.4.3).
* Locust        (Version 2.18.1).
* pytest-cov    (Version 4.1.0).



## Contribuer au projet :
GUDLFT Système de réservation de places pour les clubs sportifs dans les compétitions est un projet open-source. N'hésitez pas à forker le code source et à contribuer avec vos propres fonctionnalités.

## Auteurs
L'équipe est composée de EL-WALID EL-KHABOU et de son mentor OpenClassRooms.

## Licence
Logiciel gratuit.

## Mission

Güdlft a mis sur pied une équipe appelée Régional « Outreach » chargée de créer une version plus légère (et moins coûteuse) de leur plateforme actuelle pour les organisateurs régionaux; L'objectif de l'application est de rationaliser la gestion des compétitions entre les clubs (hébergement, inscriptions, frais et administration).

L'équipe a dressé une liste de [spécifications fonctionnelles ainsi que le guide de développement](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/Mission/2-Sp%C3%A9cifications-fonctionnelles.pdf) pour un prototype, réparties en plusieurs phases et a mis déjà en œuvre la phase 1 du prototype.

Le rapport de QA pour cette phase 1 du projet montre qu’Il y a plusieurs bogues, dont un qui fait planter l'application ! Malheureusement.

Afin de résoudre tous les bogues de cette phase 1 déjà établie, et terminer la phase 2, Vous devrez cloner et forker le repo et le mettre en place sur votre machine locale (tout ce dont vous avez besoin se trouve dans ce fichier README). Ensuite, passez en revue les bogues dans la section des problèmes, puis essayez de reproduire les problèmes sur votre machine locale pour résoudre les bogues et ajouter la gestion des erreurs. 

Pour gagner du temps de configuration, nous utilisons Flask et JSON pour éviter d'utiliser une base de données. La plupart des outils dont vous aurez besoin se trouvent dans le fichier requirements.txt dans le repo, mais vous devrez installer Flask et notre framework de test préféré, pytest, ainsi que notre outil de test de performance, Locust.

Vous devrez également préparer un rapport de test et un rapport de performances, conformément au [guide de développement à la fin des spécifications fonctionnelles ci-jointes](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/Mission/2-Sp%C3%A9cifications-fonctionnelles.pdf). 

Dans toute cette démarche, il est impératif de suivre toutes les directives, car le QA nous reproche de ne pas respecter les normes. Vous devez tester de manière approfondie les résultats requis pour toutes les fonctionnalités de l'application. Je vous encourage également à adopter une approche de TDD (Test Driven Development), car c’est le meilleur moyen pour rationaliser votre travail.

Une fois que vous aurez terminé, nous ferons un examen de ce que vous avez dans la branche QA du code. Nous examinerons les rapports et la manière dont vous avez résolu les problèmes, nous examinerons votre code et nous testerons la couverture de la nouvelle fonctionnalité.


## Liste des documents fournis dans le dossier docs de ce projet :

1. [La mission de ce projet](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/Mission/1-Mission_de_ce_projet.pdf).

2. [Les spécifications fonctionnelles & le guide de développement](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/Mission/2-Sp%C3%A9cifications-fonctionnelles.pdf).

3. [Liste des Bogues de la version 1 de ce projet](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues).

4. [La structure finale et actuelle de ce projet fini](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/Mission/3-Structure_actuelle_de_ce_projet_fini.pdf).



## base donnée : 

L'application est alimentée par des fichiers JSON. Il s’agit de contourner la présence d'une base de données jusqu’à ce que nous en ayons réellement besoin. Les principaux fichiers .json sont :
1. Competitions.json - liste des compétitions : Voici la liste de toutes les compétitions existantes dans ce projet :

| Numéro | Nom de la compétition       | Date et Heure           | Nombre de places |
|--------|-----------------------------|-------------------------|------------------|
| 1      | Spring Festival             | 2020-03-27 10:00:00     | 25               |
| 2      | Fall Classic                | 2021-10-22 13:30:00     | 13               |
| 3      | Europe Class                | 2022-12-14 10:00:00     | 19               |
| 4      | Aust Lifting                | 2023-11-14 17:00:00     | 19               |
| 5      | LA Strong Man               | 2023-12-23 11:00:00     | 35               |
| 6      | Texas She Lifts             | 2024-03-02 13:30:00     | 35               |
| 7      | Fully Booked Competition    | 2024-03-02 13:30:00     | 0                |



2. Clubs.json - liste des clubs avec des informations pertinentes. Voici la liste des adresses e-mail que l'application   
   acceptera pour votre connexion : voici la liste des clubs existants dans ce projet : 

| Numéro | Nom             | E-mail                | Points |
|--------|-----------------|-----------------------|--------|
| 1      | Simply Lift     | john@simplylift.co    | 13     |
| 2      | Iron Temple     | admin@irontemple.com  | 4      |
| 3      | She Lifts       | kate@shelifts.co.uk   | 12     |
| 4      | Bodylift France | marina@bodylift.fr    | 16     |
| 5      | Belge Lifts     | sec@belge-lift.be     | 13     |
| 6      | Aust Build      | dany@austbuild.com    | 5      |



### Comment cloner ce référentiel GitHub: 

Vous devrez cloner et forker le repo en totalité avec toutes les branches existantes:
``` 
git clone https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT.git
```

### Se déplacer dans le projet:
```
cd 2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT
```

### Pour Récupérer toutes les branches:
```
git fetch origin
```

### Pour vérifier les branches disponibles
```
git branch -a
```

## Les Branches existantes dans ce projet:

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


### Pour se déplacer entre les branches:
```
git checkout nom_de_la_branche_sur_laquelle_vous_voulez_aller
```

### Créer un environnement virtuel Python (sur une machine linux):
```
python -m venv venv
```

## Activer l'environnement virtuel Python:

### Sur Windows : 
```
.\env\Scripts\activate
```

### Sur Linux :
```
source venv/bin/activate
```

## Importer les modules:
```
pip install -r requirements.txt
```

## Démarrage du serveur Flask :
Une fois tout ce qui précède est fait, démarrez flask avec la commande suivante :
```
flask run
```

### Il est temps maintenant de démarrer l'application sur votre navigateur :
Ouvrez votre navigateur et naviguez vers une des deux adresse suivantes :
```
http://127.0.0.1:5000

ou bien

http://localhost:5000```
```

# Les tests : 
Dans ce projet, plus de 58 tests en tout et pour tout ont été élaborés comme suit : 

| Nature des tests            | Nombre                       | Commande globale                                         |
|-----------------------------|------------------------------|----------------------------------------------------------|
| 1. Les tests unitaires      | 36 tests                     | ```pytest tests/unit/```                                 |
| 2. Les tests d'intégration  | 10 tests                     | ```pytest tests/integrity/```                            |
| 3. Les tests fonctionnels   | 12 tests                     | ```pytest tests/fonctionnels/```                         |
| 4. Les tests de performance | 1 test global                |1 test global donnant 2 rapports complets grâce à LOCUST  |


## Les tests unitaires : 36 tests, vous pouvez les executez en une seule fois par la commande suivante :
```
pytest tests/unit/
```
![Execution de tous les tests unitaires à la fois](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/photos/unit.png)


## Les tests d'intégration ou integrity-tests : 10 tests, vous pouvez les executez en une seule fois par la commande suivante :
```
pytest tests/integrity/
```
![Execution de tous les tests fonctionnels à la fois](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/photos/integrity.png)


## Les tests fonctionnels : 12 tests, vous pouvez les executez en une seule fois par la commande suivante :
```
pytest tests/fonctionnels/
```
![Execution de tous les tests fonctionnels à la fois](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/photos/fonctionnels.png)


## Les tests de performance : 1 test global donnant deux rapports complets grace à LOCUST.

### Installation de locust : 
Installez locust en copiant/collant la commande suivante :
```
pip install locust
```

### Execution du test LOCUST : 
Rendez vous dans le dossier qui habite le fichier locustfile.py avec la commande suivante : 
```
cd tests/performance
```

### Démarrez le test LOCUST: 
ATTENTION,  il est impératif que votre application soit fonctionnelle et le serveur flask soit démarré
avant d'executer le test LOCUST.

Executez le test locust avec la commande suivante :
```
locust
```
Puis ouvrez une autre fenetre de votre navigateur, et mettez vous sur l'adresse suivante : 
```
http://127.0.0.1:8089
```

### Lancez LOCUST :
Une fois que vous vous rendez sur l'adresse mentionnée dans la commande précédente, vous serez sur une page comme la suivante:

![LOCUST](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/photos/locust.png)

Remplissez ces 3 cases comme mentionné dans cette photo et validez en clickant sur 'Start swarming'


### Execution d'un seul test à la fois : 

Si vous voulez executer un seul test à la fois, vous pouvez utiliser la commande suivante : 
```
pytest tests/dossier/nom_du_test
```

Par exemple, si vous voulez executer le test unitaire nommé 'test_home_page_load.py' existant dans le dossier de tests 'unit'
vous devriez l'executer avec la commande suivante : 
```
pytest tests/unit/test_home_page_load.py
```

## Test & Rapports de couverture : 
```
pytest --cov=. --cov-report term-missing --cov-report html
```


### Vérification & Contrôle du code avec flake8 :
```
flake8 --format=html --htmldir=flake-report
```


# les rapports de cette mission & projet : 

1. [Rapports d'execution de tous les tests](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/rapport/tous-les-tests.pdf).

2. [Rapports d'execution de locust pour 6 utilisateurs et spawn-rate = 1](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/rapport/locust-6-1.pdf).

3. [Rapports d'execution de locust pour 6 utilisateurs et spawn-rate = 6](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/rapport/locust-6-6.pdf).

4. [Rapports de couverture globale](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/rapport/rapport_de_couverture.pdf).

5. [Rapports de couverture pour server.py](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/rapport/rapport_coverage_for_server_py.pdf).

6. [Rapport Flake8](https://github.com/waleedos/2023_P11_Ameliorer-app-Web_Python-par-des-tests-et-du-d-bogage_GUDLFT/blob/QA/docs/rapport/flake8-violations.pdf)


## Powered by EL-WALID EL-KHABOU
```
E-mail : ewek.dev@gmail.com
```