# Program below what to watch next based on the word vector similarity of the description of movies.
import spacy
nlp = spacy.load('en_core_web_md')

# Movie title and description to compare similarity
Planet_Hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."


def watch_next(description):
    # Function takes a description as a parameter, checks similarities to all movies in file movies.txt and returns most similar movie to previously watched 'Planet Hulk'.
    with open('C:/Users/Adam/Desktop/SEB/Task 38 - NLP Semantic/movies.txt', 'r', encoding='utf-8-sig') as file:
        movies = file.readlines()
        description = nlp(description)

    # List to store the similarities
    similarity_list = []

    # Looping through all the movies, checking similarities between them and adding to the list above.
    for movie in movies:
        similarity = nlp(movie).similarity(description)
        similarity_list.append(similarity)

    # Using max function to find the movie with the highest similarity
    highest_similarity = max(similarity_list)
    most_similar_movie = movies[similarity_list.index(highest_similarity)]

    return most_similar_movie

# Displaying searched suggestion
print(f"After a 'Planet Hulk' movie, next you should watch is:\n{watch_next(Planet_Hulk)}")


# ============

