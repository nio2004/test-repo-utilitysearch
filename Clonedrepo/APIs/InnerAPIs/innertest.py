import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample user ratings dataset (user_id, movie_id, rating)
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3],
    'movie_id': [101, 102, 103, 101, 104, 102, 103, 105],
    'rating': [5, 4, 2, 5, 3, 4, 5, 1]
}

# Create DataFrame
ratings = pd.DataFrame(data)

# Create a pivot table
pivot_table = ratings.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)

# Calculate cosine similarity
similarity_matrix = cosine_similarity(pivot_table)
similarity_df = pd.DataFrame(similarity_matrix, index=pivot_table.index, columns=pivot_table.index)

# Function to get movie recommendations
def get_recommendations(user_id, num_recommendations=3):
    # Get similar users
    similar_users = similarity_df[user_id].sort_values(ascending=False).index[1:]
    
    # Get ratings from similar users
    similar_user_ratings = ratings[ratings['user_id'].isin(similar_users)]
    
    # Calculate weighted ratings
    recommendations = similar_user_ratings.groupby('movie_id').apply(
        lambda x: (x['rating'] * similarity_df[user_id][x['user_id']].values).sum() / similarity_df[user_id][x['user_id']].sum()
    ).sort_values(ascending=False)

    # Return top recommendations
    return recommendations.head(num_recommendations)

# Example usage
if __name__ == "__main__":
    user_id = 1  # Specify user_id for whom to recommend movies
    recommended_movies = get_recommendations(user_id)
    print(f"Recommended movies for User {user_id}:\n{recommended_movies.index.tolist()}")
