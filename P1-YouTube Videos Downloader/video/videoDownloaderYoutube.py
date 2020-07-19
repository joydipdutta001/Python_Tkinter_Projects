""" 
////////////////////////////////////////////////////////////////////////////////
                author_name= Joydip Dutta,
                author_email= duttajoydip98@gmail.com,
                github_id = joydipdutta001
                linkedIn_id = Joydip Dutta (JD)
                Website = cybotians.com
                
                Project_code = TIK001
                Project_Name = Youtube Video Downloader
                Project_Version = 0.1v
                Project_description=
                
                Thank You...
 ///////////////////////////////////////////////////////////////////////////////   
 """


from pytube import YouTube
from pytube import Playlist
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
from tkinter.ttk import *
from tkinter import *

playListCommand= "https://www.youtube.com/playlist"
videoCommand = "https://www.youtube.com/watch"
playListUrls = []
def playlistBoxUpdate(urlp):

    global playListUrls
    try:
        play = Playlist(urlp)
        c =len(play.video_urls)
        btn2['state'] = 'disabled'
        c2 = c

        for i in play.video_urls:
            playListUrls.append(i)
            c2 -= 1
            yt = YouTube(i)
            btn2['text'] = "Total Videos {} Remaining {}".format(c,c2)
            playlistBox.insert(END,yt.title)

        showinfo("Meassage", "List Updated")
        labelplaylistupdate.config(text="Total {} Videos in the Playlist Box".format(playlistBox.size()))
        btn2['text'] = "Import Playlist"
        btn2['state'] = 'active'
        urlInput2.delete(0, END)

    except Exception as e:
        print(e)


# onComplete
def completeDownload(stream=None,file_path=None):
    showinfo("Message", "File has been downloaded in " + path_to_save)
    btn['text']="Download Video"
    btn['state']= 'active'
    urlInput.delete(0,END)



# onProgress
def progressDownload(stream=None,chunk=None,bytes_remaining=None):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    btn['text'] = "{:00.0f}%completed".format(percent)
    barTop['value'] = percent

def progressDownload2(stream=None,chunk=None,bytes_remaining=None):
    percent = (100 * ((file_size2 - bytes_remaining) / file_size2))
    listBtn['text'] = "{:00.0f}%completed".format(percent)
    barTop['value'] = percent

def progressDownload3(stream=None,chunk=None,bytes_remaining=None):
    percent = (100 * ((file_size3 - bytes_remaining) / file_size3))
    allBtn['text'] = "{:00.0f}%completed".format(percent)
    barTop['value'] = percent




# For Single Video Download
def startDownload(url):
    global file_size,path_to_save
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


# Button to initiate the selectDownload function
def btnForSingleDownload():
    try:
        btn['text']="Please wait..."
        btn['state']= 'disabled'
        url = urlInput.get()

        cuttedUrl = url.split("?")[0]
        if url == '':
            return
        else:
            if cuttedUrl == videoCommand:
                thread =Thread(target=startDownload,args=(url,))
                thread.start()


            else:
                showinfo("Meassage","Re-enter valid link")
                btn['text'] = "Download Video"
                btn['state'] = 'active'
                urlInput.delete(0, END)
    except Exception as e:
        print(e)


# Button to Update the PlaylistBox
def btnForPlaylistUpdate():
    try:

        url2 = urlInput2.get()

        cuttedUrl2 = url2.split("?")[0]
        if url2 == '':
            return
        else:
            if cuttedUrl2 == playListCommand:
                thread = Thread(target=playlistBoxUpdate, args=(url2,))
                thread.start()


            else:
                showinfo("Meassage", "Re-enter valid link")
                btn2['text'] = "Download Video"
                btn2['state'] = 'active'
                urlInput2.delete(0, END)
    except Exception as e:
        print(e)


#  Function for Download those videos which are Selected by the user in Playlist Box
def selectDownload():
    global file_size2,total
    path_to_save1 = askdirectory()

    if path_to_save1 is None:
        return
    try:

        total = 0

        for item in playlistBox.curselection():
            total += 1
            yt1 = YouTube(playListUrls[item])
            st1 = yt1.streams.filter(progressive=True).first()

            # yt1.register_on_complete_callback(completeDownload2)
            yt1.register_on_progress_callback(progressDownload2)

            file_size2 = st1.filesize
            st1.download(output_path=path_to_save1)
            textlabel = "{} Video Done".format(total)
            labelselectedDownload.config(text=textlabel)
        showinfo("Meassage", "All Downloaded in "+path_to_save1)
        listBtn['text'] = "Download Selected"
        listBtn['state'] = 'active'


    except Exception as e:
        print(e)

# Button to initiate the selectDownload function
def btnSelectedDownload():

    try:
        listBtn['state'] = 'disabled'
        thread = Thread(target=selectDownload)
        thread.start()
    except Exception as e:
        print(e)

