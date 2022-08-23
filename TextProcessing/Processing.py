from collections import Counter
from typing import Dict


from Preprocessing import preprocessing_text, get_tokens
import  re









def addToDict(dictionary: Dict, text: str, lang: str = 'russian'):
    """
    Запускать в мультипоточном режиме для каждого поста!
    """

    hashtags = [word for word in text.split() if re.fullmatch(r'\#[a-zA-ZёЁА-Яа-я\_\-0-9]+', word)]

    #for keyword in keywords:

      #  dictionary[keyword].append([hashtag for hashtag in hashtags])




def get_keywords(text: str, lang: str):



    text = preprocessing_text(text, lang)



    text = [word for word in text if re.fullmatch(r'[a-zA-ZёЁА-Яа-я\_\-0-9]+', word)]







    #return sorted(counter.items(), key=lambda x: x[1], reverse=True)



