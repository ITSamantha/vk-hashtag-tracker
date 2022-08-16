import re
import string
from pymorphy2 import MorphAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
morph = MorphAnalyzer()
stemmer = PorterStemmer()


def set_of_tokens(text: str, lang: str = 'english'):
    """
    НЕ ИСПЫТАНО!
    """
    text = preprocessing(text)
    text_tokens = word_tokenize(text)
    text_tokens = remove_stopwords(text_tokens, lang)

    normal_tokens = [morph.normal_forms(token) for token in text_tokens]
    print(normal_tokens)


    normal_tokens = [stemmer.stem(word) for word in text_tokens]
    print(normal_tokens)
    text_tokens = set([morph.normal_forms(token) for token in text_tokens])
    return None


def dict_of_tokens(text: str, lang: str = 'english'):
    pass


def preprocessing(text: str):
    text = text_lowercase(text)
    text = remove_numbers(text)
    text = remove_punctuation(text)
    text = remove_whitespace(text)
    return  text


def text_lowercase(text: str):
    return text.lower()


def remove_numbers(text: str):
    return re.sub(r'\d+', '', text)


def remove_punctuation(text: str):
    remover = str.maketrans('', '', string.punctuation + '—')
    return text.translate(remover)


def remove_whitespace(text: str):
    return re.sub(r'(?:^\s+)|(?:(?<=\s)\s+)|(?:\s+$)', '', text)


def remove_stopwords(text_tokens: list, lang: str):
    mystopwords = set(stopwords.words(lang))
    return [word for word in text_tokens if word not in mystopwords]


