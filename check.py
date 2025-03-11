import pickle
movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity_score.pkl','rb'))
print("App Similarity Matrix Shape:", similarity.shape)
print("App Movies Shape:", movies.shape)
