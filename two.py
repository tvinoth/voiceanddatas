import speech_recognition as sr
from time import ctime
import time
import os
import sys
from gtts import gTTS
import webbrowser
from io import StringIO
import xlsxwriter
import mysql.connector

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    #os.system("mpg321 audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
    	print("Say something!")
    mydb    =   mysql.connector.connect(host="localhost",user="root",passwd="P@ssword_001",database="test")

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM auth_permission")

    myresult = mycursor.fetchall()
    audio = r.listen(source)
        # print(audio)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):
    data    =   data.lower()
    if "how are you" in data:
        speak("I am fine")

    if "hi" in data:
        speak("hello")
    
    if "open youtube" in data:
        webbrowser.open('https://youtube.com')
    
    if "open facebook" in data:
        webbrowser.open('https://facebook.com')
    
    if "open google" in data:
        webbrowser.open('https://google.com')    

    if "hi chennai how are you" in data:
        speak("hmmm fine what about you")

    if "where i am" in data:
        speak("chennai")

    if "hello" in data:
        speak("hi")
    
    if "bye" in data:
        speak("okay bye")
        sys.exit()

    if "what time is it" in data:
        speak(ctime())

    if "excel" in data:
        
        workbook = xlsxwriter.Workbook('hello.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.write('A1', 'Hello world')

        workbook.close()
    
    if "excel" in data:
        
        workbook = xlsxwriter.Workbook('hello.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.write('A1', 'Hello world')

        workbook.close()
    
    if "xl" in data:
        
        workbook = xlsxwriter.Workbook('hello.xlsx')
        worksheet = workbook.add_worksheet()
        title = workbook.add_format({
            'bold': True,
            'font_size': 14,
            'align': 'center',
            'valign': 'vcenter'
        })
        header = workbook.add_format({
            'bg_color': '#F7F7F7',
            'color': 'black',
            'align': 'center',
            'valign': 'top',
            'border': 1
        })
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="P@ssword_001",database="test")

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM auth_permission")

        myresult = mycursor.fetchall()
        print(myresult)
        worksheet.merge_range('B2:H2', "Test Data")
        worksheet.write('A1:A2', 'Hello world')
        worksheet.write('B2:B2',"No", header)
        worksheet.write('B3:B3',"Town", header)
        worksheet.write('B4:B4',"Max T. (℃)", header)

        workbook.close()
    
    if "action" in data:
        
        workbook = xlsxwriter.Workbook('hello.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.write('A1', 'Hello world')

        workbook.close()

    if "sheet" in data:
        
        workbook = xlsxwriter.Workbook('hello.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Hello world')
        workbook.close()        

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Vinoth, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

# initialization
time.sleep(2)
speak("Hi Vinoth, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
