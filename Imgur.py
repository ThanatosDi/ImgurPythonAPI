import requests
import json


class Imgur(object):
    API = 'https://api.imgur.com/'

    def __init__(self, client_id, client_secret, refresh_token=None, state='API'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.access_token = None
        self.state = state

    def make_request(self, method, endpoint, data=None, headers=None):
        resp = requests.request(
            method.upper(), self.API+endpoint, headers=headers, data=data)

        if resp.status_code != 200:
            raise ImgurClientError('Get response error',
                                   status_code=resp.status_code)
        return json.loads(resp.text)

    def Get_token(self):
        response_type = 'token'
        client_id = self.client_id
        state = self.state
        endpoint = f'oauth2/authorize?client_id={client_id}&response_type={response_type}&state={state}'
        return print(self.API+endpoint)

    def Refresh_token(self):
        """ Given a user's refresh token """
        if self.refresh_token is None:
            raise ImugrClientMissRefreshToken
        endpoint = 'oauth2/token/'
        params = {"client_id": self.client_id,
                  "client_secret": self.client_secret,
                  "grant_type": "refresh_token",
                  "refresh_token": self.refresh_token
                  }
        resp = self.make_request('POST', endpoint, data=params)
        self.access_token = resp['access_token']
        self.refresh_token = resp['refresh_token']
        return resp
# Account

    def Account(self, username):
        """Request standard user information."""
        endpoint = f'3/account/{username}'
        header = {
            'Authorization': f'Client-ID {self.client_id}'
        }
        resp = self.make_request('GET', endpoint, headers=header)
        return resp['data']

    def Account_Block_Status(self, username):
        return self.Account(username)['is_blocked']

    def Account_Block(self, username):
        """List all accounts being blocked"""
        endpoint = f'3/account/{username}/block'
        if self.access_token is None:
            self.Refresh_token()
        header = {
            'Authorization': f"Bearer {self.access_token}",
            'Accept': "application/vnd.api+json"
        }
        resp = self.make_request('GET', endpoint, headers=header)
        return resp['data']

    def Account_Block_Create(self, username):
        """Block a user."""
        endpoint = f'account/v1/{username}/block'
        if self.access_token is None:
            self.Refresh_token()
        header = {
            'Authorization': f"Bearer {self.access_token}",
            'Accept': "application/vnd.api+json"
        }
        resp = self.make_request('POST', endpoint, headers=header)
        return resp['data']

    def Account_Block_Delete(self, username):
        """ Unblock a user. """
        endpoint = f'account/v1/{username}/block'
        if self.access_token is None:
            self.Refresh_token()
        header = {
            'Authorization': f"Bearer {self.access_token}",
            'Accept': "application/vnd.api+json"
        }
        resp = self.make_request('DELETE', endpoint, headers=header)
        return resp['data']

    def Account_Images(self):
        """Get request all the images for the account that is currently authenticated. """
        endpoint = '3/account/me/images'
        if self.access_token is None:
            self.Refresh_token()
        header = {
            'Authorization': f"Bearer {self.access_token}"
        }
        resp = self.make_request('GET', endpoint, headers=header)
        return resp['data']

    def Account_Gallery_Favorites(self, username, page:int=None, favoritesSort:str='newest'):
        """Return the images the user has favorited in the gallery.\n
        (optional)\n
        page            : integer - allows you to set the page number so you don't have to retrieve all the data at once.\n
        favoriteSort    : oldest, or newest. Defaults to newest"""
        endpoint = f'3/account/{username}/gallery_favorites/{page}/{favoritesSort}'
        header = {
            'Authorization': f'Client-ID {self.client_id}'
        }
        resp = self.make_request('GET', endpoint, headers=header)
        return resp['data']
        
# Album
    def Album(self, album_id):
        """Get additional information about an album."""
        endpoint = f'3/album/{album_id}'
        header = {
            'Authorization': f'Client-ID {self.client_id}'
        }
        resp = self.make_request('GET', endpoint, headers=header)
        return resp['data']

    def Album_Images(self, album_id):
        """Return all of the images in the album."""
        endpoint = f'3/album/{album_id}/images'
        header = {
            'Authorization': f'Client-ID {self.client_id}'
        }
        resp = self.make_request('GET', endpoint, headers=header)
        return resp['data']

    def Album_Images_Detail(self, album_id, image_id):
        """Get information about an image in an album"""
        endpoint = f'3/album/{album_id}/image/{image_id}'
        header = {
            'Authorization': f'Client-ID {self.client_id}'
        }
        resp = self.make_request('GET', endpoint, headers=header)
        return resp['data']

# Image
    def Image_Upload(self, image, auth=False, **keyargs):
        """Upload a new image.\n
If non-authorization "auth" set "False".\n
If image is "file" first use binaryfile convert to binary.\n (optional)
    album       : The id of the album you want to add the image to. For anonymous albums, album should be the deletehash that is returned at creation.\n
    type        : The type of the file that's being sent; file, base64 or URL.\n
    name        : The name of the file, this is automatically detected if uploading a file with a POST and multipart / form-data\n
    title       : The title of the image.\n
    description : The description of the image."""
        allow_key = ['album', 'type', 'name', 'title', 'description']
        error_key = [key for key in keyargs.keys() if key not in allow_key]
        if error_key:
            raise ImgurClientParameterKeyNotFound(', '.join(error_key))
        endpoint = '3/image'
        Authorization = f'Client-ID {self.client_id}'
        if auth:
            self.Refresh_token()
            Authorization = f'Bearer {self.access_token}'
        header = {
            'Authorization': Authorization
        }
        params = keyargs
        params['image'] = image
        resp = self.make_request(
            'POST', endpoint, headers=header, data=params)
        return resp['data']

    def Image_Delete(self, image_id):
        """Deletes an image. Need to authorization"""
        endpoint = f'3/image/{image_id}'
        self.Refresh_token()
        header = {
            'Authorization': f'Bearer {self.access_token}'
        }
        resp = self.make_request('DELETE', endpoint, headers=header)
        return resp

    def Image_Delete_AM(self, image_deletehash):
        """Deletes an image. Un-authorization, but need image's deletehash."""
        endpoint = f'3/image/{image_deletehash}'
        header = {
            'Authorization': f'Client-ID {self.client_id}'
        }
        resp = self.make_request('DELETE', endpoint, headers=header)
        return resp

    @staticmethod
    def binaryfile(file):
        with open(file, 'rb') as file:
            fileContent = file.read()
        return fileContent

# Error


class ImgurClientError(Exception):
    def __init__(self, error_message, status_code=None):
        self.status_code = status_code
        self.error_message = error_message

    def __str__(self):
        if self.status_code:
            return "(%s) %s" % (self.status_code, self.error_message)
        else:
            return self.error_message


class ImgurClientRateLimitError(Exception):
    def __str__(self):
        return 'Rate-limit exceeded!'


class ImugrClientMissRefreshToken(Exception):
    def __str__(self):
        return 'Miss refresh_token. Please run Get_token and open url in browser to get refresh_token.'


class ImgurClientParameterKeyNotFound(Exception):
    def __init__(self, error_keys):
        self.error_keys = error_keys

    def __str__(self):
        return f'Parameter key not found. {self.error_keys} not allow key.'
