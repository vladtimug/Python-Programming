from tkinter import *
from tkinter.filedialog import *

global selected
selected = False

color_bg = 'gray14'
color_fg = 'turquoise2'
class Window():    # class Windows inherited from Frame
    def __init__ (self, main, title, geometry):
        self.main = main
        self.main.title(title)
        self.main.geometry(geometry)
        self.text_scroll = Scrollbar(main)
        self.text_scroll.pack(side = RIGHT, fill = Y)
        self.text_h_scroll = Scrollbar(main, orient = 'horizontal')
        self.text_h_scroll.pack(side = BOTTOM, fill = X)
        self.T = Text(main, height = 34, width = 20, bg = color_bg, fg = color_fg,font = ('Helvetica', 14), yscrollcommand = self.text_scroll.set, undo = True, wrap = 'none', xscrollcommand = self.text_h_scroll.set)
        self.T.pack(fill = BOTH)
        self.text_scroll.config(command = self.T.yview)
        self.text_h_scroll.config(command = self.T.xview)
        
def client_exit():
    exit()
    
def open_new_window():
        new_window = Toplevel()
        new_window.iconbitmap('E:/concursuri & internships & personal_projects/Me/tkinter text editor/icon.ico')
        new_window.title('Editext-Beta')
        new_window.geometry('1000x800')
        text_scroll_new = Scrollbar(new_window)
        text_scroll_new.pack(side = RIGHT, fill = Y)
        text_h_scroll_new = Scrollbar(new_window, orient = 'horizontal')
        text_h_scroll_new.pack(side = BOTTOM, fill = X)
        T = Text(new_window, height = 34, width = 20, bg = color_bg, fg = color_fg, font = ('Helvetica', 14), yscrollcommand = text_scroll_new.set, undo = True, wrap = 'none', xscrollcommand = text_h_scroll_new.set)
        T.pack(fill = BOTH)
        text_scroll_new.config(command = T.yview)
        text_h_scroll_new.config(command = T.xview)

        menu = Menu(root)            # create menu of the main windows

        new_window.config(menu = menu)     # instantiate menu

        file = Menu(menu, tearoff = False)                # create file obj from class Menu

        file.add_command(label = "New", command = new_file)                # create command
        file.add_command(label = "New Window", command = open_new_window)
        file.add_command(label = 'Open', command = open_file)
        file.add_command( label = 'Save', command = save)
        file.add_command(label = 'Save As', command = save_as_file)
        file.add_separator()
        file.add_command(label = "Exit", command = client_exit)    # add exit command to file
        menu.add_cascade(label = "File", menu = file)    # add command to menu cascade

        # create the file object)
        edit = Menu(menu, tearoff = False)
        edit.add_command(label="Undo        (Ctrl+z)", command = getattr(app, 'T').edit_undo)
        edit.add_command(label="Redo        (Ctrl+y)",command = getattr(app, 'T').edit_redo)
        edit.add_separator()
        edit.add_command(label = "Cut           (Ctrl+x)", command = lambda: cut_text(False))
        edit.add_command(label = 'Copy          (Ctrl+c)', command = lambda: copy_text(False))
        edit.add_command(label = 'Paste         (Ctrl+v)', command = lambda: copy_text(False))
        menu.add_cascade(label = "Edit", menu = edit)    # add command to menu cascade5

        status_bar = Label(new_window, text = 'Ready    ', anchor = E)
        status_bar.pack(fill = X, side = BOTTOM, ipady = 10)
        
def open_file():
    getattr(app, 'T').delete('1.0', END)
    filename = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("python files", "*.py"),("txt files","*.txt"),("all files","*.*")))
    f = open(filename)
    data = f.read()
    status_bar.config(text = filename)
    app.main.title(filename)
    getattr(app, 'T').insert(END, data)
    f.close()

def new_file():
    getattr(app, 'T').delete('1.0', END)
    root.title('EdiText-Beta New File')
    status_bar.config(text = 'New File   ')

def save_as_file():
    filename = asksaveasfilename(defaultextension = ".*", initialdir = "/", title = "Save File As", filetypes = (("python files", "*.py"),("txt files","*.txt"),("all files","*.*")))
    if filename:
        filename = open (filename, "w")
        root.title(filename.name + ' EdiText-Beta')
        filename.write(getattr(app, 'T').get('1.0', END) )
        filename.close()

def save():
    file_types = [("python files", "*.py"),
                 ("txt files","*.txt"),
                 ("all files","*.*")]
    
    filename = asksaveasfile(mode = 'w', defaultextension = file_types, filetypes = file_types)
    if filename:
        text2save = str(getattr(app, 'T').get("1.0", END))
        filename.write(text2save)
        root.title(filename.name+ ' EdiText-Beta')
        filename.close()

def cut_text(event):
    global selected
    if event:
        selected = app.main.clipboard_get()
    else:
        if getattr(app, 'T').selection_get():
            selected = getattr(app, 'T').selection_get()
            getattr(app, 'T').delete("sel.first", "sel.last")
            app.main.clipboard_clear()
            app.main.clipboard_append(selected)
        
def paste_text(event):
    global selected
    if event:
        app.main.clipboard_get()
    else:
        if selected:
            position = getattr(app, 'T').index(INSERT)      
            getattr(app, 'T').insert(position, selected)        #insert text at cursor pos

def copy_text(event):
    global selected
    if event:
        selected = app.main.clipboard_get()
    else:    
        if getattr(app, 'T').selection_get():
            selected = getattr(app, 'T').selection_get()        
            app.main.clipboard_clear()
            app.main.clipboard_append(selected)
    
     
root = Tk()
root.iconbitmap('E:/concursuri & internships & personal_projects/Me/tkinter text editor/icon.ico')
app = Window(root, 'Editext-Beta', '1000x810')

menu = Menu(root)            # create menu of the main windows
app.main.config(menu = menu)     # instantiate menu

file = Menu(menu, tearoff = False)                # create file obj from class Menu

file.add_command(label = "New", command = new_file)                # create command
file.add_command(label = "New Window", command = open_new_window)
file.add_command(label = 'Open', command = open_file)
file.add_command(label = 'Save', command = save)
file.add_command(label = 'Save As', command = save_as_file)
file.add_separator()
file.add_command(label = "Exit", command = client_exit)    # add exit command to file
menu.add_cascade(label = "File", menu = file)    # add command to menu cascade

# create the file object)
edit = Menu(menu, tearoff = False)
edit.add_command(label="Undo        (Ctrl+z)",command = getattr(app, 'T').edit_undo)
edit.add_command(label="Redo        (Ctrl+y)",command = getattr(app, 'T').edit_redo)
edit.add_separator()
edit.add_command(label = "Cut           (Ctrl+x)", command = lambda: cut_text(False))
edit.add_command(label = 'Copy        (Ctrl+c)', command = lambda: copy_text(False))
edit.add_command(label = 'Paste        (Ctrl+v)', command = lambda: paste_text(False))
menu.add_cascade(label = "Edit", menu = edit)    # add command to menu cascade

status_bar = Label(root, text = 'Ready    ', anchor = E, bd = 1)
status_bar.pack(fill = X, side = BOTTOM)

app.main.bind('<Control-Key-x>', cut_text)
app.main.bind('<Control-Key-c>', copy_text)
app.main.bind('<Control-Key-v>', paste_text)

root.mainloop()
