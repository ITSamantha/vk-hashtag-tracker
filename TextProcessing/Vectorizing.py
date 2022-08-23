from typing import List
from typing import AnyStr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

#TODO: Сделать класс с определенной векторизацией и классификацией, храня модель (возможно и хештег)

def using_TF_IDF(text: List[AnyStr], min_df = 1 ):
    #TODO: Проверить  min_df!!!
    vectorizer = TfidfVectorizer(min_df = min_df)
    vectorizer.fit(text, init_model = )
    x_train = vectorizer.fit_transform(text, nit_model = )

    return  x_train


def for_test_using_TF_IDF(text: List[AnyStr], min_df = 1 ):
    #TODO: Проверить  min_df!!!
    vectorizer = TfidfVectorizer(min_df = min_df)

    x_test = vectorizer.transform(text)
    return  x_test




