import time
import os
import json
from htmlparser import MyHTMLParser


for tag in ['INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP', 'ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'INFJ', 'INFP', 'ESTP']:
  ts=2612
  curl_str = "curl 'https://twitter.com/i/search/timeline?f=tweets&vertical=default&q=%23" + tag + "%20lang%3Aar&src=typd&include_available_features=1&include_entities=1&last_note_ts=2516&max_position=TWEET-711340624943906817-718124708412203008-BD1UO2FFu9QAAAAAAAAETAAAAAcAAAASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&reset_error_state=false' -H 'accept-encoding: gzip, deflate, sdch' -H 'x-requested-with: XMLHttpRequest' -H 'accept-language: en-US,en;q=0.8' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36' -H 'accept: application/json, text/javascript, */*; q=0.01' -H 'referer: https://twitter.com/search?f=tweets&vertical=default&q=%23ISFP%20lang%3Aar&src=typd' -H 'authority: twitter.com' -H 'cookie: guest_id=v1%3A143863298058930111; mp_c3de24deb6a3f73fba73a616bb625130_mixpanel=%7B%22distinct_id%22%3A%20%227851b24a2bf2c7756fe7a387d4a02f3c71ef869d436e1e29099f9a08eefb812c%22%2C%22isAdmin%22%3A%20false%2C%22isAccountSpending%22%3A%20false%2C%22serviceLevel%22%3A%20%22null%22%2C%22goalBased%22%3A%20true%7D; eu_cn=1; kdt=6CB6J5Euwi4vSd6f87cx1xUNoW5QFzRSRJalTKFv; remember_checked_on=1; auth_token=43da469332b0c6afff154a20904cf4b538412d9b; pid=\"v3:1458750681895591692855842\"; __utma=43838368.234037132.1438633240.1459465162.1459465162.1; __utmz=43838368.1459465162.1.1.utmcsr=t.co|utmccn=(referral)|utmcmd=referral|utmcct=/Hs5aCk1uqi; lang=en; twitter_ads_id=v1_716178566988214277; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0; _ga=GA1.2.234037132.1438633240; _gat=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJXH09NTAToMY3NyZl9p%250AZCIlNWIxYjdjZjJjY2FmMGQ3Yzc0ZDE4MmNlMmU1OTA1ODE6B2lkIiVkOGIz%250AY2UwNWVjMTczYzUxMzUwYzc5ZGEzMTU2YmI4Yg%253D%253D--516ce1de0aff3a3c1e0181febb7482f25f4aa224; ua=\"f5,m2,m5,rweb,msw\"' --compressed -o a.txt"
  os.system(curl_str)
  c = 0
  while True:
    c += 1
    with open('a.txt') as f:
      out = json.loads(f.read())
      last = out["inner"]["min_position"]
      html = out["inner"]["items_html"]
      if len(html.replace('\n', '')) == 0 or c > 1000:
        break
      #print html
      with open(tag+'.txt', 'ab') as file:
        parser = MyHTMLParser(file)
        parser.feed(html)
      ts += 1
      next_curl_str = "curl 'https://twitter.com/i/search/timeline?f=tweets&vertical=default&q=%23ISFP%20lang%3Aar&src=typd&include_available_features=1&include_entities=1&last_note_ts="+str(ts)+"&max_position="+last+"&reset_error_state=false' -H 'accept-encoding: gzip, deflate, sdch' -H 'x-requested-with: XMLHttpRequest' -H 'accept-language: en-US,en;q=0.8' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36' -H 'accept: application/json, text/javascript, */*; q=0.01' -H 'referer: https://twitter.com/search?f=tweets&vertical=default&q=%23ISFP%20lang%3Aar&src=typd' -H 'authority: twitter.com' -H 'cookie: guest_id=v1%3A143863298058930111; mp_c3de24deb6a3f73fba73a616bb625130_mixpanel=%7B%22distinct_id%22%3A%20%227851b24a2bf2c7756fe7a387d4a02f3c71ef869d436e1e29099f9a08eefb812c%22%2C%22isAdmin%22%3A%20false%2C%22isAccountSpending%22%3A%20false%2C%22serviceLevel%22%3A%20%22null%22%2C%22goalBased%22%3A%20true%7D; eu_cn=1; kdt=6CB6J5Euwi4vSd6f87cx1xUNoW5QFzRSRJalTKFv; remember_checked_on=1; auth_token=43da469332b0c6afff154a20904cf4b538412d9b; pid=\"v3:1458750681895591692855842\"; __utma=43838368.234037132.1438633240.1459465162.1459465162.1; __utmz=43838368.1459465162.1.1.utmcsr=t.co|utmccn=(referral)|utmcmd=referral|utmcct=/Hs5aCk1uqi; lang=en; twitter_ads_id=v1_716178566988214277; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0; _ga=GA1.2.234037132.1438633240; _gat=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJXH09NTAToMY3NyZl9p%250AZCIlNWIxYjdjZjJjY2FmMGQ3Yzc0ZDE4MmNlMmU1OTA1ODE6B2lkIiVkOGIz%250AY2UwNWVjMTczYzUxMzUwYzc5ZGEzMTU2YmI4Yg%253D%253D--516ce1de0aff3a3c1e0181febb7482f25f4aa224; ua=\"f5,m2,m5,rweb,msw\"' --compressed -o a.txt"
      os.system(next_curl_str)
      time.sleep(1)
      

