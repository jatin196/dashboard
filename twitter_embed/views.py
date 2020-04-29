from django.shortcuts import render
from .models import item
# import tweepy
# from tweepy import cursor
#
#
# consumer_key='D9Uy9lN9YEBUp0XGlYfx90pYg'
# consumer_secret='rUS2OqjAOdPbImbA2DOnIxSm2rcxqyPT3D2FL7DfuKC4hRNS7J'
# access_token='740634443937763328-Gg39pz8YjRmLIxZOH1QvUeRmkNeRSC7'
# access_secret_token='t8UnulrDDrVkwucBJWwopXNYPv8HcO0eopGrov2TInFDl'
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret_token)
#
# try:
#     redirect_url = auth.get_authorization_url()
#     print(redirect_url)
# except tweepy.TweepError:
#     print('Error! Failed to get request token.')
#
# api = tweepy.API(auth)
# for friend in tweepy.Cursor(api.friends).items():
#     # Process the friend here
#     print(friend)
# # api.update_status('tweepy + oauth!')
# for status in tweepy.Cursor(api.friends_timeline).items(200):
#     # Process the status here
#     print(status)
# # public_tweets = api.home_timeline()
# # for follower in tweepy.Cursor(api.followers).items():
# #     print(follower.name)
# #     follower.follow()
# # for tweet in public_tweets:
# #     print(tweet.text)
# # user = api.get_user('jatinpopli196')
# # print(user.screen_name)
# # print(user.followers_count)
# # for friend in user.friends():
# #    print(friend.screen_name)

def video_view(request):
    videos = item.objects.all()
    print(videos[0].video)
    context = {
        'videos' : videos
    }
    return render(request, 'video_home.html', context)