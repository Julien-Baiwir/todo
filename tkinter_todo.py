import tkinter
from tkinter import *

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task= task_entry.get()
    task_entry.delete(0, END)
    
    if task:
        with open("tkinter_list.txt", 'a') as taskfile: taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    
    if task in task_list:
        task_list.remove(task)
        with open("tkinter_list.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task +"\n")
    listbox.delete( ANCHOR)
    

def openTaskFile():   
    try:
        global task_list
        with open("tkinter_list.txt", "r") as taskfile:
         tasks = taskfile.readlines()
        for task in tasks:
            if task !='/n':
                task_list.append(task)
                listbox.insert(END, task)
    
    except:
        file=open('tkinter_list.txt', 'w')  
        file.close()    
        
#icon
Image_icon=PhotoImage(file="Image/task.png")
root.iconphoto(False, Image_icon)

#topbar
TopImage = PhotoImage(file="Image/topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file ="Image/dock.png")
Label(root, image=dockImage, bg ="#32405b").place(x=30, y=25)

heading=Label(root,text="ALL TASK",font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

#main
frame= Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task=StringVar()
task_entry=Entry(frame, width=18, font="arial 20", bd = 0)
task_entry.place(x=10, y=7)
task_entry.focus()

button=Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)

button.place(x=300, y=0)

#listbox
frame1 = Frame(root, bd=3, width=700, heigh=280, bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1, font=('arial', 12), width=40, heigh=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a9fff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = BOTH)

listbox.config(yscrollcommand=scrollbar.set)

openTaskFile()

#delete
Delete_icon=PhotoImage(file="Image/delete.png")
Button(root, image = Delete_icon, bd =0, command= deleteTask).pack(side=BOTTOM, pady=13 )

root.mainloop()
