from flask import Flask , make_response , request , jsonify
from flask_mongoengine import MongoEngine
import collections
# from dotenv import load_dotenv, find_dotenv
import os

app = Flask(__name__)
# load_dotenv(find_dotenv())
# password = os.environ.get("MONGODB")
# conn_str = f"mongodb+srv://pelvic:{password}@cluster0.zst9xg2.mongodb.net/Online_News?retryWrites=true&w=majority"
conn_str = f"mongodb+srv://pelvic:Pelvic4ever@cluster0.zst9xg2.mongodb.net/Online_News?retryWrites=true&w=majority"
app.config['MONGODB_HOST'] = conn_str

db = MongoEngine()
db.init_app(app)

class News(db.Document):
    Headlines = db.StringField()
    Links = db.StringField()
    Story = db.StringField()

    meta = {
        "indexes": [
            {
                'fields': ['$Headlines'],
                'default_language': 'english'
            }
        ]
    }

    def to_json(self):
        return {
            'Headlines' : self.Headlines,
            'Links' : self.Links,
            'Story' : self.Story


        }


@app.route('/')
def api_search():
    if request.method == 'GET':
        print(request.method)
        D_News = []
        for news in News.objects:
            D_News.append(news)
        return make_response(jsonify(D_News), 200)

@app.route('/find')
def specificbook():
    if request.method == 'GET':
        tags = request.args.get('keyword')
        news_obj = News.objects.search_text(tags).first()
        if news_obj:
            return make_response(jsonify(news_obj.to_json()), 200)
        else:
            return make_response('Not found', 404)




    # if D_News:
    #     return make_response(jsonify(D_News.to_json(), 200))
    # else:
    #     return make_response('', 404)


if __name__ == '__main__':
    app.run()




