import tweepy
import re
from translate import translate_text

from init import initial
API = initial()
tweets = []

pages = [1, 2, 3, 4]
fn = ["。", "?", "、、、", ":", "？", "!", "！", "...", "笑"]
for p in pages:
    results = API.user_timeline(screen_name="D_kazuyan", exclude_replies=True, include_rts=False, count=200, page=p)
    for r in results:
        if not r.retweeted:
            text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", r.text)
            text=re.sub('RT', "", text)
            text=re.sub('┃━━━━━━━━━━━━━┃', "", text)
            text=re.sub('お気に入り', "", text)
            text=re.sub('会食恐怖症', "", text)
            text=re.sub('質問箱', "", text)
            text=re.sub(r'(#[^\s]+)', "", text)#ハッシュタグ
            text=re.sub(r"@([A-Za-z0-9_]+)", "", text)#メンション
            text=re.sub(r'[︰-＠]', "", text)#全角記号
            text=re.sub('\n', "", text)#改行文字
            if text and text[-1] not in fn:
                text += "。"
            tweets.append(text)
        # tweets.append(translate_text(text))
line = "".join(tweets)
line += translate_text(line)
# print(line)
with open("tweet.txt", "wt", encoding="UTF-8") as f:
    f.write(line)
# print(tweets)
# for page in pages:
#     results = api.user_timeline(screen_name="D_kazuyan", count=200)
# print("Hello world")