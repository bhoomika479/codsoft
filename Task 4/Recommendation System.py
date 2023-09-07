# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample movie dataset
data = {'Title': ['Movie 1', 'Movie 2', 'Movie 3', 'Movie 4'],
        'Genre': ['Action', 'Comedy', 'Action', 'Drama'],
        'Description': ['Explosive action-packed movie', 'Hilarious comedy with great actors',
                        'Action thriller with suspense', 'Emotional drama with a powerful story']}
movies_df = pd.DataFrame(data)

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Compute the TF-IDF matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['Description'])

# Compute the cosine similarity between movies based on their descriptions
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations based on user preferences
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = movies_df[movies_df['Title'] == title].index[0]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 5 most similar movies (excluding the input movie itself)
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 recommended movies
    return movies_df['Title'].iloc[movie_indices]

# Example: Recommend movies similar to 'Movie 1'
recommendations = get_recommendations('Movie 1')
print("Recommended Movies:")
print(recommendations)