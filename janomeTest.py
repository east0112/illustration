from janome.tokenizer import Tokenizer
#理解せず突っ込んだライブラリ群
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#ここまで

import os
import psycopg2
import psycopg2.extras

#postgreSQL connect関数
def get_connection():
    #dsn = os.environ.get('DATABASE_URL')
    #return psycopg2.connect(dsn)
    strCon = " user=postgres dbname= LoveLive_music password= ll0630 port= 5432 host= localhost"
    return psycopg2.connect(strCon)

#wordCloud 出力関数
def create_wordcloud(text):
    fpath = "C:\Windows\Fonts\irohamaru-Regular.ttf"
    wordCloud = WordCloud(background_color="white",font_path=fpath,  width=900, height=500).generate(text)
    plt.figure(figsize=(15,12))
    plt.imshow(wordCloud)
    plt.axis("off")
    plt.show()

#postgreSQLへ接続
with get_connection() as conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute('SELECT * FROM music')
        musicRows = cur.fetchall()

#形態素解析 関数
def analysis_janome(text):
    #encText = text.encode('utf-8')
    t = Tokenizer()
    output = []
    for token in t.tokenize(strLyric):
        output.append(token.surface)
    return output

#取得データの出力
for row in musicRows:
    strLyric = row['lyric']
    create_wordcloud(" ".join(analysis_janome(strLyric)))
    #for token in t.tokenize(strLyric):
    #create_wordcloud(" ".join(t.tokenize(strLyric)).decode('utf-8'))
