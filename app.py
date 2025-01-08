from flask import Flask, render_template, request
import json

app = Flask(__name__)

def load_media_data():
  
    with open('data.txt', 'r') as file:
        return json.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    genre = request.form.get('genre')
    search_query = request.args.get('search', '').lower()

   
    media = load_media_data()

    if genre:
        f_media = [item for item in media if item['genre'] == genre]
    elif search_query:
        f_media = [item for item in media if search_query in item['title'].lower()]
    else:
        f_media = media
    
    genres = ["Action", "Sci-Fi", "Horror"]
    
    return render_template('index.html', media=f_media, genres=genres)

@app.route('/video/<int:media_id>')
def video(media_id):
    media = load_media_data()  
    video_item = next((item for item in media if item['id'] == media_id), None)
    if video_item:
        return render_template('video.html', video=video_item)
    return "Video not found", 404

if __name__ == '__main__':
    app.run(debug=True)

