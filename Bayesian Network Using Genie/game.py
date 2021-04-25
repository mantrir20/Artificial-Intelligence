from tkinter import *
import time
from tkinter.constants import END
win = Tk()
win.geometry("500x500")
p1 = StringVar()
p2 = StringVar()
p3 = StringVar()
p4 = StringVar()
p5 = StringVar()
p6 = StringVar()
p7 = StringVar()


def solve(d, s1, s2, c, boat):
    all_colors = ["RED","BLUE","GREEN"]
    #cntText.insert(END,c)
    print("boat at: " + str(boat) + " RED: " + str(d["RED"]) + " BLUE: " + str(d["BLUE"]) + " GREEN: " + str(d["GREEN"]))
    st = "boat at: " + str(boat) + " RED: " + str(d["RED"]) + " BLUE: " + str(d["BLUE"]) + " GREEN: " + str(d["GREEN"])
    p3.set(st)
    """ p3.set(c)
    #boat_pos_txt.insert(END,boat)
    p4.set(boat)
    #red_txt.insert(END,str(d["RED"]))
    p5.set(str(d["RED"]))
    #blue_txt.insert(END,str(d["BLUE"]))
    p6.set(str(d["BLUE"]))
    #green_txt.insert(END,str(d["GREEN"]))
    p7.set(str(d["GREEN"])) """
    time.sleep(1)
    if(d["RED"] == 0 and d["BLUE"] == 0 and d["GREEN"] == 0):
        return True
    
    if(boat == "east"):
        c = c + 1
        if(solve(d,s1,None,c,"west") == True):
            return True
        else:
            if(solve(d,None,s2,c,"west") == True):
                return True
    
    if(boat == "west"):
        c = c + 1
        p_boat = ""
        if(s1 == None):
            p_boat = s2
        else:
            p_boat = s1
        
        for i in all_colors:
            curr_p = i
            if(curr_p != p_boat and d[curr_p] != 0):
                d[curr_p] -= 1
                if(s1 == None):
                    if(solve(d,curr_p,s2,c,"east") == True):
                        return True
                if(s2 == None):
                    if(solve(d,s1,curr_p,c,"east") == True):
                        return True
                d[curr_p] = d[curr_p] + 1
    return False

def enter():
    colour1 = p1.get()
    colour2 = p2.get()
    count = 1
    d = {"RED":3, "BLUE":3, "GREEN":3}
    boat = "east"
    ans = solve(d,colour1,colour2,count,boat)


win.title("Boat Trip")
l1 = Label(win, text="Colour1:", font=("calibri",18,"bold")).place(x=10,y=10)
entr1 = Entry(win, textvariable=p1).place(x=100,y=10)
l2 = Label(win, text="Colour2:", font=("calibri",18,"bold")).place(x=10,y=50)
entr2 = Entry(win,textvariable=p2).place(x=100,y=50)
entr = Button(win, text="Enter",font=("calibri",16,"bold"),command=enter).place(x=150,y=90)

""" cntLab = Label(win,text="Step No:",font=("Calibri",18,"bold")).place(x=10,y=150)
#cntText = Text(win,height=2,width=30).place(x=100,y=150)
cntText = Entry(win,textvariable=p3).place(x=100,y=150)

boat_pos_lab = Label(win,text="Boat Pos:",font=("Calibri",18,"bold")).place(x=10,y=190)
#boat_pos_txt = Text(win,height=2,width=30).place(x=100,y=190)
boat_pos_txt = Entry(win,textvariable=p4).place(x=100,y=190)

red_lab = Label(win,text="RED:",font=("calibri",18,"bold")).place(x=10,y=230)
#red_txt = Text(win,height=2,width=30).place(x=100,y=230)
red_txt = Entry(win,textvariable=p5).place(x=100,y=230)

blue_lab = Label(win,text="BLUE:",font=("calibri",18,"bold")).place(x=10,y=270)
#blue_txt = Text(win,height=2,width=30).place(x=100,y=270)
blue_txt = Entry(win,textvariable=p6).place(x=100,y=270)

green_lab = Label(win,text="GREEN:",font=("calibri",18,"bold")).place(x=10,y=310)
#green_txt = Text(win,height=2,width=30).place(x=100,y=310)
green_txt = Entry(win,textvariable=p7).place(x=100,y=310) """

txt_entr = Entry(win,textvariable=p3,width=50).place(x=10,y=130)





win.mainloop()