import speech_recognition as sr
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

root = Tk()
root.geometry("600x400")
root.title("Speech to Text")

def translation():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = "Sorry, could not recognise your voice"
        speechBox.delete(1.0, END)
        speechBox.insert(END, text)

def saveText():
    f = asksaveasfile(defaultextension = ".txt")
    if f:
        print(speechBox.get(1.0, END), file = f)
    else:
        messagebox.showinfo("Warning", "Text not saved")

titl = Label(root, text = "Voice Notepad", font = ("Arial", 30, "bold"))
titl.pack(side = "top")

speechBox = Text(root, width = 40, height = 4)
speechBox.place(x = 130, y = 130)

recordButton = Button(root, text = "Start Recording", command = translation)
recordButton.pack(side = "left")

saveButton = Button(root, text = "Save Text", command = saveText)
saveButton.pack(side = "right")

root.mainloop()
