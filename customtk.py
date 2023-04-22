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
