import numpy as np
import tkinter as tk
from idlelib.tooltip import Hovertip
from package import *

#================================================ main ==================================================
#window
if __name__ == '__main__':
    param = parameter()
    root.title('main')
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='preview',
        command=(lambda e=ents: preview(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    Hovertip(b1,'Preview the alignment result for a single file.\nPlease select the file for which you would like to view the alignment result.')
    b2 = tk.Button(root, text='Do processing',
        command=(lambda e=ents: precessing(e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    Hovertip(b2,'Start batch process.')
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    Hovertip(b3,'Quit the program.')
    root.mainloop()