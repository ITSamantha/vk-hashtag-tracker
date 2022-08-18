from collections import Counter
from typing import Dict

from pymorphy2 import MorphAnalyzer
from pymystem3 import mystem
from nltk.stem.snowball import SnowballStemmer
from Preprocessing import preprocessing_text, get_tokens
import  re
morph = MorphAnalyzer()





def using_snowball(text: str, lang: str):
    """
    Альтернативный метод лемматизации

    """
    stemmer = SnowballStemmer(language=lang)
    tokens = get_tokens(text, lang)
    result = [stemmer.stem(token) for token in tokens]
    return result


def addToDict(dictionary: Dict, text: str, lang: str = 'russian'):
    """
    Запускать в мультипоточном режиме для каждого поста!
    """

    hashtags = [word for word in text.split() if re.fullmatch(r'\#[a-zA-ZёЁА-Яа-я\_\-0-9]+', word)]
    keywords = get_keywords(text, lang)
    # dict  : (string : set()) !!!
    for keyword in keywords:

        dictionary[keyword].append([hashtag for hashtag in hashtags])




def get_keywords(text: str, lang: str):
    """
    Основной метод лемматизации
    """


    text = preprocessing_text(text, lang)

    mmm = mystem.Mystem()
    text = mmm.lemmatize(text)
    text = [word for word in text if re.fullmatch(r'[a-zA-ZёЁА-Яа-я\_\-0-9]+', word)]



    size = len(text)
    counter = Counter(text)


    return sorted(counter.items(), key=lambda x: x[1], reverse=True)



def using_mymorphy(text: str, lang: str):
    """
    Альтернативный метод лемматизации
    """
    text_tokens = get_tokens(text, lang)
    normal_tokens = [morph.normal_forms(token) for token in text_tokens]
    return normal_tokens
