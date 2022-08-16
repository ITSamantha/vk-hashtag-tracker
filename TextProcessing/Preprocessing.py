import re
import string

from nltk.corpus import stopwords


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


