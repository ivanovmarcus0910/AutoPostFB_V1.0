import customtkinter as ctk

def say_hello():
    label.configure(text=f"Hello, {entry.get()}!")

app = ctk.CTk()
app.title("CustomTkinter Example")

entry = ctk.CTkEntry(app)
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Greet", command=say_hello)
button.pack(pady=10)

label = ctk.CTkLabel(app, text="")
label.pack(pady=10)

app.mainloop()