##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

def test_my_button():
    frame_auth.tkraise()

# main window
root = tk.Tk()
root.wm_geometry("200x150")
root.title("CoolKid")
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack(padx=0,pady=0)

ent_username = tk.Entry(frame_login, bd=3, show="*")
ent_username.pack(padx=0,pady=0)

lbl_password = tk.Label(frame_login, text='Password:',font='Arial')
lbl_password.pack(padx=0,pady=0)

ent_password = tk.Entry(frame_login, bd=3, show="*")
ent_password.pack(padx=0,pady=0)


frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")
frame_login.tkraise()

btn_login = tk.Button(frame_login, text="Login", bd=6,fg="red",bg="blue", command = test_my_button)
btn_login.pack(padx=0,pady=0)

root.mainloop()