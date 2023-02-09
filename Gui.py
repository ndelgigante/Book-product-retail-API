import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")

def signup():
    print("U are in signup")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Book API")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Login", command=login)
button1.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Sign up", command=signup)
button2.pack(pady=12, padx=10)

root.mainloop()