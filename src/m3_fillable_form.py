import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()
window.title("Form")
name_label = tk.Label(window, text="Name", height=2, bg="#808080", width=17)
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()
address1_label = tk.Label(window, text="Address Line 1", height=2, bg="#808080", width=17)
address1_label.pack()
address1_entry = tk.Entry(window)
address1_entry.pack()
address2_label = tk.Label(window, text="Address Line 2", height=2, bg="#808080", width=17)
address2_label.pack()
address2_entry = tk.Entry(window)
address2_entry.pack()
city_label = tk.Label(window, text="City", height=2, bg="#808080", width=17)
city_label.pack()
city_entry = tk.Entry(window)
city_entry.pack()
state_label = tk.Label(window, text="State", height=2, bg="#808080", width=17)
state_label.pack()
state_entry = tk.Entry(window)
state_entry.pack()
zip_label = tk.Label(window, text="Zip Code", height=2, bg="#808080", width=17)
zip_label.pack()
zip_entry = tk.Entry(window)
zip_entry.pack()
phone_label = tk.Label(window, text="Phone Number", height=2, bg="#808080", width=17)
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()
email_label = tk.Label(window, text="Email Address", height=2, bg="#808080", width=17)
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()
button = tk.Button(window, text="Submit")
button.pack()
window.mainloop()