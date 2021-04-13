import snscrape.modules.twitter as sntwitter
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *


root=tk.Tk()

root.configure(bg="Light Blue")

root.geometry("500x300")

disglobvar="Fillertext"
def retweetyesno():
    MsgBox = tk.messagebox.askquestion ('Include Retweets','Are you sure you want to include retweets',icon = 'warning')
    if MsgBox == 'yes':
        global disglobvar
        disglobvar="yes"
    else:
        disglobvar="something"

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()


x1=tk.IntVar()
x2=tk.StringVar()
x3=tk.StringVar()
x4=tk.StringVar()
x5=tk.StringVar()
x6=tk.StringVar()
x7=tk.StringVar()

def submit():
    countvar=int(x1.get())
    wordsvar=x2.get()
    sincevar=x3.get()
    untilvar=x4.get()
    csvnamevar=x5.get()
    personvar=x6.get()
    locationvar=x7.get()
    tweetslist=[]

    params="'"+wordsvar+" from:"+personvar+" near:"+locationvar+" since:"+sincevar+" until:"+untilvar+"'"
    params=str(params)

    global disglobvar
    if disglobvar=="yes":
        params="'"+wordsvar+" from:"+personvar+" near:"+locationvar+" include:nativeretweets"+" since:"+sincevar+" until:"+untilvar+"'"
        params=str(params)
    #print(params)
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(params).get_items()):
        if i>countvar:
            break
        if (i%100==0):
            print("Progress:",i,"/",countvar)
        tweetslist.append([tweet.content, tweet.date, tweet.user.username, tweet.lang, tweet.user.location, tweet.id])
    tweetslistdataframe = pd.DataFrame(tweetslist, columns=["Tweet Content","Tweet Date","Username","Language","Location",'Tweet ID'])
    tweetslistdataframe.to_csv(csvnamevar+".csv")
    tweetslist.clear()
    del tweetslistdataframe
    #root.destroy()

count_label=tk.Label(root, text = 'How Many Tweets Would You Like?',bg="Light Blue", font = ('calibre',10,'bold'))
word_label=tk.Label(root, text = 'What Keywords do you Want?',bg="Light Blue", font = ('calibre',10,'bold'))
since_label=tk.Label(root, text = 'What is the Start Date?', bg="Light Blue",font = ('calibre',10,'bold'))
until_label=tk.Label(root, text = 'What is the End Date?', bg="Light Blue",font = ('calibre',10,'bold'))
csvname_label=tk.Label(root, text = 'What would you like the File to be Named?',bg="Light Blue", font = ('calibre',10,'bold'))
person_label=tk.Label(root, text = 'Who would you like to download Tweets from?',bg="Light Blue", font = ('calibre',10,'bold'))
location_label=tk.Label(root, text = 'Where would you like to download Tweets from?',bg="Light Blue", font = ('calibre',10,'bold'))

count_entry = tk.Entry(root, textvariable = x1, font=('calibre',10,'normal'))
word_entry = tk.Entry(root, textvariable = x2, font=('calibre',10,'normal'))
since_entry = tk.Entry(root, textvariable = x3, font=('calibre',10,'normal'))
until_entry = tk.Entry(root, textvariable = x4, font=('calibre',10,'normal'))
csvname_entry = tk.Entry(root, textvariable = x5, font=('calibre',10,'normal'))
person_entry = tk.Entry(root, textvariable = x6, font=('calibre',10,'normal'))
location_entry = tk.Entry(root, textvariable = x7, font=('calibre',10,'normal'))

retweetbtn=tk.Button(root,text="Want Retweets?",bg="Yellow", command=retweetyesno)

sub_btn=tk.Button(root,text = 'Get Tweets', bg="Light Green", command = submit)

exitbtn=tk.Button(root, text="Exit", bg="Red", command=ExitApplication)


count_label.grid(row=0,column=0)
count_entry.grid(row=0,column=1)

word_label.grid(row=1,column=0)
word_entry.grid(row=1,column=1)

since_label.grid(row=2,column=0)
since_entry.grid(row=2,column=1)

until_label.grid(row=3,column=0)
until_entry.grid(row=3,column=1)

person_label.grid(row=4, column=0)
person_entry.grid(row=4, column=1)

location_label.grid(row=5,column=0)
location_entry.grid(row=5,column=1)

retweetbtn.grid(row=6,column=1)

csvname_label.grid(row=7,column=0)
csvname_entry.grid(row=7,column=1)

sub_btn.grid(row=8,column=1)

exitbtn.grid(row=10,column=1)

# performing an infinite loop
# for the window to display
root.mainloop()

print("Thanks for using my code! If you have any comments or questions, feel free to contact me through GitHub.")
