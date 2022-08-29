from typing import List
from typing import AnyStr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


#TODO: Сделать класс с определенной векторизацией и классификацией, храня модель (возможно и хештег)

def using_TF_IDF(text: List[AnyStr], min_df = 5 ):
    #TODO: Проверить  min_df!!!
    vectorizer = TfidfVectorizer(min_df = min_df)
    #vectorizer.fit(text, init_model = )
    #x_train = vectorizer.fit_transform(text, nit_model = )

    #return  x_train

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




