from selenium import webdriver
from tkinter import *
from tkinter import messagebox  
from PIL import ImageTk,Image
import time

def driverTask():
    global page
    global end
    
    dest=str(end.get())
    
    #driver object creation
    c=webdriver.Chrome('C:\Program Files\selenium\chromedriver')   
    c.maximize_window()
    
    #google map page
    c.get("https://www.google.com/maps/@19.1502972,72.9316023,13z/data=!3m1!4b1")

    #enter end in searchbar
    time.sleep(3)
    c.find_element_by_id("searchboxinput").send_keys(dest)

    #press the direction button
    c.find_element_by_id("searchbox-directions").click()

    #enter start in searchbar
    time.sleep(3)
    c.find_element_by_xpath('//input[@placeholder="Choose starting point, or click on the map..."]').send_keys(start+"\n")

    #Get Details
    time.sleep(3)
    c.find_element_by_xpath('//span[.="Details"]').click()
    time.sleep(3)
    t=c.find_element_by_xpath('//span[@class="delay-light"]').text

    #quiting the browser
    c.quit()

    #dialogue box
    messagebox.showinfo(title="Selenium Hariharan 2020 Output ", message="Home: Mehul Cinema Mulund \nDestination: "+dest+"\nTime Required: "+t)


def pageDesign():
    #page
    global page
    page=Tk()
    page.geometry("400x300+441+200")
    page.overrideredirect(True)
    bg1=Image.open("assets\page.jpg")
    bg2=ImageTk.PhotoImage(bg1)
    back_ground= Label(page,image=bg2)
    back_ground.place(x=-2,y=-2)
    

    #cross button
    cb1=Image.open("assets\cross.jpg")
    cb2=ImageTk.PhotoImage(cb1)
    cross_button=Button(page,image=cb2,bd=0,highlightthickness=0,command=page.destroy)
    cross_button.place(x=368,y=0)

    #end entry
    global end
    end=StringVar()
    end_entry=Entry(page,textvariable=end,bd=0,font=("barlow semibold",12),width=31,justify=LEFT)
    end_entry.place(x=58,y=182)
    #end="don bosco institute of technology mumbai"

    #details
    g1=Image.open("assets\go.jpg")
    g2=ImageTk.PhotoImage(g1)
    go_button=Button(page,image=g2,bd=0,highlightthickness=0,command=driverTask)
    go_button.place(x=303,y=229)

    page.mainloop()

#declaring home
start="mehul cinema mulund"
dest=""
pageDesign()
