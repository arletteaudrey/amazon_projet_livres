# amazon_projet_livres
Projet d’extraction des données des 30 livres les plus vendus en 2022 sur Amazon

Etapes:
Web Scraping : Authentiﬁcation de mon poste de travail sur Amazon à l’aide d’un user agent obtenu sur https://http‐ bin.org/get. 

Utilisation des packages BeautifulSoup, Request pour extraire les données. Enﬁn les données recueillies ont été stocké dans un Dataframe qui a été converti en 
un ﬁchier csv.

Data Cleaning : Le ﬁchier csv obtenu d’Amazon a été nettoyé à partir d’Excel. Les doublons ont été retiré de même que les vides; les fonctions Proper et Trim ont permis 
d’harmoniser le contenu des colonnes.

Base de données : Connexion à une base de données PostgreSql via le package psycopg2 aﬁn de créer des tables correspondantes aux modèles de données récupéré sur amazon 
aﬁn de stocker les dataframes directement dans une base pour une exploitation prochaine, à travers PowerBI ou SAS Visual Analytics. 
