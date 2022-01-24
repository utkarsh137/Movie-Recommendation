# Read the Dataset
# url of dataset from github repository
url = "https://raw.githubusercontent.com/utkarsh137/Movie-Recommendation/main/movie_metadata.csv"
data = pd.read_csv(url)
data.head()

#Let's drop unnecesseay columns that are useless for our analysis
data = data.drop(['color', 
                      'director_facebook_likes', 
                      'actor_3_facebook_likes', 
                      'actor_1_facebook_likes', 
                      'cast_total_facebook_likes', 
                      'actor_2_facebook_likes',  
                      'facenumber_in_poster', 
                      'content_rating', 
                      'country', 
                      'movie_imdb_link', 
                      'aspect_ratio',
                      'plot_keywords',
                      ], 
                       axis = 1)
data.columns
