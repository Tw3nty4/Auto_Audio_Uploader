# Import the required Libraries
import tkinter
from tkinter import *
from tkinter import ttk, filedialog
from moviepy.editor import *
from aiomixcloud import Mixcloud
from aiomixcloud.auth import MixcloudOAuth

win = Tk()
win.geometry("700x350")


def open_file():
    global filepath
    file = filedialog.askopenfile(mode='r', filetypes=[('MKV', '*.MKV')])
    if file:
        filepath = os.path.abspath(file.name)
        Label(win, text="The File is located at : " + str(filepath), font=('Aerial 11')).pack()


# Add a Label widget
label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)
#inputtxt = Text(win, height=5, width=25)


def upload():
    #input = inputtxt.get("1.0", "end-1c")
    video = VideoFileClip(filepath)
    video.audio.write_audiofile('.mp3')
    #os.system('python upload_video.py --file="{filepath}" --title="Summer vacation in California" --description="Had fun surfing in Santa Cruz" --keywords="surfing,Santa Cruz" --category="22" --privacyStatus="private"')


ttk.Button(win, text="Browse", command=open_file).pack(pady=20)
ttk.Button(win, text="Upload", command=upload).pack(pady=20)
#inputtxt.pack()
win.mainloop()