# Function for All Download Activity
def allDownload():
    global file_size3, total3
    path_to_save2 = askdirectory()

    if path_to_save2 is None:
        return
    try:

        total3 = 0

        for items in playListUrls:
            total3 += 1
            yt2 = YouTube(items)
            st2 = yt2.streams.filter(progressive=True).first()

            # yt2.register_on_complete_callback(completeDownload3)
            yt2.register_on_progress_callback(progressDownload3)

            file_size3 = st2.filesize
            st2.download(output_path=path_to_save2)
            textlabel2 = "{} Video Done".format(total3)
            labelselectedDownload.config(text=textlabel2)
        showinfo("Meassage", "All Downloaded in "+path_to_save2)
        allBtn['text'] = "Download All"
        allBtn['state'] = 'active'

    except Exception as e:
        print(e)


# Button to initiate the allDownload function
def btnAllDownload():
    try:
        allBtn['state'] = 'disabled'
        thread = Thread(target=allDownload)
        thread.start()
    except Exception as e:
        print(e)

# # Animation function 1

def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)


font = ('vardana bold',12)
file_size= 0

# GUi Code
root = Tk()
root.title("Youtube Downloader")
root.iconbitmap("res/cyboicon.ico")
root.geometry("720x720")

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the submenu

subMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open")
subMenu.add_command(label="Exit", command=root.destroy)


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us")



# Frames
topFrame = Frame(root)
topFrame.pack(side=TOP, padx=10, pady=10,fill=BOTH,expand=TRUE)

middleFrame = Frame(root)
middleFrame.pack(side=TOP, padx=10, pady=10,fill=BOTH,expand=TRUE)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, padx=10, pady=10,fill=BOTH,expand=TRUE)





# image section

img = PhotoImage(file="res/cobolarge.png")
headingImg = Label(topFrame, image=img)
headingImg.pack(side="top",pady='3')

# Animated Text
canvas=Canvas(topFrame,bg='white')
canvas.pack(fill=BOTH, expand=1)
text_var="!!!! Download YouTube Videos and Playlists Easily. visit cybotians.com for more Projects !!!!"
text=canvas.create_text(0,-2000,text=text_var,font=('vardana',15,'bold'),fill='red',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = x2-x1
height = y2-y1
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()

# making input field
text1="Paste your video URL here And then Click Download Button"
Label(middleFrame,text= text1,fg = "red",bg = "white",font = "vardana 10 bold").pack(side='top')

urlInput= Entry(middleFrame,font=font,justify=CENTER)
urlInput.pack(side="top",fill='x',padx='10',pady='5')
urlInput.focus()

middleFrameBottom = Frame(middleFrame)
middleFrameBottom.pack(side=TOP, padx=10, pady=10,fill=BOTH,expand=TRUE)

# Download Button
btn = Button(middleFrameBottom, text="Download Video",font=font,relief='ridge',command=btnForSingleDownload)
btn.pack(side='left',pady='2',padx=100)


# Progress Bar 2
barTop = Progressbar(middleFrameBottom,length = 100,orient = HORIZONTAL,maximum=100)
barTop.pack(side="right",padx=100)



# making input field2
text2="Paste your playlist URL here to insert the videos in Playlist Box below"
Label(middleFrame,text= text2,fg = "red",bg = "white",font = "vardana 10 bold").pack(side='top',pady='10')


urlInput2= Entry(middleFrame,font=font,justify=CENTER)
urlInput2.pack(side="top",fill='x',padx='10',pady='2')
urlInput2.focus()

# playlist update Button
btn2 = Button(middleFrame, text="Import Playlist",font=font,relief='ridge',command=btnForPlaylistUpdate)
btn2.pack(side='top',pady=5)

labelplaylistupdate = Label(middleFrame,text= "Nothing Added in The Playlist Box",fg = "black",bg = "Light Green",font = font)
labelplaylistupdate.pack(side='top',pady=5)

# PlayList Box
playlistBox = Listbox(middleFrame,selectmode=EXTENDED)
playlistBox.pack(side='top',fill='both',pady='10',padx='20',expand='1')



# Playlist Button

listBtn = Button(bottomFrame, text= "Download Selected",font=font,relief='ridge',command=btnSelectedDownload)
listBtn.pack(side='left',pady=10,padx=20)

# Download Indication
labelselectedDownload = Label(bottomFrame,text= "Nothing Downloaded yet",fg = "black",bg = "Light Green",font = font)
labelselectedDownload.pack(side='left',pady=5,padx=20)
# Progress Bars

barBottom = Progressbar(bottomFrame,length = 100,orient = HORIZONTAL,maximum=100)
barBottom.pack(side='left',padx=20)

allBtn = Button(bottomFrame, text= "Download All",font=font,relief='ridge',command=btnAllDownload)
allBtn.pack(side='right',pady=10,padx=20)
root.mainloop()


