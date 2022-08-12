import vk_api
import vk as VK
import os

VAR_NAME = "VK_Hashtag_Tracker"

def main():
    session = vk_api.vk_api.VkApi(token=os.environ[VAR_NAME])
    vk = session.get_api()
    tools = vk_api.VkTools(session)
    a = session.method('newsfeed.search',{'q':'#fcb','count':100})
    c=0
    for i in a['items']:
        print(c, i['text'], end='\n\n')
        c+=1




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

