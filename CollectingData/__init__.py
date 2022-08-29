import os
import pandas as pd
import re
import json
import vk_api
import TextProcessing.Lemmatization as p
from TextProcessing import Lemmatization, Preprocessing

VAR_NAME = "VK_Hashtag_Tracker"

CATEGORIES_FILE_NAME = "categories.txt"


#Создание json файла со словарем
def create_data_json_file(session, posts_count="50", posts_for_hashtag_count="100"):
    with open(CATEGORIES_FILE_NAME, "r",encoding='utf-8') as file:
        categories = [cat.replace('\n','') for cat in file.read().split(',')]
    print("Categories read: ", *categories)

    json_dict = dict()
    for category in categories:
        if category=="кино":
            break
        print(category+"\n")
        posts = find_posts(session, text=f"#{category}", count=posts_count)
        hashtags = list()
        for post in posts['items']:
            temp = [word.lower() for word in post['text'].split() if re.fullmatch(r'\#[a-zA-ZёЁА-Яа-я\_\-0-9]+', word.lower())]
            hashtags.extend(temp)
        hashtags = set(hashtags)
        print(hashtags, len(hashtags))
        json_dict[category] = dict()
        for hashtag in hashtags:
            temp_posts = find_posts(session, text=f"{hashtag}", count=posts_for_hashtag_count)
            text_posts = set([post['text'] for post in temp_posts['items']])
            json_dict[category][hashtag] = list()
            json_dict[category][hashtag].extend(
                [[word for word in Lemmatization.using_mystem(Preprocessing.preprocessing_text(text, 'russian'))
                  if re.fullmatch(r'[a-zA-ZёЁА-Яа-я\_\-0-9]+', word)]
                 for text in text_posts])
            print(hashtag + " done")

    """
    Dictionary structure:
    "category": {"hashtag":[lists of main words]}
    """
    df = pd.DataFrame.from_dict(json_dict, orient="index")# ПОДУМАТЬ О DataFrame

    df.to_csv("data.csv", index=False)

    with open("data.txt", "w" ,encoding="utf-8") as file:
        s = json.dumps(json_dict, ensure_ascii=False)
        file.write(s)

        # words = [p.using_mystem(posts['items'][i]['text']) for i in range(3)]
        # norm_words = [[word[0] for word in words[i][:10] if word[0].isalpha() and len(word)<=3] for i in range(len(words)) ]
        # print(norm_words)

def func(session):
    with open(CATEGORIES_FILE_NAME, "r", encoding='utf-8') as file:
        categories = [cat.replace('\n', '') for cat in file.read().split(',')]
    print("Categories read: ", *categories)

    for category in categories:
        print(category + "\n")
        posts = find_posts(session, text=f"#{category}", count="50")
        hashtags = list()
        for post in posts['items']:
            temp = [word.lower() for word in post['text'].split() if
                    re.fullmatch(r'\#[a-zA-ZёЁА-Яа-я\_\-0-9]+', word.lower())]
            hashtags.extend(temp)
        hashtags = set(hashtags)
        print(hashtags, len(hashtags))

def find_posts(session, text:str, count:str):
    return session.method('newsfeed.search', {'q': f"\"{text}\"", 'count': count})


def main():
    session = vk_api.vk_api.VkApi(token=os.environ[VAR_NAME])
    vk = session.get_api()
    create_data_json_file(session)



#Тестовая функция
def function(session):
    var = input('Введите текст:')
    a = session.method('newsfeed.search', {'q': f"\"{var}\"", 'count': "3"})
    words = [p.using_mystem(a['items'][i]['text']) for i in range(3)]
    for i in words:
        print(i)
    norm_words = [words[i][:3] for i in range(len(words))]
    print(norm_words)

if __name__ == '__main__':
    main()
