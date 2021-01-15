from textblob import TextBlob
from textblob.translate import NotTranslated
from time import sleep


def translate_text(comment):
    ret = ""
    if hasattr(comment, "decode"):
        comment = comment.decode("utf-8")
    text = TextBlob(comment)
    try:
        text = text.translate(to="ko")
        print(text)
        sleep(0.1)
        text = text.translate(to="ja")
        sleep(0.1)
    except NotTranslated:
        pass
    ret += str(text)
    # try:
    #     text = text.translate(to="tr")
    #     print(text)
    #     sleep(0.1)
    #     text = text.translate(to="ja")
    #     sleep(0.1)
    # except NotTranslated:
    #     pass
    # ret += str(text)
    return str(ret)