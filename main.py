import os
import vk_api
import requests
from dotenv import load_dotenv
from telegram.ext import Updater

VK_GROUP_ID = 179723123


def upload_image_to_album(vk, image_path):
    album_id = 263905799
    upload = vk_api.VkUpload(vk)
    photo = upload.photo(
        photos=image_path,
        album_id=album_id,
        group_id=VK_GROUP_ID
    )
    vk_photo_url = 'photo{}_{}'.format(
        photo[0]['owner_id'], photo[0]['id']
    )
    return vk_photo_url


def post_vkontakte(image_path, message):
    vk_session = vk_api.VkApi(login=vk_login, token=vk_token, app_id=vk_app_id)
    vk = vk_session.get_api()
    photo_url = upload_image_to_album(vk, image_path)
    vk.wall.post(owner_id=VK_GROUP_ID, message=message, attachments=photo_url, access_token=vk_token)


def post_telegram(chat_id, image_path, message):
    REQUEST_KWARGS = {
        'proxy_url': 'socks5://adress',
        # Optional, if you need authentication:
        'urllib3_proxy_kwargs': {
            'username': 'login',
            'password': 'pass',
        }
    }
    updater = Updater(token=bot_token, request_kwargs=REQUEST_KWARGS)
    bot = updater.bot
    bot.send_message(chat_id=chat_id, text=message)
    bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))


def upload_image_to_fb(image_path):
    url = f'https://graph.facebook.com/{fb_group_id}/photos'
    data = {
        'access_token': fb_token
    }
    files = {"source": open(image_path, 'rb')}
    response = requests.post(url, data=data, files=files)
    return response.json().get('id')


def post_facebook(image_path, message):
    url = f'https://graph.facebook.com/{fb_group_id}/feed'
    media_id = upload_image_to_fb(image_path)
    media_attach = {"media_fbid": f"{media_id}"}
    data = {
        'message': f'{message}',
        'attached_media[0]': str(media_attach),
        'access_token': fb_token
    }
    response = requests.post(url, data=data)


if __name__ == '__main__':
    load_dotenv()
    bot_token = os.getenv('bot_token')
    vk_token = os.getenv('vk_access_token')
    vk_login = os.getenv('vk_login')
    vk_app_id = os.getenv('app_id')
    fb_token = os.getenv('fb_token')
    fb_group_id = os.getenv('fb_group_id')
    post_vkontakte('images\iceland.jpg', 'Picture from Iceland')
    post_telegram('@dev_py', 'images\iceland.jpg', 'Picture from Iceland')
    post_facebook('images\iceland.jpg', 'Picture from Iceland')
