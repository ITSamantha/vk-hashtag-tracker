from collections import Counter
import TextProcessing.Preprocessing as Preprocessing
from nltk import pos_tag,ne_chunk
from nltk.stem.porter import PorterStemmer
from pymorphy2 import MorphAnalyzer
from pymystem3 import mystem
from nltk.tokenize import word_tokenize
morph = MorphAnalyzer()
stemmer = PorterStemmer()


def set_of_tokens(text: str, lang: str = 'english'):
    """
    НЕ ИСПЫТАНО!
    """
    text = Preprocessing.preprocessing(text)
    lst_txt = using_mymorphy(text, lang)
    print(sorted(lst_txt, key = lambda x: x[0]))
    print(using_mystem(text))
    """Птицекрылка королевы Александры, или птицекрылка Александры, ' \
           'или птицекрыл королевы Александры, или орнитоптера Александра, ' \
           'или орнитоптера королевы Александры (Ornithoptera alexandrae) — ' \
           'вид дневных бабочек из рода Ornithoptera семейства парусников. ' \
           'Размах крыльев самцов достигает 14,7—22 см, самок — 18,7—24,8 см, ' \
           'а по некоторым данным даже до 28—30 см. Считается одной из крупнейших по размаху крыльев дневных бабочек в мире."""

    #text_tokens = set([morph.normal_forms(token) for token in text_tokens])
    return None

def using_mystem(text:str):
    text = Preprocessing.preprocessing(text)
    mmm = mystem.Mystem()

    text111 = mmm.lemmatize(text)
    text111 = [word for word in text111 if word != ' ' and word != '\n']
    text_set = set(text111)
    text_set = Preprocessing.remove_stopwords(text111, 'russian')
    counter = Counter(text_set)
    #return set(text_set)
    print("Что-то посчиталось")
    return sorted(counter.items(), key=lambda x: x[1],reverse=True)

def using_mymorphy(text:str,lang:str):
    text_tokens = word_tokenize(text)
    text_tokens = Preprocessing .remove_stopwords(text_tokens, lang)
    text_tokens = set(text_tokens)
    normal_tokens = [morph.normal_forms(token) for token in text_tokens]
    return normal_tokens


def dict_of_tokens(text: str, lang: str = 'english'):
    pass


def part_of_speech(text: str):


    text_tokens = word_tokenize(text)
    return pos_tag(text_tokens)


def create_tree_entities(text: str):
    text = Preprocessing .preprocessing(text)
    text_tokens = word_tokenize(text)
    text_tokens = Preprocessing.remove_stopwords(text_tokens, 'russian')

    word_pos = pos_tag(text_tokens)
    ss = ne_chunk(text_tokens)
    mmm = mystem.Mystem()
    ss1 = mmm.lemmatize(ss)
    ss1 = [word for word in ss1 if word != ' ' and word != '\n']
    text_set = set(ss1)
    text_set = Preprocessing .remove_stopwords(ss1, 'russian')
    counter = Counter(text_set)
    return sorted(counter.items(), key=lambda x: x[0])

