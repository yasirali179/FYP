import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# reading .csv file
dataset = pd.read_csv(r"D:\FYP\Destinations.csv")

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(dataset['dest_description'])

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
results = {}
for idx, row in dataset.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], dataset['dest_id'][i]) for i in similar_indices]
    results[row['dest_id']] = similar_items[1:]

def destination(id):
    return dataset.loc[dataset['dest_id'] == id]['dest_name'].tolist()[0].split(' - ')[0]

# Just reads the results out of the dictionary
def recommend(dest_id, num):
    print("Recommending " + str(num) + " destinations similar to " + destination(dest_id) + "...")
    print("\n")
    recs = results[dest_id][:num]
    for rec in recs:
        print("Recommended Destination: " + destination(rec[1]) + " (score:" + str(rec[0]) + ")")