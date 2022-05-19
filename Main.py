from tkinter import *
from tkinter import ttk, filedialog
from moviepy.editor import *
import tkinter as tk
import requests


win = Tk()
win.geometry("700x350")
filepath = None
name = None
picture = None

inputtxt = tk.Text(win, height=3, width=30)
picture = tk.Text(win, height=4, width=30)


def open_file():
    global filepath
    file = filedialog.askopenfile(mode='r', filetypes=[('MKV', '*.MKV')])
    if file:
        filepath = os.path.abspath(file.name)
        Label(win, text="The File is located at : " + str(filepath), font='Aerial 11').pack()


def mixcloud_Img():
    Picture = filedialog.askopenfile(mode='r', filetypes=[('png', '*.PNG')])
    if Picture:
        Picture = os.path.abspath(Picture.name)
        Label(win, text="The Picture is located at : " + str(Picture), font='Aerial 11').pack()


def mixcloud():
    Title = inputtxt.get("1.0", "end-1c")
    postUrl = ("https://api.mixcloud.com/upload/?access_token=u8PRPGyz9dGyBrbFFcPRX8MHDVSGDuqU")
    files = {'mp3': open('C:/Users/Keith/Documents/GitHub/Auto_Audio_Uploader/name' + '.mp3', 'rb'), }
    data = {
        'name': f'{Title}',
        'tags-0-tag': 'EDM',
        'description':'Socials Mixcloud: https://www.mixcloud.com/Lovles/ Twitch: https://twitch.tv/loveless_fur (Stream Weekly on Wednesdays) Twitter: https://twitter.com/DJLovles',
        'picture': f'{picture}',
    }
    r = requests.post(postUrl, files=files, data=data)


def upload():
    global filepath
    global name
    video = VideoFileClip(filepath)
    video.audio.write_audiofile('name.mp3')
    os.system(f' python upload_video.py --file="{filepath}" --title="{name}" '
              '--description="Socials Mixcloud: https://www.mixcloud.com/Lovles/ Twitch: '
              'https://twitch.tv/loveless_fur (Stream Weekly on Wednesdays) Twitter: https://twitter.com/DJLovles '
              '---Tracklist--- " --keywords="Music EDM" --category="10" '
              '--privacyStatus="public"')
    mixcloud()


Label(win, text="Click the Button to browse the Files", font='Georgia 13').pack()
ttk.Button(win, text="Browse", command=open_file).pack(pady=20)
ttk.Button(win, text="Picture", command=mixcloud_Img).pack(pady=20)
ttk.Button(win, text="Upload", command=upload, ).pack(pady=20)

inputtxt.pack()
win.mainloop()
