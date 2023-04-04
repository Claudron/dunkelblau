from flask import Flask, render_template, url_for 
app = Flask(__name__)


@app.route('/')
def audio():
  song_title = "Episode 1"
  audio_url = url_for('static', filename='audio/Episode1_V5.1_mix1.mp3')
  return render_template('index.html', song_title=song_title, audio_url=audio_url)

if __name__ == '__main__':
    app.run()
