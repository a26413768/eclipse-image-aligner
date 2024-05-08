import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import cv2
import os
import time
from package.window_def import *
from package.process_def import *
from package.type_def import *
#Create an instance of Tkinter frame
root = tk.Tk()
preview_filename = ""
is_done = 0

#================================================ processing ==================================================
def precessing(ents):
    global is_done
    is_done = 0
    param = parameter(ents)
    progres=0
    progress_var = tk.DoubleVar()
    progress_str = tk.StringVar()

    progress_win = tk.Toplevel(root)
    progress_win.geometry('220x100')
    progress_win.title("processing")
    tk.Label(progress_win, textvariable=progress_str, width=15, height=2).pack()
    progress_bar = ttk.Progressbar(progress_win, variable=progress_var, maximum=100, length=200)
    progress_bar.pack()

    # Check if the input directory exists
    if not os.path.isdir(param.openDir):
        print(f"Error: The following folder does not exist:\n{param.openDir}")
        return

    # Get list of image files
    # imageFiles = os.listdir(param.openDir, )
    imageFiles = [f for f in os.listdir(param.openDir) if f.endswith(param.fileType)]
    if len(imageFiles) == 0:
        print("No file found!!!\n")
        progress_win.destroy()
        return
    print(imageFiles)

    progress_step = float(100.0/len(imageFiles))
    # Process each image
    for filename in imageFiles:
        progres+=progress_step
        progress_str.set(str(filename))
        progress_var.set(progres)
        progress_win.update()
        ret, resized = center_frame(param.openDir + '/' + filename, param)
        if ret == -1:
            continue
        # Save the image
        savePath = os.path.join(param.saveDir, filename)
        print(f"Now writing {savePath}")
        try:
            cv2.imwrite(savePath, resized)
        except cv2.error:
            filename_without_ex = os.path.splitext(os.path.basename(filename))[0]
            filename = filename_without_ex + ".tif"
            savePath = os.path.join(param.saveDir, filename)
            print(f"Now writing {savePath}")
            cv2.imwrite(savePath, resized)

    print("*******finish*******")
    progress_str.set("finish")
    progress_win.update()
    progress_win.destroy()

#================================================ preview ==================================================
def preview(ents):
    param = parameter(ents)
    preview_filename = filedialog.askopenfilename(filetypes=[("preview file", param.fileType)], initialdir=param.openDir)

    do_preview(ents, preview_filename)

def do_preview(ents, preview_filename):
    param = parameter(ents)

    ret, resized = center_frame(preview_filename, param)
    if ret == -1:
        return
    cv2.imshow('preview', resized)
    while cv2.getWindowProperty('preview', cv2.WND_PROP_VISIBLE) > 0:
        if cv2.waitKey(50) > 0:
            break
    cv2.destroyAllWindows()

#================================================ makeform ==================================================
def makeform(root, fields):
    ents = []
    i = 0
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ents.append(ent)
        ent.insert(0, default_val[i])
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=5,
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.YES,
                 fill=tk.X)
        i+=1
    return ents

