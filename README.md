# Comics publisher

This script add posts with photo to 3 services(vkontakte, facebook and telegram)

### How to install

1. You need to [create VK App](https://vk.com/apps?act=manage). Choose Standalone type of app.
2. Get access token using [Implicit flow](https://vk.com/dev/implicit_flow_user). In scope parameter use: photos,groups,wall,offline
3. Register telegram bot. This link helps you -> [How to register telegram bot](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/).
4. Get Facebook token(user-token) on [here](https://developers.facebook.com/tools/explorer/)
5. Create .env file and add:
 * bot_token=<bot_token>
 * vk_token=<vk_access_token>
 * vk_login=<vk_login>
 * vk_app_id=<app_id>
 * fb_token=<fb_token>
 * fb_group_id=<fb_group_id><br/>
To find chat_id , write message to telegram bot @userinfobot.<br/>
For telegram bot you need chat_id, you find it in telegram chanel info(like this https://t.me/chat_id)
5. Install dependencies (written below)

Note: This script using SOCKS5 Proxy, because from Russia access to telegram is blocked.
#### Proxy settings
[You can buy proxies here](https://proxy6.net)
```
    request_kwargs = {
        'proxy_url': 'socks5://proxy_adress',
        # Optional, if you need authentication:
        'urllib3_proxy_kwargs': {
            'username': 'username',
            'password': 'password',
        }
    }
```
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Program output example
```
python main.py
```
Posts will appear in 3 services

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).