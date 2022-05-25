import os, smtplib
from random import randint
from tkinter import *
from simplecrypt import encrypt, decrypt
from tkinter.messagebox import showerror, showinfo, askokcancel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class path_take():
    main_path = os.path.abspath(__file__).replace(os.path.basename(__file__), '')
    with open(f'{main_path}/fromaddr.cfg', 'rb') as file:
        crypted_data = file.read()
        global fromaddr
        fromaddr = decrypt('if_u_jailbreak_here_u_gay', crypted_data).decode('utf8')
        file.close()

    with open(f'{main_path}/mypass.cfg', 'rb') as file:
        crypted_data = file.read()
        global mypass
        mypass = decrypt('if_u_jailbreak_here_u_gay', crypted_data).decode('utf8')
        file.close()
#  decrypting e-mail and password
class forgot_password():
    def forgot():
        login = entry_labels_etc.login_entry.get()
        toaddr = entry_labels_etc.email_entry.get()
        encrypt_code = entry_labels_etc.encrypting.get()
        with open(f'{path_take.main_path}/{login}_email.cfg', 'rb+') as file:
            email_decrypted = decrypt(encrypt_code, file.read()).decode('utf8')
            if email_decrypted == toaddr:
                forgot_password.email(toaddr=toaddr, login=login)
            else: showerror(title='LogIn', message='E-mail don`t correct! Try again!')
#  if u forgot password, u can delete account
class email():
    def email(toaddr, login, type_msg, password, encrypt_code):
        code = randint(10000, 99999)

        if type_msg == "debug":
            print("Debuging....")
        elif type_msg == 'forgot':
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = f"{code}. LogIn creating account"
            body = f"Your code: {code} \nIf you don`t asked this code, ignore the email."
            
            
            
        elif type_msg == 'registration' or 'login':
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = f"{code}. LogIn creating account"
            body = f"{code}"

            messageReg = MIMEMultipart()
            messageReg['From'] = fromaddr
            messageReg['To'] = toaddr
            messageReg['Subject'] = f"LogIn creating account"


            bodyReg = f'''Your LogIn: {login}
Your password: {password}
Your decrypt phrase: {encrypt_code}
Thanks for using my app!
Made in Russia with love!'''
            messageReg.attach(MIMEText(bodyReg, 'plain'))
            textReg = messageReg.as_string()
        else:
            showerror('Oh no!', 'Oh no! Creator idiot! Send this program in my Telegram: @bebra_YaFlay')
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, mypass)

        text = msg.as_string()
        
        server.sendmail(fromaddr, toaddr, text)
        
        def command():
            if type_msg == 'forgot':
                if getCode.get() in body:
                    newWindow.destroy()
                    os.remove(f'{path_take.main_path}/{login}.cfg')
                    os.remove(f'{path_take.main_path}/{login}_email.cfg')
                    deleting_text.del_text(when='all')
                    server.quit()
                else:
                    showerror(title='LogIn', message='Code isnt correct')
            elif type_msg == 'registration':
                if getCode.get() in body:
                    newWindow.destroy()
                    server.sendmail(fromaddr, toaddr, textReg)
                    server.quit()
                    creating_account.creating_account(login=login, password=password, encrypt_code=encrypt_code, toaddr=toaddr)
                else:
                    showerror(title='LogIn', message='code isnt correct')
            elif type_msg == 'login':
                if getCode.get() in body:
                    newWindow.destroy()
                    logging_account.loging(login=login, password=password, encrypt_code=encrypt_code)
                else:
                    showerror(title='LogIn', message='Code isnt correct')


        newWindow = Toplevel(window)
        newWindow.title("LogIn code")
        newWindow.geometry("200x200")
        getCode = Entry(newWindow, width=10)
        getCode.grid(row=1)
        button = Button(newWindow, text='Creating account', command=command)
        button.grid(row=2)  
        server.quit()     
# send code for ur mail
class creating_account():
    def creating_account(login, password, encrypt_code, toaddr):
        password2 = encrypt(encrypt_code, password)
        if not os.path.isfile(f'{path_take.main_path}/{login}.cfg'):
            with open(f'{path_take.main_path}/{login}.cfg', 'wb+') as file:
                file.write(password2)
                file.close()
            showinfo(title='LogIn', message='Account created!')
        else:
            showerror(title='LogIn', message='Account already created!')
        with open(f'{path_take.main_path}/{login}_email.cfg', 'wb+') as file:
            toaddr2 = encrypt(encrypt_code, toaddr) 
            file.write(toaddr2)
            file.close()
        deleting_text.del_text(when='all')
        # creating files with ur e-mail and password. All encrypted
