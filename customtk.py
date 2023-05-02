# importing required modules
import tkinter
import customtkinter
from PIL import ImageTk, Image
import requests
from models import User
import ctypes
from CTkMessagebox import CTkMessagebox

# backend connection
url = 'http://localhost:5000/'
user = User()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("600x440")
app.title('Login')


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("Supply Solutions")
        # remove title bar , page reducer and closing page !!!most have a quit button with app.destroy!!! (this app have a quit button so don't worry about that)
        self.overrideredirect(True)
        # make the app as big as the screen (no mater wich screen you use)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # root!
        self.main_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        self.left_side_panel = customtkinter.CTkFrame(self.main_container, width=150, corner_radius=10)
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)

        self.left_side_panel.grid_columnconfigure(0, weight=1)
        self.left_side_panel.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.left_side_panel.grid_rowconfigure((4, 5), weight=1)

        # self.left_side_panel WIDGET
        self.logo_label = customtkinter.CTkLabel(self.left_side_panel, text="Welcome! \n",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.scaling_label = customtkinter.CTkLabel(self.left_side_panel, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.left_side_panel,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20), sticky="s")

        self.bt_Quit = customtkinter.CTkButton(self.left_side_panel, text="Quit", fg_color='#EA0000',
                                               hover_color='#B20000',
                                               command=self.close_window)
        self.bt_Quit.grid(row=9, column=0, padx=20, pady=10)

        # button to select correct frame IN self.left_side_panel WIDGET
        self.bt_homepage = customtkinter.CTkButton(self.left_side_panel, text="Homepage",
                                                   command=lambda: self.homie(user.id))
        self.bt_homepage.grid(row=1, column=0, padx=20, pady=10)

        self.bt_profile = customtkinter.CTkButton(self.left_side_panel, text="Profile", command=self.profile)
        self.bt_profile.grid(row=2, column=0, padx=20, pady=10)

        self.bt_categories = customtkinter.CTkButton(self.left_side_panel, text="Manager Options",
                                                     command=self.manager)
        self.bt_categories.grid(row=3, column=0, padx=20, pady=10)

        # right side panel -> have self.right_dashboard inside it
        self.right_side_panel = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)

        self.right_dashboard = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#ffffff")
        self.right_dashboard.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0,
                                  pady=0)
        self.id = id
        self.homie(id)
    #  self.right_dashboard   ----> dashboard widget
    def homie(self, id):
        self.clear_frame()

        self.name = customtkinter.CTkLabel(master=self.right_dashboard, text=user.name,
                                           font=('Century Gothic', 50))
        self.lastname = customtkinter.CTkLabel(master=self.right_dashboard, text=user.lastname,
                                               font=('Century Gothic', 50))
        self.name.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        self.lastname.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


        def help_func():
            ctypes.windll.user32.MessageBoxW(0,
                                             "Here are the app instructions:\n\n1. asd\n2. sdfs\n3. sdfgsdg\n4. hrth",
                                             "Help", 0)

        self.help_BTN = customtkinter.CTkButton(master=self.right_dashboard, width=60, height=20, text="Help",
                                                command=help_func,
                                                corner_radius=6)
        self.help_BTN.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)


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

    def profile(self):
        self.clear_frame()
        # self.bt_from_frame3 = customtkinter.CTkButton(self.right_dashboard, text="Profile",
        #                                               command=lambda: print("test profile"))
        # self.bt_from_frame3.grid(row=0, column=0, padx=20, pady=(10, 0))

        self.name = customtkinter.CTkLabel(master=self.right_dashboard, text="First name: ",
                                           font=('Century Gothic', 18))
        self.name_entry = customtkinter.CTkEntry(master=self.right_dashboard, width=220)
        self.name_entry.insert(0, user.name)

        self.lastname = customtkinter.CTkLabel(master=self.right_dashboard, text="Last name: ",
                                               font=('Century Gothic', 18))
        self.lastname_entry = customtkinter.CTkEntry(master=self.right_dashboard, width=220)
        self.lastname_entry.insert(0, user.lastname)

        self.email = customtkinter.CTkLabel(master=self.right_dashboard, text="E-mail: ",
                                            font=('Century Gothic', 18))
        self.email_entry = customtkinter.CTkEntry(master=self.right_dashboard, width=220)
        self.email_entry.insert(0, user.email)

        def save_changes_func():
            data = {'email': self.email_entry.get(), 'name': self.name_entry.get(),
                    'lastname': self.lastname_entry.get()}
            response = requests.post(url + 'changeInfo', data=data)
            if response.status_code == 200:
                result = response.json()
                if result['message'] == 'change successful':
                    ctypes.windll.user32.MessageBoxW(0, "Your changes have been saved in the system.", "Saved Changes",
                                                     0)
                    user.name = data['name']
                    user.email = data['email']
                    user.lastname = data['lastname']
                else:
                    ctypes.windll.user32.MessageBoxW(0, "Your changes have NOT been saved in the system.", "ERROR", 0)

        self.save_BTN = customtkinter.CTkButton(master=self.right_dashboard, width=60, height=20, text="Save changes",
                                                command=save_changes_func,
                                                corner_radius=6)

        self.name.place(relx=0.3, rely=0.1, anchor=tkinter.CENTER)
        self.name_entry.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        self.lastname.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)
        self.lastname_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        self.email.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)
        self.email_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.save_BTN.place(relx=0.75, rely=0.3, anchor=tkinter.CENTER)

        #  self.right_dashboard   ----> categories widget
        def manager(self):
            self.clear_frame()

            # The email selection combo box
            email_type = {}  # keys = emails, values = user type
            response = requests.get(url + 'getUsersTypes')
            if response.status_code == 200:
                result = response.json()
                # print(result)
                for x in result['users']:
                    email_type[x[0]] = int(x[1])

            def add_definition(n):
                if n == 1:
                    return '1 - Student'
                elif n == 2:
                    return '2 - Staff'
                else:
                    return '3 - Manager'

            def save_callback():
                email_type[combobox1.get()] = int(combobox2.get()[0])

                temp_data = {}
                temp_email = combobox1.get()
                temp_data['email'] = temp_email
                temp_type = int(combobox2.get()[0])
                temp_data['type'] = temp_type

                response = requests.post(url + 'changeType', data=temp_data)
                if response.status_code == 200:
                    print(email_type, temp_data)
                    result = response.json()

            def delete_callback():

                temp_data = {}
                temp_email = combobox1.get()
                temp_data['email'] = temp_email

                if CTkMessagebox(icon='warning', title="Warning", option_1="Yes", option_2="Cancel",
                                 message="Are you sure you want to delete this user?").get() == 'Yes':
                    del email_type[combobox1.get()]
                    response = requests.post(url + 'removeUser', data=temp_data)
                    if response.status_code == 200:
                        print(email_type, temp_data)
                        result = response.json()

                    # combobox1['values'] = list(test_dictionary.keys())
                    combobox1.configure(values=list(email_type.keys()))
                    if len(email_type) > 0:
                        combobox1.set(list(email_type.keys())[0])
                        update_combobox2()

            def update_combobox2(*args):
                key = combobox1.get()
                value = add_definition(email_type.get(key))
                if email_type.get(key) is not None:
                    combobox2.set(str(value))

            combobox1_var = customtkinter.StringVar(value=list(email_type.keys())[0])
            combobox1 = customtkinter.CTkComboBox(master=self.right_dashboard, values=list(email_type.keys()),
                                                  variable=combobox1_var, width=200, height=40,
                                                  corner_radius=5, dropdown_font=('Arial', 12),
                                                  command=update_combobox2)
            combobox1.pack(pady=10)

            combobox2_var = customtkinter.StringVar(value=add_definition(list(email_type.values())[0]))
            combobox2 = customtkinter.CTkComboBox(master=self.right_dashboard,
                                                  values=['1 - Student', '2 - Staff', '3 - Manager'],
                                                  variable=combobox2_var, width=200, height=40, corner_radius=5,
                                                  dropdown_font=('Arial', 12))
            combobox2.pack(pady=10)

            save_button = customtkinter.CTkButton(master=self.right_dashboard, text="Save", font=('Arial', 14),
                                                  corner_radius=5,
                                                  hover=True, command=save_callback)
            save_button.pack(pady=10)

            delete_button = customtkinter.CTkButton(master=self.right_dashboard, text="Delete User", font=('Arial', 14),
                                                    corner_radius=5,
                                                    hover=True, command=delete_callback)
            delete_button.pack(pady=10)  #

        # Change scaling of all widget 80% to 120%
        def change_scaling_event(self, new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            customtkinter.set_widget_scaling(new_scaling_float)

        # close the entire window
        def close_window(self):
            App.destroy(self)

        # CLEAR ALL THE WIDGET FROM self.right_dashboard(frame) BEFORE loading the widget of the concerned page
        def clear_frame(self):
            for widget in self.right_dashboard.winfo_children():
                widget.destroy()
def register_in_db(w, entry1, entry2, entry3, entry4):
    data = {
        'email': entry1.get(),
        'password': entry4.get(),
        'firstname': entry2.get(),
        'Last name': entry3.get(),
    }
    response = requests.post(url + 'register', data=data)
    if response.status_code == 200:
        result = response.json()
        if result['message'] == 'register successful':
            w.destroy()
            app = customtkinter.CTk()  # creating custom tkinter window
            app.geometry("600x440")
            app.title('Login')
            login_page(app)
        else:
            print('shpih')
    else:
        print('Failed to authenticate user')


def register_function(app):
    app.destroy()  # destroy current window and creating new one
    w = customtkinter.CTk()
    w.geometry("600x440")
    w.title('Register')
    img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
    l1 = customtkinter.CTkLabel(master=w, image=img1)
    l1.pack()

    # creating custom frame
    frame = customtkinter.CTkFrame(master=l1, width=320, height=400, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Register to our system", font=('Century Gothic', 20))
    l2.place(x=50, y=45)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Email')
    entry1.place(x=50, y=100)
    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='First name')
    entry2.place(x=50, y=155)
    entry3 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Last name')
    entry3.place(x=50, y=210)
    entry4 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry4.place(x=50, y=265)
    register_button = customtkinter.CTkButton(master=frame, width=120, height=40, text="Register",
                                              command=lambda: register_in_db(w, entry1, entry2, entry3, entry4),
                                              corner_radius=6)
    register_button.place(x=105, y=325)

    w.mainloop()

