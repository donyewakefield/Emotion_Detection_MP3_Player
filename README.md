# Emotion Detection MP3 Player Web App
Capstone project for DTSC 400 Applied Data Science course. A mp3 player that detects the users face and classifies the emotion being conveyed by the user. When the user is satisfied, a playlist associated with that emotion is fetched from a music database and played for the user.

## Languages
* `Python`
* `Javascript`
* `HTML/CSS`
## Tools and Software 
* `Visual Studio Code`
* `Google Colab`
* `pgAdmin (postgreSQL)`
* `SmartDraw` - https://www.smartdraw.com/

--- Look below for steps on running this code 


![music_pic](https://github.com/donyewakefield/emotion_detection_MP3_player/assets/71467135/55ea8599-dc76-4f97-afe2-50aa1506d12f)

# Steps to run this web app
1) Download the zip file containing the compressed form of the web app.
2) Place the downloaded zip file in a folder that you would access the web app from.
3) Within that folder, extract the web app from the zip file there in that folder.
4) Open a command prompt (cmd on Windows OS) or terminal on MacOS
5) First, you will need to make sure that you are at the correct directory to access the web app (called 'music_player'); e.g. path\to\music_player. Then while in 'music_player' directory, begin creating a virtual environment and installing all dependencies in there.
## Dependencies that you need
This Flask app requires additional dependecies on top of `Python 3.x`
### Create Virtual Environment
```
python -m venv myenv
```
### Activate that Virtual Environment
```
myenv\Scripts\activate
```
### Install all dependencies
```
pip install Flask
pip install numpy
pip install matplotlib
pip install tensorflow
pip install opencv-python
pip install psycopg2
```
7) Make sure the virtual environment is still activated; If not, Do this by typing .\myenv\Scripts\activate or source venv/bin/activate on MacOS; the cmd should look like this now: path\to\music_player>.\myenv\Scripts\activate; This results in the cmd now looking like this: (myenv) path\to\music_player>
8) Now, type in python app.py; Should look like this: (myenv) path\to\music_player>python app.py
9) While the app is setting up, this message will show up "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead." It is usually written in Red so it would be hard to miss. Under that, there is a URL link:* Running on http://127.0.0.1:5000; Highlight that link and copy it. Then paste in the search bar of the browser of your choice (e.g. google chrome)
10) Around the time when that is done, a seperate python window will show up (you will notice the python symbol at bottom of your screen); click on that icon and you will be greeted with a small window that detects your face and attempts to classify your current emotion; When satisfied with your current emotion label, do not exit out of the window, as it will only repeatedly show up again. Instead, press 'q' on the keyboard to quit out of it
11) Finally, the web page will finish loading and you will be greeted with the playlist associated with your emotion

![music_player_pic](https://github.com/donyewakefield/emotion_detection_MP3_player/assets/71467135/5c2a9e40-9ba1-447d-8a49-b662316bfdb9)
## Minor issues:
* The model has the hardest time detecting the sad emotion so sometimes exaggerated sad expressions must be made :(
* The model also has a hard time detecting accurately when there is poor lighting in the room