class logging_account():  
    def loging(login, password, encrypt_code):
        try:
            with open(f'{path_take.main_path}/{login}.cfg', 'rb+') as file:
                passwordDecrypted = decrypt(encrypt_code, file.read()).decode('utf8')
                file.close()
            if password == passwordDecrypted:
                askokcancel(title='LogIn', message='LogIn succesful!')
                deleting_text.del_text(when='all')
            else:
                showerror(title='LogIn', message='Password or login don`t correct. Try again!')
                deleting_text.del_text(when='all')
        except Exception as e:
            print(e)
            showerror(title='LogIn', message='Account don`t created!')
        # log in function. u can use this for ur program
class deleting_text():
    def del_text(when):
        if when == 'login_entry':
            entry_labels_etc.login_entry.delete(0, END)
        elif when == 'password_entry':
            entry_labels_etc.password_entry.delete(0, END)
        elif when == 'encrypting':
            entry_labels_etc.encrypting.delete(0, END)
        elif when == 'email_entry':
            entry_labels_etc.email_entry.delete(0, END)
        elif when == 'all':
            entry_labels_etc.login_entry.delete(0, END)
            entry_labels_etc.password_entry.delete(0, END)
            entry_labels_etc.encrypting.delete(0, END)
            entry_labels_etc.email_entry.delete(0, END)
        # delete text login, password, encrypt code and email
class buttons_treatment():
    
    def clicked():
        login = entry_labels_etc.login_entry.get()
        encrypt_code = entry_labels_etc.encrypting.get()
        password = entry_labels_etc.password_entry.get()
        toaddr = entry_labels_etc.email_entry.get()
        email.email(toaddr=toaddr, login=login, password=password, encrypt_code=encrypt_code, type_msg='login')
        # login button 
    def creating_account_def():
        login = entry_labels_etc.login_entry.get()
        password = entry_labels_etc.password_entry.get()
        encrypt_code = entry_labels_etc.encrypting.get()
        toaddr = entry_labels_etc.email_entry.get()
        
        if login == ['mypass', 'fromaddr', 'debug']:
            showerror(title='LogIn', message='This login blocked!')
            deleting_text.del_text(when='login_entry')
        else:
            email.email(toaddr=toaddr, login=login, password=password, encrypt_code=encrypt_code, type_msg='registration')
        # creating account button 
    def closed():
        window.destroy()
        # window close button
    
class entry_labels_etc():
    login_label = Label(text='Login:')
    password_label = Label(text='Password:')
    encrypt_code_label = Label(text='En(De)crypt code:')
    email_label = Label(text='Your e-mail:')
    # labels for entry
    login_entry = Entry(width=20)#, window  )
    # login entry
    password_entry = Entry(width=20, show='*')#,window)
    # password entrywith seeked symbols 
    encrypting = Entry(  width=20, show='*')#,window)
    # encrypt code with seeked symbols
    email_entry = Entry(  width=20)#,window)
    # email entry 
    create_account_button = Button(  text='Create account', command=buttons_treatment.creating_account_def)#,window)
    # create account button
    login_button = Button(  text='LogIn', command=buttons_treatment.clicked)#,window)
    # log in button
    forgot_but = Button(text='Forgot password?', command=forgot_password.forgot)#,window)
    # forgot password button
    close = Button(text='Close', command=buttons_treatment.closed)#,window)
    # close app button
    # buttons and entry
window = Tk()
window.title('LogIn App')
window.geometry('415x180')
# window create
entry_labels_etc.email_entry.grid(column=2, row=3)
entry_labels_etc.password_entry.grid(column=2, row=1)
entry_labels_etc.encrypting.grid(column=2, row=2)
entry_labels_etc.login_entry.grid(column=2,row=0)
# entry
entry_labels_etc.create_account_button.grid(row=1, column=3)
entry_labels_etc.close.grid(column=3, row=3)
entry_labels_etc.forgot_but.grid(row=2, column=3)
entry_labels_etc.login_button.grid(row=0, column=3)
# buttons
entry_labels_etc.login_label.grid(column=1, row=0)
entry_labels_etc.password_label.grid(column=1, row=1)
entry_labels_etc.encrypt_code_label.grid(column=1, row=2)
entry_labels_etc.email_label.grid(column=1, row=3)
# labels
# grid for buttons and entry
window.mainloop()
# Thanks for watching my shit-code!
# If u seeked a bug, write me in Telegram: @bebra_yaflay or in VK(russian facebook and instagram): https://vk.com/bebra_yaflay