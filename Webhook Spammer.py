import requests
import tkinter
import customtkinter

def Spam():
    while True:
        requests.post(Webhook.get(), json = {"content": Message.get()})
   
def Send():
    requests.post(Webhook.get(), json = {"content": Message.get()})
 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

App = customtkinter.CTk()
App.resizable(False, False)
App.geometry("425x190")
App.title("Webhook Deleter")

Label_1 = customtkinter.CTkLabel(App, text = "Webhook:", font = ("cascadia mono", 18))
Label_1.grid(row = 0, column = 0, padx = 10, pady = 8)

Webhook_Url = tkinter.StringVar()
Webhook = customtkinter.CTkEntry(App, font = ("cascadia mono", 13), width = 300, height = 30, textvariable = Webhook_Url, )
Webhook.grid(row = 0, column = 1, padx = 5, pady = 8)

Label_2 = customtkinter.CTkLabel(App, text = "Message:", font = ("cascadia mono", 18))
Label_2.grid(row = 1, column = 0, padx = 10, pady = 8)

Message_Content = tkinter.StringVar()
Message = customtkinter.CTkEntry(App, font = ("cascadia mono", 13), width = 300, height = 30, textvariable = Message_Content)
Message.grid(row = 1, column = 1, padx = 5, pady = 8)

Send_Message = customtkinter.CTkButton(App, text = "Send Message", font=("cascadia mono", 18), width = 400, height = 35, command = Send)
# Send_Message.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "w")
Send_Message.place(anchor = "n", relx = 0.5, rely = .525)


Spam_Webhook = customtkinter.CTkButton(App, text = "Spam Webhook", font = ("cascadia mono", 18), width = 400, height=35, command = Spam)
# Spam_Webhook.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "w")
Spam_Webhook.place(anchor = "n", relx = 0.5, rely = .75)

App.mainloop()
