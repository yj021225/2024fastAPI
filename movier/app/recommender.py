#recommender.py

import pandas as pd
import pickle
from scipy.sparse import coo_matrix

saved_model_fname = 'model/finalized_model.sav'
data_fname = 'data/ratings.csv'
item_fname = 'data/movies_final.csv'
weight = 10

def calculate_item_based(item_id, items):
    loaded_model = pickle.load(open(saved_model_fname, "rb"))
    recs = loaded_model.similar_items(itemid=int(item_id), N=11)
    return [str(items[r]) for r in recs[0]]

def item_based_recommendation(item_id):
    ratings_df = pd.read_csv(data_fname)
    ratings_df["userId"] = ratings_df["userId"].astype("category")
    ratings_df["movieId"] = ratings_df["movieId"].astype("category")
    movies_df = pd.read_csv(item_fname)

    items = dict(enumerate(ratings_df["movieId"].cat.categories))
    try:
        parsed_id = ratings_df["movieId"].cat.categories.get_loc(int(item_id))
        result = calculate_item_based(parsed_id, items)
    except KeyError as e:
        result = []
    result = [int(x) for x in result if x != item_id]
    result_items = movies_df[movies_df["movieId"].isin(result)].to_dict("records")
    return result_items

#recommender.py

def build_matrix_input(input_rating_dict, items):
    model = pickle.load(open(saved_model_fname, "rb"))
    # input rating list : {1: 4.0, 2: 3.5, 3: 5.0}

    item_ids = {r: i for i, r in items.items()}
    mapped_idx = [item_ids[s] for s in input_rating_dict.keys() if s in item_ids]
    data = [weight * float(x) for x in input_rating_dict.values()]
    # print('mapped index', mapped_idx)
    # print('weight data', data)
    rows = [0 for _ in mapped_idx]
    shape = (1, model.item_factors.shape[0])
    return coo_matrix((data, (rows, mapped_idx)), shape=shape).tocsr()


def calculate_user_based(user_items, items):
    loaded_model = pickle.load(open(saved_model_fname, "rb"))
    recs = loaded_model.recommend(
        userid=0, user_items=user_items, recalculate_user=True, N=10
    )
    return [str(items[r]) for r in recs[0]]


def user_based_recommendation(input_ratings):
    ratings_df = pd.read_csv(data_fname)
    ratings_df["userId"] = ratings_df["userId"].astype("category")
    ratings_df["movieId"] = ratings_df["movieId"].astype("category")
    movies_df = pd.read_csv(item_fname)

    items = dict(enumerate(ratings_df["movieId"].cat.categories))
    input_matrix = build_matrix_input(input_ratings, items)
    result = calculate_user_based(input_matrix, items)
    result = [int(x) for x in result]
    result_items = movies_df[movies_df["movieId"].isin(result)].to_dict("records")
    return result_items


