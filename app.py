from flask import Flask, send_file
from flask import render_template
from db_connect import fetch_data
from face_detection import capture_expr

app = Flask(__name__)

@app.route('/')
def main_page():
    emotion = capture_expr()
    records = fetch_data(emotion)
    song1 = records[0]; song2 = records[1]; song3 = records[2]
    return render_template("structure.html", title1=song1[0], artist1=song1[1], song_path1=song1[2], img_path1=song1[3], background_img=song1[4],
                           title2=song2[0], artist2=song2[1], song_path2=song2[2], img_path2=song2[3],
                           title3=song3[0], artist3=song3[1], song_path3=song3[2], img_path3=song3[3])

if __name__ == '__main__':
    app.run(debug=True)






