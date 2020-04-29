from django.shortcuts import render, redirect, reverse
import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup
from datetime import timedelta, timezone, datetime
import os
import math
import shutil
from  .models import Headline, UserProfile

def news_list(request):
    user_p = UserProfile.objects.filter(user=request.user).first()
    headlines = Headline.objects.all()
    # now = datetime.now(timezone.utc)
    # time_difference = now - user_p.last_scrape
    # time_difference_in_hours = time_difference / timedelta(minutes=60)
    # next_scrape = 24 - time_difference_in_hours
    # if time_difference_in_hours <= 24:
    #     hide_me = True
    # else:
    #     hide_me = False

    context = {
        'obj_list':headlines,
        # 'hide_me': hide_me,
        # 'next_scrape': math.ceil(next_scrape)
    }
    return render(request, "home.html", context)

def scrape(request):

    user_p = UserProfile.objects.filter(user=request.user).first()

    if user_p is not None:
        user_p.last_scrape = datetime.now(timezone.utc)
        user_p.save()

    session = requests.Session()
    # session.headers = {"Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"}
    url = "https://www.theonion.com/"
    content = session.get(url, verify=False).content
    soup = BeautifulSoup(content, "html.parser")
    posts = soup.find_all('article', {'class': 'js_post_item'})

    for i in posts :
        title = i.findAll('h4', {'class': "sc-1qoge05-0"})[0]
        link = i.find('a')['href']
        print(title.text)
        print(link)

        try:
            img_src = i.find('img')['srcset'].split(' ')
            print(img_src[0])
            # create image file and object
            media_root = 'D:/code/python/tutorial/dashboard_jd/media_root'

            lf = img_src[0].split('/')[-1].split("?")[0]

            r = session.get(img_src[0], stream=True, verify=False)

            with open(lf, 'wb') as f:
                for chunk in r.iter_content(chunk_size=(1024)):
                    f.write(chunk)

            img_abs_path = os.path.abspath(lf)
            shutil.move(img_abs_path, media_root)
            new_headline = Headline()

            new_headline.title = title.text
            new_headline.url = link
            new_headline.image = lf
            new_headline.save()

        except:
            pass
    return redirect(reverse('home'))

    # print(columns[4].text)
    # print(len(columns))

    # url = "https://www.theonion.com/"
    # page = requests.get(url)
    # soup = BeautifulSoup(page.content, "html.parser")
    # columns = soup.find_all('h4', attrs={'class' : 'sc-1qoge05-0'})
    # print(columns)
