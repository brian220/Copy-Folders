import sys
sys.path.append("../copy_file.py")
import copy_file
import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askdirectory
from tkinter import PhotoImage
#main window
window = tk.Tk()
window.title('Copy Folders')
window.geometry('800x420')

#src label
src_label =tk.Label(window, text = "Source folder")
src_label.place(x = 20, y = 25, width = 100, height = 30)

#dest label
src_label =tk.Label(window, text = "Desrination folder")
src_label.place(x = 400, y = 25, width = 100, height = 30)


#src list box
lbs = tk.Listbox(window)
lbs.place(x = 20, y = 50, width = 275, height = 330)

#dest list box
lbd = tk.Listbox(window)
lbd.place(x = 400, y = 50, width = 275, height = 330)

#src button
#1. src add button
src_list_id = 1
src_list = []
def adds():
  global hit_adds
  global src_list_id
  filename = askdirectory()
  if filename != "":
    lbs.insert(src_list_id, str(src_list_id) + "  " + filename)
    src_list.append(filename)
    src_list_id += 1

add_src = tk.Button(window,text = "+", command = adds, font=('Helvetica', '25'))
add_src.place(x = 295, y = 50, width = 40, height = 40)

#2. src pop button
def pops():
  lbs.delete(tk.END)
  src_list.pop()

pop_src = tk.Button(window,text = "-", command = pops, font=('Helvetica', '25'))
pop_src.place(x = 295, y = 90, width = 40, height = 40)

#dest button
#1. dest add button 
dest_list_id = 1
dest_list = []
def addd():
  global dest_list_id
  filename = askdirectory()
  if filename != "":
    lbd.insert(dest_list_id, str(dest_list_id) + "  " + filename)
    dest_list.append(filename)
    dest_list_id += 1

add_dest = tk.Button(window,text = "+", command = addd, font=('Helvetica', '25'))
add_dest.place(x = 675, y = 50, width = 40, height = 40)

#2. dest pop button
def popd():
  lbd.delete(tk.END)
  dest_list.pop()
  
pop_dest = tk.Button(window,text = "-", command = popd, font=('Helvetica', '25'))
pop_dest.place(x = 675, y = 90, width = 40, height = 40)



#comfirm button
def comfirm():
  if len(src_list) != len(dest_list):
    tk.messagebox.showerror(message = "The source and destination size mismatch!!")
  else:
    copy_file.move_file_between_folder(src_list, dest_list)
  
comfirm_button = tk.Button(window , text = "Comfirm \n copy",command = comfirm)
comfirm_button.place(x = 700, y = 310, width = 70, height = 70)

	
#显示主窗口
window.mainloop()
#filename = askopenfilename()