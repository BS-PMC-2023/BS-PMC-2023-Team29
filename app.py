from db import UserDb
from flask import Flask, jsonify, request
from models import User


db = UserDb()
# Create a cursor object to execute SQL queries
cursor = db.cursor

#init app
app = Flask("app")

@app.route('/login',methods=['POST'])
def login():
    temp = User()
    temp.email, temp.password = request.form['email'],request.form['password']
    if db.login(temp):
        user = db.get_user_by_email(temp.email).totuple()
        return jsonify({'message': 'Login successful','user': user})
    else:
        return jsonify({'message': 'Invalid username or password'})

if __name__ == '__main__':
    app.run(debug=True)
    

def login_function(app, entry1, entry2):
    email, passord = entry1.get(), entry2.get()

    data = {
        'email': email,
        'password': passord
    }

    response = requests.post(url + 'login', data=data)
    if response.status_code == 200:
        result = response.json()
        if result['message'] == 'Login successful':
            app.destroy()  # destroy current window and creating new one
            user.tupple_insert(result['user'])
            w = App()
            w.mainloop()
        else:
            print('shpih')
    else:
        print('Failed to authenticate user')


def login_page(app):
    if app:
        app.destroy()

    app = customtkinter.CTk()  # creating custom tkinter window
    app.geometry("600x480")
    app.title('Login')

    img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
    l1 = customtkinter.CTkLabel(master=app, image=img1)
    l1.pack()

    # creating custom frame
    frame = customtkinter.CTkFrame(master=l1, width=320, height=400, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Log into your account", font=('Century Gothic', 20))
    l2.place(x=50, y=45)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry2.place(x=50, y=165)

    l3 = customtkinter.CTkButton(master=frame, text="Forget password?", font=('Century Gothic', 12),
                                 command=lambda: forget_password(app))
    l3.place(x=155, y=195)

    # Create custom button
    login_button = customtkinter.CTkButton(master=frame, width=120, height=40, text="Login",
                                           command=lambda: login_function(app, entry1, entry2), corner_radius=6)
    login_button.place(x=30, y=235)
    register_button = customtkinter.CTkButton(master=frame, width=120, height=40, text="Register",
                                              command=lambda: register_function(app), corner_radius=6)
    register_button.place(x=170, y=235)

    img3 = customtkinter.CTkImage(Image.open("samilogo.png").resize((40, 40), Image.ANTIALIAS))

    img3 = customtkinter.CTkButton(master=frame, image=img3, text="Sami Shamoon College of Engineering", width=40,
                                   height=40, compound="left", fg_color='white', text_color='black',
                                   hover_color='#AFAFAF')
    img3.place(x=160, y=320, anchor=tkinter.CENTER)
    # COMMIT alex -------------------BSPMC2329 - 34---------------------------------------
    def about_func():
        ctypes.windll.user32.MessageBoxW(0, "Made with love by:\n\nAlex, Bar, Aden and Basel", "About Us", 0)

    # end COMMIT alex -------------------BSPMC2329 - 34---------------------------------------
    about_BTN = customtkinter.CTkButton(master=frame, width=60, height=20, text="About us", command=about_func,
                                        corner_radius=6)
    about_BTN.place(x=160, y=370, anchor=tkinter.CENTER)

    # You can easily integrate authentication system
    app.mainloop()

