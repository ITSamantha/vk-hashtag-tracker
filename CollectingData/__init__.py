import os
import pandas as pd
import re
import vk_api

import TextProcessing
import TextProcessing.Lemmatization as p
from TextProcessing import Lemmatization, Preprocessing

VAR_NAME = "VK_Hashtag_Tracker"

CATEGORIES_FILE_NAME = "categories.txt"


# Возвращает DataFrame
def create_dataframe_from_categories(session, posts_count="1", posts_for_hashtag_count="2"):
    """
    Функция создает DataFrame для списка категорий из файла.
    Колонки DataFrame: ['category','hashtag','list_of_words']
    """
    with open(CATEGORIES_FILE_NAME, "r", encoding='utf-8') as file:
        categories = [cat.replace('\n', '') for cat in file.read().split(',')]
    print("Categories read: ", *categories)
    # df = pd.DataFrame()
    main_list = list()
    for category in categories:
        if category=='искусство':
            break
        print(category + "\n")
        posts = find_posts(session, text=f"#{category}", count=posts_count)
        hashtags = list()
        for post in posts['items']:
            temp = [word.lower() for word in post['text'].split() if
                    re.fullmatch(r'\#[a-zA-ZёЁА-Яа-я\_\-0-9]+', word.lower())]
            hashtags.extend(temp)
        hashtags = set(hashtags)
        print(hashtags, len(hashtags))
        for hashtag in hashtags:
            temp_posts = find_posts(session, text=f"{hashtag}", count=posts_for_hashtag_count)#TODO:исправить повторение текстов для разных хэштегов
            text_posts = set([post['text'] for post in temp_posts['items']])
            # temp_lst = [[word for word in Lemmatization.using_mystem(Preprocessing.preprocessing_text(text, 'russian'))
            #              if re.fullmatch(r'[a-zA-ZёЁА-Яа-я\_\-0-9]+', word)]
            #             for text in text_posts]
            temp_lst = [Lemmatization.using_mystem(Preprocessing.preprocessing_text(text, 'russian'))
                        for text in text_posts]
            main_list.append([category, hashtag, temp_lst])
            print(hashtag + " done")




    # Сброс ограничений на количество выводимых рядов
    pd.set_option('display.max_rows', None)
    # Сброс ограничений на число столбцов
    pd.set_option('display.max_columns', None)
    # Сброс ограничений на количество символов в записи
    pd.set_option('display.max_colwidth', None)

    #print(TextProcessing.Vectorizing.using_TF_IDF([main_list[i][2][0] for i in range(len(main_list))]))

    df = pd.DataFrame(main_list, columns=['category', 'hashtag', 'list_of_words'])
    print(df)
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


def main():
    session = vk_api.vk_api.VkApi(token=os.environ[VAR_NAME])
    vk = session.get_api()
    df = create_dataframe_from_categories(session)
    write_into_json_and_csv(df)


#Тестовая функция
# def function(session):
#     var = input('Введите текст:')
#     a = session.method('newsfeed.search', {'q': f"\"{var}\"", 'count': "3"})
#     words = [p.using_mystem(a['items'][i]['text']) for i in range(3)]
#     for i in words:
#         print(i)
#     norm_words = [words[i][:3] for i in range(len(words))]
#     print(norm_words)


if __name__ == '__main__':
    main()
