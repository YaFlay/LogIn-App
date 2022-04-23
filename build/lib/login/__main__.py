# github.com/yaflay
import tkinter as tk
from commands import *
def main():
    window = Tk()
    windows.title('LogIn App')
    windows.geometry('415x180')
    a = tk.PhotoImage(file=f'{path_take.main_path}/icon.png')
    windows.tk.call('wm', 'iconphoto', windows._w, a)
    # windows.window create
    login_label = Label(text='Login:')
    password_label = Label(text='Password:')
    encrypt_code_label = Label(text='En(De)crypt code:')
    email_label = Label(text='Your e-mail:')
    # labels for entry
    login_entry = Entry(  width=20 )
    # login entry
    password_entry = Entry(  width=20, show='*')
    # password entrywith seeked symbols 
    encrypting = Entry(  width=20, show='*')
    # encrypt code with seeked symbols
    email_entry = Entry(  width=20)
    # email entry 
    create_account_button = Button(  text='Create account', command=buttons_treatment.creating_account_def)
    # create account button
    login_button = Button(  text='LogIn', command=buttons_treatment.clicked)
    # log in button
    forgot_but = Button(  text='Forgot password?', command=forgot_password.forgot)
    # forgot password button
    close = Button(  text='Close', command=buttons_treatment.closed)
    # close app button
    # buttons and entry
    email_entry.grid(column=2, row=3)
    password_entry.grid(column=2, row=1)
    encrypting.grid(column=2, row=2)
    login_entry.grid(column=2,row=0)
    # entry
    create_account_button.grid(row=1, column=3)
    close.grid(column=3, row=3)
    forgot_but.grid(row=2, column=3)
    login_button.grid(row=0, column=3)
    # buttons
    login_label.grid(column=1, row=0)
    password_label.grid(column=1, row=1)
    encrypt_code_label.grid(column=1, row=2)
    email_label.grid(column=1, row=3)
    # labels
    # grid for buttons and entry
    windows.mainloop()
    # Thanks for watching my shit-code!
    # If u seeked a bug, write me in Telegram: @bebra_yaflay or in VK: https://vk.com/bebra_yaflay

if __name__ == '__main__':
    main()