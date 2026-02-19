Mon projet a pour concept un quiz intelligent pour les étudiants.
L’utilisateur entre sa matière, son niveau et le sujet à réviser.
L’IA génère ensuite une question adaptée en fonction des informations envoyées.
Ensuite, l’étudiant renvoie une seconde requête avec la question générée et sa réponse

L’API analyse alors la réponse et peut continuer le quiz de manière interactive.

Au départ, le projet utilisait l’API OpenAI.
Cependant, j’ai rencontré des erreurs de quota (erreur 429), ce qui empêchait de tester correctement l’API.
J’ai donc choisi d’utiliser l’IA Groq (modèle Llama)
il faudra donc générer votre propre clé Groq et l’ajouter dans le code avant de lancer le projet.

exemple d'utilisation :
Body JSON :
Première requete dans le body :
{
  "matiere": "Anglais",
  "theme": "Dérivées",
  "niveau": "Lycée"
}
L’IA génère une question adaptée au niveau et à la matière.

Deuxième requête (répondre à la question)
Body JSON :
deuxième requete dans le body :
{
  "matiere": "Anglais",
  "theme": "Grammaire",
  "niveau": "Lycée",
  "question_precedente": "Que signifie le mot 'Hôpital' en anglais ?",
  "reponse_etudiant": "Hospital"
}
L’API analyse la réponse de l’étudiant et continue le quiz de manière intelligente.
