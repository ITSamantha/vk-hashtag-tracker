import re
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def preprocessing_text(text: str, lang: str = 'russian'):
    text = text.lower()

    text = re.sub(r'[^a-zA-ZёЁа-яА-Я0-9 ]+', ' ', text)

    mystopwords = set(stopwords.words(lang))

    list_text = [word for word in text.split() if word not in mystopwords]
    text = ' '.join([word for word in list_text])
    text = re.sub(r'(?:^\s+)|(?:(?<=\s)\s+)|(?:\s+$)', '', text)



    return text


def get_tokens(text: str, lang: str):
    text = preprocessing_text(text, lang)
    return word_tokenize(text, language=lang)


