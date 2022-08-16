from nltk import pos_tag,ne_chunk
from nltk.stem.porter import PorterStemmer
from pymorphy2 import MorphAnalyzer
from nltk.tokenize import word_tokenize
from Preprocessing import preprocessing
from Preprocessing import remove_stopwords
morph = MorphAnalyzer()
stemmer = PorterStemmer()


def set_of_tokens(text: str, lang: str = 'english'):
    """
    НЕ ИСПЫТАНО!
    """
    text = preprocessing(text)
    text_tokens = word_tokenize(text)
    text_tokens = remove_stopwords(text_tokens, lang)
    text_tokens = set(text_tokens)
    normal_tokens = [morph.normal_forms(token) for token in text_tokens]
    print(normal_tokens)

    #text_tokens = set([morph.normal_forms(token) for token in text_tokens])
    return None


def dict_of_tokens(text: str, lang: str = 'english'):
    pass


def part_of_speech(text: str):


    text_tokens = word_tokenize(text)
    return pos_tag(text_tokens)


def create_tree_entities(text: str):
    text = preprocessing(text)
    text_tokens = word_tokenize(text)
    text_tokens = remove_stopwords(text_tokens, 'russian')

    word_pos = pos_tag(text_tokens)

    return ne_chunk(text_tokens)
