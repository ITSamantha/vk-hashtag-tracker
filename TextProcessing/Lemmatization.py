import re

from nltk import WordNetLemmatizer
from pymorphy2 import MorphAnalyzer
from pymystem3 import mystem
from nltk.stem.snowball import SnowballStemmer

from TextProcessing.Preprocessing import get_tokens


def using_mymorphy(text: str, lang: str):
    """
    Альтернативный метод лемматизации
    """
    morph = MorphAnalyzer()
    tag = morph.tag('Я')
    print(tag.POS)
    text_tokens = get_tokens(text, lang)
    normal_tokens = [morph.normal_forms(token) for token in text_tokens]
    return normal_tokens


def using_snowball(text: str, lang: str):
    """
    Альтернативный метод лемматизации

    """
    stemmer = SnowballStemmer(language=lang)
    tokens = get_tokens(text, lang)
    result = [stemmer.stem(token) for token in tokens]
    return result


def using_mystem(text: str, ):
    """
    Основной метод лемматизации
    Использовать для всего текста записи!
    """

    mmm = mystem.Mystem()
    text = mmm.lemmatize(text)
    text = ' '.join(text)
    text = re.sub(r'(?:^\s+)|(?:(?<=\s)\s+)|(?:\s+$)', '', text)
    print("done")
    return text


def usingWordNet(text: str, lang: str):
    lemmatizer = WordNetLemmatizer()
    tokens = get_tokens(text, lang)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

