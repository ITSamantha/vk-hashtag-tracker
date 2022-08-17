import vk_api
import vk as VK
import os
import TextProcessing.Processing as p

VAR_NAME = "VK_Hashtag_Tracker"

#Тестовая функция сбора с json
def test_function(session,TEXT = 'супер папа'):
    posts = session.method('newsfeed.search', {'q': f"\"{TEXT}\"", 'count': "3"})
    words = [p.using_mystem(posts['items'][i]['text']) for i in range(3)]
    norm_words = [[word[0] for word in words[i][:10] if word[0].isalpha() and len(word)<=3] for i in range(len(words)) ]
    print(norm_words)

def main():
    session = vk_api.vk_api.VkApi(token=os.environ[VAR_NAME])
    vk = session.get_api()
    tools = vk_api.VkTools(session)
    test_function(session)


#Тестовая функция
def function(session):
    var = input('Введите текст:')
    a = session.method('newsfeed.search', {'q': f"\"{var}\"", 'count': "3"})
    words = [p.using_mystem(a['items'][i]['text']) for i in range(3)]
    for i in words:
        print(i)
    norm_words = [words[i][:3] for i in range(len(words))]
    print(norm_words)








    #wall = tools.get_all('account.getProfileInfo', 1, {'owner_id': 158559805})1

    # upload = vk_api.VkUpload(session)
    #
    # photo = upload.photo('C:\\Users\\diana\\Desktop\\Другое\\как.jpg')
    #
    # vk_photo_url = 'https://vk.com/photo{}_{}'.format(
    #     photo[0]['owner_id'], photo[0]['id']
    # )

    # print(photo, '\nLink: ', vk_photo_url)

    # print('Posts count:', wall['count'])
    #
    # if wall['count']:
    #     print('First post:', wall['items'][0], '\n')
    #
    # if wall['count'] > 1:
    #     print('Last post:', wall['items'][-1])






if __name__ == '__main__':
    main()

