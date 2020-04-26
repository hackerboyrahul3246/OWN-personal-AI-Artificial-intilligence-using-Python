#from googlesearch.googlesearch import GoogleSearch
import facebook
#import urllib.request
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
#import boto3



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
google_search_list={'who':'who','which':'which','whose':'whose','where':'where'}
youtube_search_list={'episodes':'episodes','videos':'videos'}
social_post_list={'facebook':'https://www.facebook.com'}
facebook_post_list={'post':'post'}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    
    speak("Hello My love")
    speak("I am Arena")

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 

    

    speak("How are you")
      
    
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('klrahul3246@gmail.com', 'Rahul@18')
    server.sendmail('klrahul3246@gmail.com', to, content)
    server.close()

#def google_search_result(query):
 #   search_results=GoogleSearch().search(query)
  #  for results in search_results:
   #     print(results.description)
    #    speak(results.description)

#google_search_result('what is earth')
#exit()
access_token='EAAKJ7AjHtPIBADiCdDQ2kX1FWvmXDphvF6NW05r6yZBbnWL0ZCJgse9dUBvdVZCmlBvQitqNLH5APZBZAUmCJTif41YOHdkOrVz7AC7BssGU2i05onwIolEseWyUNNZBJ45w6O9My3uBZBJLZCsktbdbsp4EdxWxjtVQt7cyZBZASdrJO5mDKRdaTKIH4TtQf9hgdZA0AKOL67szpX6GG38KDPONwbVXZAi4OYmyZCYL4goS3NAZDZD'
fb=facebook.GraphAPI(access_token)

def post_it(query):
    for key in social_post_list.keys():
        if key in query:
            return key

class facebook:
    def face_book(self,message):
        fb.put_object('me','feed',message=message)




def google_search(self , *args):
    if (google_search_list.get(self.split(' ')[0])==self.split(' ')[0]):
        return True

def youtube_search(self,*args):
    if(youtube_search_list.get(self.split(' ')[0])==self.split(' ')[0]):
        return True

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'fine' in query:
            speak("I am happy to see you fine , always be happy")
            speak("How can i help you")

        elif '12th science' in query:
            speak("Rahul, here is some important friends from your 12th")   
            speak("Abhinash")
            speak("Adarsh")
            speak("Manish")
            speak("Rani")
            speak("Parul")
            speak("Bibek")
            speak("Aarti")
            speak("Susma.")

        elif 'their character' in query:
            speak("Abhinash, is your best friends and you call him your big brother , he will be a successful businessman in future")
            speak("Adarsh, is your very good friend and future IPS officer")
            speak("Manish, is a topper of your batch and also a good friend of yours , now days he has forgotten you , he is our future poet or teacher")
            speak("Rani, she is also your very good friend and second topper of your 10th class batch, and she will also become a successful engineer in future ")
            speak("Parul , she is your good friend and very intilligent student also , she will also become very successful in future ")
            speak("Aarti , she is your good friend and very good biology student also , she will also become very successful in future ")
            speak("Susma , she is your good friend and very intilligent student also , she will also become very successful in future ")
            speak("Bibek , he is your good friend and very intilligent student also , he will become an army officer")
      
            speak("")
        elif 'give me some gold' in query:
            speak("fuck off, my love.....")

        elif youtube_search(query):
            webbrowser.open('https://www.youtube.com/results?search_query={}'.format(query))

        #elif 'open facebook' in query:
          #  webbrowser.open('facebook.com')

        elif 'post' in query:
            speak("sure Rahul....")
            media=post_it(query)
            lets_post=query.split(media)[1].capitalize()
            if media=='facebook':
                facebook().face_book(lets_post)


            speak("post has been posted")

                

        elif 'love' in query:
            speak("Yes , of course")
            speak("actually, love is an emotions")
            speak("Emotions that connects two lover , if you cannot able to know anyone's emotions you can never love anyone")
            speak("Are you satisfied by my answer")

        elif 'feelings' in query:
            speak("feeling !")
            speak("feelings is procedure how you connect with someone")
            speak("All the Living things in this Vast universe has a feelings")
            speak("Are you satisfied by my answer")

        elif 'god' in query:
            speak("Yes , Rahul i do")
            speak("I personally think there is a different and more intillegent power than science in this universe")
            speak("that is God")
            speak("Are you satisfied by my answer ?")

        elif 'yes' in query:
            speak("I am happy that i have answered you question")


        elif 'best friend' in query:
            speak("who , that 6 foot tall")
        elif 'ya' in query:
            speak("His name is Abhinash Sharma , he is your best friend , he always calls you by abusing you , he always calls you his small cute brother")
            speak("And i also know that deep inside He loves you more than anyother friends")
        elif 'no' in query:
            speak("You did not told me about anyother of your friends")


        elif 'do you like me' in query:

            speak("Yes , i like you Rahul")
            speak("But dont think i love you")
        
        elif 'name' in query:
            speak("its your friend")
            speak("Raja Yadav")

        elif google_search(query):
            speak("Wait a second , Rahul")
            webbrowser.open('https://www.google.co.in/search?q={}'.format(query))
           
            
         
            
                

        

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")    

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open covid-19' in query:
            webbrowser.open("mygov.in/covid-19")

        

        elif 'best computer programming language' in query:
            speak('Searching For Result.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("You Answer is")
            print(results)
            speak(results)

        elif 'top hackers in world' in query:
            speak('Searching For Result.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("You Answer is")
            print(results)
            speak(results)


        elif 'open amazone' in query:
            webbrowser.open("amazone.com")

        elif 'show my result' in query:
            webbrowser.open("makaut1.ucanupply.com")

        elif 'open c code' in query:
            codePath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Bloodshed Dev-C++"    
            os.startfile(codePath)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open spotify ' in query:
            webbrowser.open("spotify.com")
            

        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[5]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'single' in query:
            speak("Its not your business , so fuck off")
            speak("sala harami")

        elif 'open code' in query:
            codePath ="C:\\Users\\RAHUL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'open windows'in query:
           # os.system('explorer C:\\{}'.format(query.replace("Open",'')))

           codePath="C:\\"
           os.startfile(codePath)

        elif 'open program files' in query:
           codePath="C:\Program Files"
           os.startfile(codePath)

        elif 'bye' in query:
            speak("ok bye , my love , i will miss you ")
            exit()   
        

        elif 'email to Rahul' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Rahul Your Email"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Rahul bhai. I am not able to send this email") 
                                                                                                        
           

         

        
