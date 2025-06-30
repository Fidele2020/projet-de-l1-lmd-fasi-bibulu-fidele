import customtkinter as ctk
from PIL import Image
import pyttsx3 as pyt
import os
import wikipedia
import webbrowser

#image

meliodas=Image.open("melio.png")
brigade=Image.open("brigade.png")
savoir=Image.open("savoir.png")
exit=Image.open("exit.png")
sharu=Image.open("sharu.png")
konoha=Image.open("konoha.png")

#initialisation os

output_dir="mes audios"
os.makedirs(output_dir,exist_ok=True)

#initialisation appli

app=ctk.CTk()
app.title("projet upc")
app.geometry("500x600")
app.resizable(False,False)
app.config(bg="gray10")
nomination="hello"

#creation de fonction pour chaque button

def web():
    webbrowser.open("index.html")

def button_pyttsx3():
    def button3():
        frame1.destroy()

    def lecture():
        texte=textarea.get("1.0","end").strip()
        if texte:
            text=textarea.get("1.0","end")
            engine=pyt.init()
            engine.say(text)
            engine.runAndWait()

        else:
            def supp():
                label0.configure(text="")
            label0.configure(text=msg)
            app.after(3000,supp)
    def save():
        texte=textarea.get("1.0","end").strip()
        if texte:
            text=textarea.get(0.0,"end")
            engine=pyt.init()
            nom=os.path.join(output_dir,f"audio_{nomination}_.mp3")
            engine.save_to_file(text,nom)
            engine.runAndWait()
            engine.stop()
            def supp():
                 label0.configure(text="")
            label0.configure(text="audio enregistrer:-)")
            app.after(3000,supp)

        else:   
            def supp():
                 label0.configure(text="")
            label0.configure(text=msg)
            app.after(3000,supp)

    msg="veuillez saisir du texte \ndans le champ de texte\npour plus d'infos\nprière de visiter notre site"

    frame1=ctk.CTkFrame(frame_principal,border_color="orange",border_width=2,corner_radius=12,bg_color="gray30")

    frame1.pack(expand=True,fill="both")
    frame1.propagate(False)

    textarea=ctk.CTkTextbox(frame1,bg_color="gray30",fg_color="gray15",height=400,border_width=2,font=("Algerian",20,"bold"),border_color="orange",corner_radius=12)

    textarea.pack(pady=10,fill="x",padx=10)

    btn_3=ctk.CTkButton(frame1,text="lecture",font=("Algerian",20,"bold"),image=ctk.CTkImage(dark_image=sharu,light_image=sharu),border_color="orange",border_width=2,fg_color="green",hover_color="darkcyan",command=lecture)

    btn_3.place(x=14,y=420)

    btn_4=ctk.CTkButton(frame1,text="save",font=("Algerian",20,"bold"),image=ctk.CTkImage(dark_image=konoha,light_image=konoha),border_color="orange",border_width=2,fg_color="green",hover_color="darkcyan",command=save)

    btn_4.place(x=264,y=420)

    btn_5=ctk.CTkButton(frame1,text="exit",command=button3,font=("Algerian",20,"bold"),image=ctk.CTkImage(dark_image=exit,light_image=exit),border_color="orange",border_width=2,fg_color="red",hover_color="black")
    
    btn_5.place(x=140,y=470)
    
    label0=ctk.CTkLabel(app,text=None,fg_color=None,font=("Algerian",15,"bold"))
    label0.place(relx=0.2,rely=0)

def buttton_bote():

    

    def wiki(mot):
        wikipedia.set_lang("fr")
        try:
            resultat=wikipedia.summary(mot,sentences=2)
            return resultat
        except wikipedia.exceptions.DisambiguationError as e:
            return f"mot bizarre essayez d'etre plus precis"
        
        except wikipedia.exceptions.PageError:
            return "aucune page trouvèe"
        
        except Exception as e :
            return f"erreur: {str(e)}"

    def chatbot_response(entrage_text):
        responses={
            "bonjour":"bonjour comment ça va ?",
            "comment":"je suis un programme donc je vais toujours bien",
            "il est quel heure":"il est temps de coder",
            "bien":"j'en suis ravie ;)",
            "impoli":"je sais",
            "hum":"connard ?"
        }
        return responses.get(entrage_text.lower(),wiki(entrage_text))


    def send_message(event=None):
        user_message=entrage_text.get()
        if user_message.strip()!="":
            textarea.configure(state="normal")
            textarea.insert("end",f"vous:{user_message}\n", "user")
            bot_message=chatbot_response(user_message)
            textarea.insert("end",f"bot:{bot_message}\n", "bot")
            textarea.configure(state="disabled")
            textarea.see("end")
            entrage_text.delete(0,"end")



    frame2=ctk.CTkFrame(frame_principal,border_color="orange",border_width=2,corner_radius=12,  bg_color="gray30")
    frame2.pack(expand=True,fill="both")
    frame2.propagate(False)

    textarea=ctk.CTkTextbox(frame2,bg_color="gray30",fg_color="gray15",border_width=2,font=("Algerian",20,"bold"),border_color="orange",corner_radius=12,height=465,width=400,state="disabled",wrap="word")
    textarea.see("end")
    
    textarea.tag_config("user",foreground="white",spacing1=5)
    textarea.tag_config("bot",foreground="green",spacing1=5)

    textarea.place(x=10,y=10)

    entrage_text=ctk.CTkEntry(frame2,width=320,placeholder_text="entrer message")
    entrage_text.place(x=5,y=480)

    send_message=ctk.CTkButton(frame2,text="envoyez",width=50,command=send_message)
    send_message.place(x=340,y=480)

#creation widgets

frame_principal=ctk.CTkFrame(app,corner_radius=12,border_color="orange",border_width=2)
frame_principal.pack(pady=40,padx=40,expand=True,fill="both")
frame_principal.propagate(False)

button_pyt=ctk.CTkButton(frame_principal,text="MELIODAS ",height=40,font=("Algerian",20,"bold"),border_color="orange",fg_color="darkgreen",  hover_color="darkcyan",border_width=2,corner_radius=12,image=ctk.CTkImage(dark_image=meliodas,light_image=meliodas),command=button_pyttsx3)

button_pyt.place(x=120,y=130)

button_bot=ctk.CTkButton(frame_principal,text="TORKELL   ",height=40,font=("Algerian",20,"bold"),border_color="orange",border_width=2,corner_radius=12,image=ctk.CTkImage(dark_image=brigade,light_image=brigade),hover_color="darkcyan",fg_color="darkgreen",command=buttton_bote)

button_bot.place(x=120,y=230)

button_web=ctk.CTkButton(frame_principal,text="EN SAVOIR",height=40,font=("Algerian",20,"bold"),border_color="orange",border_width=2,corner_radius=12,image=ctk.CTkImage(dark_image=savoir,light_image=savoir),hover_color="darkred",fg_color="darkcyan",command=web)

button_web.place(x=120,y=330)





app.mainloop()