import os
from flask import Flask, render_template
import pymysql as sql
from bs4 import BeautifulSoup

DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')
DATABASE = os.getenv('DATABASE')
SEARCH_TERM = os.getenv('SEARCH_TERM')
SQL = (f"select a.ID as id, a.post_content as content from wp_posts a left join wp_term_relationships b on a.ID=b.object_id "
       f"left join wp_term_taxonomy c on b.term_taxonomy_id=c.term_taxonomy_id left join wp_terms d on c.term_id=d.term_id "
       f"where slug = '{SEARCH_TERM}' order by rand() limit 1")

app = Flask(__name__)


@app.route('/')
@app.route('/random/')
def random():
    db = sql.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DATABASE);
    cur = db.cursor()
    cur.execute(SQL)
    row = cur.fetchone()
    bs = BeautifulSoup(row[1], 'html.parser')
    return render_template('display.html', href=bs.a['href'], src=bs.a.img['src'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
