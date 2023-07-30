import customtkinter

app = customtkinter.CTk()
app.geometry("1260x720")
app.resizable(False, False)

label = customtkinter.CTkLabel(app, text="hello", padx=20, pady=20, font=("Segoe UI", 20))
label.pack()

app.mainloop()
