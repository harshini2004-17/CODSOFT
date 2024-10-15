import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample user-item rating data for collaborative filtering
ratings_data = {
    'User': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Movie1': [5, 4, 0, 0, 2],
    'Movie2': [3, 0, 0, 5, 1],
    'Movie3': [4, 0, 0, 0, 5],
    'Movie4': [0, 5, 3, 0, 0],
    'Movie5': [0, 0, 4, 2, 0]
}

# Create DataFrame for ratings
ratings = pd.DataFrame(ratings_data)
ratings.set_index('User', inplace=True)

# Calculate similarity matrix for collaborative filtering
similarity_matrix = cosine_similarity(ratings.fillna(0))
similarity_df = pd.DataFrame(similarity_matrix, index=ratings.index, columns=ratings.index)

# Function to recommend movies using collaborative filtering
def recommend_movies_collaborative(user, num_recommendations=2):
    similar_users = similarity_df[user].sort_values(ascending=False).index[1:]
    recommendations = {}
    
    for similar_user in similar_users:
        for movie in ratings.columns:
            if ratings.loc[similar_user, movie] > 0 and ratings.loc[user, movie] == 0:
                if movie in recommendations:
                    recommendations[movie] += ratings.loc[similar_user, movie]
                else:
                    recommendations[movie] = ratings.loc[similar_user, movie]
    
    # Sort recommendations by score
    recommended_movies = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    
    return [movie for movie, score in recommended_movies[:num_recommendations]]

# Sample movie data for content-based filtering
movies_data = {
    'Title': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'Genres': ['Action Comedy', 'Action', 'Comedy', 'Drama Action', 'Comedy Drama']
}

# Create DataFrame for movies
movies = pd.DataFrame(movies_data)

# User preferences for content-based filtering
user_preferences = 'Action Comedy'

# Create TF-IDF Vectorizer for content-based filtering
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(movies['Genres'])

# Calculate cosine similarity for content-based filtering
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to recommend movies using content-based filtering
def recommend_movies_content_based(user_pref, num_recommendations=2):
    user_vector = tfidf.transform([user_pref])
    sim_scores = linear_kernel(user_vector, tfidf_matrix).flatten()
    recommended_indices = sim_scores.argsort()[-num_recommendations:][::-1]
    return movies['Title'].iloc[recommended_indices].tolist()

# Example usage
if __name__ == "__main__":
    user = 'Alice'
    recommended_movies_collab = recommend_movies_collaborative(user)
    print(f"Recommended movies for {user} (Collaborative Filtering): {recommended_movies_collab}")
    
    recommended_movies_content = recommend_movies_content_based(user_preferences)
    print(f"Recommended movies based on preferences (Content-Based Filtering): {recommended_movies_content}")
