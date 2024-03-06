Importations et Définition de Fonctions :
Le script commence par importer des modules tels que numpy, networkx, et définir des fonctions comme greedy_simulated_annealing_tsp, greedy_threshold_accepting_tsp, gen_complete_random_graph, gen_geometric_graph, etc.
Classe TSP :
La classe TSP est définie avec une initialisation prenant une matrice d'adjacence comme argument, une méthode get_solution pour générer un cycle aléatoire, et une méthode get_path_cost pour calculer le coût d'un cycle donné.
Fonctions Principales :
Des fonctions comme gen_best_solution cherchent la meilleure solution au TSP en utilisant différentes méthodes comme Christofides ou des approches gloutonnes.
La fonction gen_datum génère des données comprenant une matrice d'adjacence, le meilleur chemin trouvé par l'algorithme Christofides et d'autres informations liées à la résolution du TSP.
La fonction gather_all_data_from_temp_folder rassemble toutes les données stockées dans un dossier temporaire.
La fonction gen_dataset génère un ensemble de données pour résoudre le TSP en utilisant différentes méthodes et paramètres spécifiés.
Exécution du Code :
Le script vérifie s'il est exécuté en tant que fichier principal, puis appelle la fonction gather_all_data_from_temp_folder pour rassembler les données à partir d'un dossier temporaire.