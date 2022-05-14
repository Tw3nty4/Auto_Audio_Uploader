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


def open_file():
    global filepath
    file = filedialog.askopenfile(mode='r', filetypes=[('MKV', '*.MKV')])
    if file:
        filepath = os.path.abspath(file.name)
        Label(win, text="The File is located at : " + str(filepath), font='Aerial 11').pack()
        # picture = filedialog.askopenfile(mode='r', filetypes=[('png', '*.PNG')])
        # if picture:
        # filepath = os.path.abspath(picture.name)
        # Label(win, text="The File is located at : " + str(picture), font='Aerial 11').pack()


label = Label(win, text="Click the Button to browse the Files", font='Georgia 13')
inputtxt = tk.Text(win, height=3, width=30)


# picture = tk.Text(win, height=4, width=30)


def mixcloud():
    Title = inputtxt.get("1.0", "end-1c")
    postUrl = ("https://api.mixcloud.com/upload/?access_token=u8PRPGyz9dGyBrbFFcPRX8MHDVSGDuqU")
    files = {'mp3': open('C:/Users/Keith/Documents/GitHub/Auto_Audio_Uploader/name' + '.mp3', 'rb'), }
    data = {
        'name': f'{Title}',
        'tags-0-tag': 'EDM',
        'description': '',
        'picture': f'{picture}',
    }
    r = requests.post(postUrl, files=files, data=data)


def upload():
    global filepath
    global name
    video = VideoFileClip(filepath)
    video.audio.write_audiofile('name.mp3')
    # os.system(f' python upload_video.py --file="{filepath}" --title="{name}" '
    # '--description=" " --keywords="surfing,Santa Cruz" --category="22" '
    # '--privacyStatus="private"')
    mixcloud()


ttk.Button(win, text="Browse", command=open_file).pack(pady=20)
ttk.Button(win, text="Upload", command=upload).pack(pady=20)
# ttk.Button(win, text="Picture", command=upload).pack(pady=20)
inputtxt.pack()
win.mainloop()
label.pack(pady=10)
