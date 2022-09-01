from typing import List
from typing import AnyStr

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


#TODO: Сделать класс с определенной векторизацией и классификацией, храня модель (возможно и хештег)

def using_TF_IDF(texts1: List[AnyStr], texts2=None, min_df =  1):
    #TODO: Проверить  min_df!!!
    pd.set_option('display.max_columns', None)  # or 1000
    pd.set_option('display.max_rows', None)  # or 1000
    pd.set_option('display.max_colwidth', -1)  # or 199
    vectorizer = TfidfVectorizer(min_df = min_df)
    newText = vectorizer.fit_transform(texts1)
    #text = vectorizer.transform(texts2)

    matrix1 = pd.DataFrame(newText.toarray(), columns=vectorizer.get_feature_names_out())
    #matrix2 = pd.DataFrame(text.toarray(), columns=vectorizer.get_feature_names_out())
    return matrix1 #, matrix2

def knn_tf_idf(x_train, y_train,x_test=None, y_test=None):
    model = Pipeline([('tf-idf', TfidfVectorizer()),
                      ('knn', KNeighborsClassifier())])
    min_dfs = [i for i in range(2, 16)]
    knn_neighbours = [i for i in range(2, 21)]
    knn_neighbours.extend([20, 30, 40, 50, 100])
    #leaf_size = [i for i in range(1, 21)]
    params = [{
        'tf-idf__min_df': min_dfs,
        'knn__n_neighbors': knn_neighbours,
        'knn__weights': ['uniform', 'distance']}]

    gs_knn = GridSearchCV(model,
                          param_grid=params,
                          scoring='accuracy',
                          cv=5)
    gs_knn.fit(x_train, y_train)
    print(gs_knn.best_params_)

def for_test_using_TF_IDF(text: List[AnyStr], min_df = 1 ):
    #TODO: Проверить  min_df!!!
    vectorizer = TfidfVectorizer(min_df = min_df)

    x_test = vectorizer.transform(text)
    return  x_test




