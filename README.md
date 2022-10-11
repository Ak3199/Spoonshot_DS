# Spoonshot_DS_App

Q1 - This code implements a recommendation system, which returns a ranked list based on the article that has been provided. The basic idea behind this implementation is that, when traversing through the article the similarity of the words present in the article to the words present in the ingreideint list would decide how relevant is the food item to this particular article and subsequently allot some points for the ranking. 

This code also involves some sort of NLP (using Wu & Palmer Similarity), as we are going through the synonyms of the words and its possible variations. I have tried to make this as generalised as possible, however there will always be some scope for improvement. 

The problems which I can currently identify but couldn't try and explore solutions to further was reducing the time complexity (it's current O(n^3)), adding better comparison techniques so that the result is more profound.I also thought of including web-scraping aspect wherein we use an API will be used to maybe get something like some nutritional value that will assist in ranking the food items.

Q2 - The time complexity of this code is O(n), it considers all the cases possible while trying to get the product of all the subsets present.
