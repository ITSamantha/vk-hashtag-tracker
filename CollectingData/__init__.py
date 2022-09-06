import os
import pandas as pd
import re
import vk_api

import threading

import TextProcessing
import TextProcessing.Lemmatization as p
from TextProcessing import Lemmatization, Preprocessing

VAR_NAME = "VK_Hashtag_Tracker"

CATEGORIES_FILE_NAME = "categories.txt"


# Возвращает DataFrame
def create_dataframe_from_categories(session,category,posts_count="75", posts_for_hashtag_count="100"):
    """
    Функция создает DataFrame для списка категорий из файла.
    Колонки DataFrame: ['category','hashtag','list_of_words']
    """
    main_list = list()
    posts = find_posts(session, text=f"#{category}", count=posts_count)
    hashtags = list()
    for post in posts['items']:
        temp = [word.lower() for word in post['text'].split() if
                    re.fullmatch(r'\#[a-zA-ZёЁА-Яа-я\_\-0-9]+', word.lower())]
        hashtags.extend(temp)
    hashtags = set(hashtags)
    print("Количество хэштегов:",len(hashtags),"\nХэштеги:", ','.join(hashtags))
    i=1
    for hashtag in hashtags:
        temp_posts = find_posts(session, text=f"{hashtag}", count=posts_for_hashtag_count)#TODO:исправить повторение текстов для разных хэштегов
        text_posts = set([post['text'] for post in temp_posts['items']])
        temp_lst = [Preprocessing.preprocessing_text(text, 'russian') for text in text_posts if text != '']
        temp_lst = [Lemmatization.using_mystem(text) for text in temp_lst if text !='']
        if temp_lst:
            main_list.append([category, hashtag, temp_lst])
        print(f"{i}/{len(hashtags)}.{hashtag} done")
        i+=1
    #
    # # Сброс ограничений на количество выводимых рядов
    # pd.set_option('display.max_rows', None)
    # # Сброс ограничений на число столбцов
    # pd.set_option('display.max_columns', None)
    # # Сброс ограничений на количество символов в записи
    # pd.set_option('display.max_colwidth', None)
    #
    df = pd.DataFrame(main_list, columns=['category', 'hashtag', 'list_of_words'])
    return df


def write_into_json_and_csv(data_frame: pd.DataFrame, file_name='data'):
    try:
        data_frame.to_csv(f"{file_name}.csv",index = False)
    except Exception as e:
        print('Что-то пошло не так с записью файла. Исключение:',e)
        return False
    return True

def find_posts(session, text: str, count: str,offset = "0"):
    return session.method('newsfeed.search', {'q': f"\"{text}\"", 'count': count,"offset":offset})


def main(nameThread: str, index_target: int):
    session = vk_api.vk_api.VkApi(token=os.environ[VAR_NAME])
    vk = session.get_api()
    with open(CATEGORIES_FILE_NAME, "r", encoding='utf-8') as file:
        categories = [cat.replace('\n', '') for cat in file.read().split(',')]
    print("Categories read: ", *categories)
    for index, category in enumerate(categories):
        if index == index_target:
            print(f"{nameThread} : {index+1}/{len(categories)}.Категория: {category.capitalize()}")
            df = create_dataframe_from_categories(session,category)
            if df.shape[0]!=0:
                write_into_json_and_csv(df, f'category_{index}')


#Тестовая функция
# def function(session):
#     var = input('Введите текст:')
#     a = session.method('newsfeed.search', {'q': f"\"{var}\"", 'count': "3"})
#     words = [p.using_mystem(a['items'][i]['text']) for i in range(3)]
#     for i in words:
#         print(i)
#     norm_words = [words[i][:3] for i in range(len(words))]
#     print(norm_words)
#TODO: Многопоток сделан на скорую руку
if __name__ == '__main__':

    targets = [15,16,18]
    for target in targets:
        thread_name = f'Поток {target}'
        t = threading.Thread(target = main, args=(thread_name, target))
        t.start()


