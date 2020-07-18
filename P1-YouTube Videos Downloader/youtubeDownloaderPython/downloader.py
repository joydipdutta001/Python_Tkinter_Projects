from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
# yo  = yt("https://www.youtube.com/watch?v=2wVEFhjUQZ4&list=PL0_zW7OYSBkrITvXwqwfunI2Oj6CrW71k&index=31&t=0s")
#

font = ('vardana',20)
file_size= 0

# onComplete
def completeDownload(stream=None,file_path=None):
    showinfo("Message", "File has been downloaded")
    btn['text']="Download Video"
    btn['state']= 'active'
    urlInput.delete(0,END)

# onProgress
def progressDownload(stream=None,chunk=None,bytes_remaining=None):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    btn['text'] = "{:00.0f}%completed".format(percent)


def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return
    try:
        yt = YouTube(url)
        st = yt.streams.first()

        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)

        file_size = st.filesize
        st.download(output_path=path_to_save)

    except Exception as e:
        print(e)

def btnClicked():
    try:
        btn['text']="Please wait..."
        btn['state']= 'disabled'
        url = urlInput.get()
        if url == '':
            return
        thread =Thread(target=startDownload,args=(url,))
        thread.start()
    except Exception as e:
        print(e)
# GUi Code
root = Tk()
root.title("Youtube Downloader")
root.iconbitmap("res/cyboicon.ico")
root.geometry("720x720")

# image section

img = PhotoImage(file="res/cobolarge.png")
headingImg = Label(root, image=img)
headingImg.pack(side="top",pady='3')

# making input field
urlInput= Entry(root,font=font,justify=CENTER)
urlInput.pack(side="top",fill='x',padx='10')
urlInput.focus()
# Download Button
btn = Button(root, text="Download Video",font=font,relief='ridge',command=btnClicked)
btn.pack(side='top',pady=20)


root.mainloop()
