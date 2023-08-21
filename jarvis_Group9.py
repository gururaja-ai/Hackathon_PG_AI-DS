import pyttsx3 #pip install pyttsx3 in terminal and then use this
import speech_recognition as sr
import datetime
import pyaudio
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui



engine=pyttsx3.init('sapi5') #syntax of the module
voices=engine.getProperty('voices') #takes properties from engines
# print(voices[0].id)
engine.setProperty('voice',voices[len(voices)-3].id)  #change 1 , 2 , 3 , 4 for changing voices

    
#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
#to convert your voice to text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio=r.listen(source,timeout=5,phrase_time_limit=4)
    try:
        print("recognizing...")
        query=r.recognize_google(audio, language='en-in') #change web search engine or website , we can use 
        print(f" user said : {query}")
    
    except Exception as e:
        speak("say that again please") #use any type of lanugage 
        return "none"
    return query
      


import datetime # add this line
def wish():
    hour = int(datetime.datetime.now().hour) # this should work now
#     tt=" hello "
#     # tt = time.strftime("%I:%M:%p")
# #to wish
# # def wish():
# #     hour=int(datetime.datetime.now().hour)
# #     tt = time.strftime("%I:%M:%p")
# #     # tt=time.strtime("%I:%M:%p")
#     if hour>=0 and hour <=12:
#         speak (f"good morning,its{tt}")
#     elif hour>12 and hour<18:
#         speak (f"good afternoon,its{tt}")
#     else:
#         speak (f"good evening,its{tt}")
        
    speak("This is Jio Companion, please tell me how can i help you")
    
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('guru.mtip@gmail.com','ai@GURU369') #change yousername and password
    server.sendmail('your email id',to,content)
    server.close()
        
#for news update
def news():
    main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=25fac6e462824b22b1a20c42860105ad'
    main_page=requests.get(main_url).json()
    #print main page
    articles=main_page["articles"]
    #print articles
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eight","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        #print(f"todays{day[1] news is : ",head[i]})
        speak(f"today's {day[i]} news is: {head[i]}")
    
    


print(voices[0].id) 

author="gururaj" #student name

""" apply voice based login system 
    if it fails then use passcode
    
"""

   
if __name__=="__main__":
    wish()
    # if 1:
    
    while True:
        query=takecommand().lower()
        #logic building for tasks
        if 'open notepad' in query:
            npath="C:\\Windows\\system32\\notepad.exe" 
            os.startfile(npath)
        elif "open adobe reader" in query:
            apath="C:\\Program Files (x86)\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            os.startfile(apath)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.Videocapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow("webcam",img)
                k=cv2.waitkey(50)
                if key==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        
        elif "play music" in query:
            music_dir="E:\\music"  #use directory
            songs=os.listendir(music_dir)
            # rd=random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir,song))
        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            
        elif "wikipedia" in query:
            speak("searching wikipedia..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)
        
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")
            
        elif "open google" in query:
            speak("what should I search for you")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "send message" in query:
            kit.sendwhatmsg("+918885830329","guru you got first prize in hackathon",2,25)
        
        elif "play songs on youtube" in query:
            kit.playonyt("see you again") # change your chosen song as per google
            
            
            
        elif "you can sleep" in query:
            speak("thanks for using, have agood day")
            sys.exit()
            
        elif "close notepad" in query:#to close any application
            speak("okay, closing notepad")
            os.system("taskill /f /im notepad.exe")
        
        elif "set alarm" in query:
            nn=int(datetime.datetime.now().hour)
            if nn==22:
                music_dir="E:\\music"
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
        
        elif "tell me a joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)
        
        elif"shut down the system" in query:
            os.system ("shutdown /s /t 5")
        elif"restart the system" in query:
            os.system ("shutdown /r /t 5")
        elif"sleep the system" in query:
            os.system ("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")    
            
            #speak("sir , do you have any other work")    
        
        
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.keyDown("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            
        elif "tell me new" in query:
            speak("please wait sir, fetching the latest news ")
            news()
        
        elif "email to guru" in query:
            speak("what should i say? ")
            query=takecommand().lower()
            if "send a file" in query:
                email='your@gmail.com' #your mail id
                password='your_pass' #your email account password
                send_to_email="person@gmail.com" #whom you are sending the message to
                speak("okay sir, what is the subject for this email")
                query=takecommand().lower()
                subject=query
                speak("and sir, what is the message for this email")
                query2=takecommand().lower()
                message=query2
                speak("sir please enter the correct path of the file into the shell")
                file_location=input("please enter the path here") 
                
                speak("please wait, i am sending email now")
                
                msg=MIMEMultipart()
                msg['From']=email
                msg['To']=send_to_email
                msg['Subject']=subject
                
                msg.attach(MIMEText(message,'plain'))
                
                #setup the attachment
                filename=os.path.basename(file_location)
                attachment=open(file_location,"rb")
                part=MIMEBase('application','octet-stream')
                part.set_payload(attatcment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment; filename= %s " % filename )

                #attach the attachment to the MIMEMultipart object
                msg.attach(part)
                
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email,password)
                text=msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to gururaj")
            else:
                email='your@gmail.com' #Your email
                password='your_pass' #your email account password
                send_to_email='person@gmail.com' #whom you are sending the messege to
                message=query # the message in the mail
                
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()#Use TLS
                server.login(email,password)
                server.sendmail(email,send_to_email,message) #send the email
                server.quit() #logout of the email server
                speak("email has been sent to gururaja")
           
        # elif "email to guru"  in query:
        #     try:
        #         speak("what should i say ? ")
        #         content=takecommand().lower()
        #         to="guru.mtip@gmail.com"
        #         # to=takecommand().lower()                
        #         sendEmail(to,content)
        #         speak("email has been sent")
                
        #     except Exception as e:
        #         print(e)
        #         speak("sorry, I am unable to send mail to {to} ".format(to))
        
        elif "no thanks" in query:
            speak("thanks for using this, have a good day.")
            sys.exit()
            
        speak("do you have any other work")

        
        
        
        
        
               
            
            
            
        
        
            
        
        
        
            
                
        
        
            
            
            
        
            