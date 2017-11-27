#final project
#instagram api

from instagram.client import InstagramAPI

api = InstagramAPI(client_id = '19a9f427686348c7b101de72738ba569', client_secret =' 9e8b768924f94e3088208d2a7723dd89')
popular_media = api.media_popular(count=100)