from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse
import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden
from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about')),
                                                access_token=response['access_token'],
                                                v='5.103')),
                          None
                          ))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return
    data = resp.json()['response'][0]
    if data['sex']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMALE

    if data['about']:
        user.shopuserprofile.aboutMe = data['about']
    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().date().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    user.save()


# def save_profile(backend, user, response, *args, **kwargs):
#     if backend.name == 'facebook':
#         profile = user.get_profile()
#         if profile is None:
#             profile = Profile(user_id=user.id)
#         profile.gender = response.get('gender')
#         profile.link = response.get('link')
#         profile.timezone = response.get('timezone')
#         profile.save()