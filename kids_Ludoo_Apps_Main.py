import Tkinter as tk
import sys
from PIL import ImageTk
from PIL import Image
#from Modules.Linked_List import CLL
import time
import random
import threading



class Kids_Ludoo_App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)    # create main root window assigned to 'MyApp' object

        
        self.My_App_Height=600
        self.My_App_Width=800
        
        self.configure(background="#262626")
        self.wm_state("zoomed")    
        self.overrideredirect(1)
        self.x_dim=self.winfo_screenwidth()
        self.y_dim=self.winfo_screenheight()
        
        self.parent_frame=tk.Frame(self,width=self.x_dim,height=self.y_dim,bg="#262626")
        self.parent_frame.pack()

        self.page_id=None

        self.selected_player_index=[0,0]

        self.points_table=[]

        self.First_Page()
        #self.Sixth_Page()


    def Quit(self):
        self.destroy()      
        
    def First_Page(self):
        fp=Initial_Dairy_Page(self,self.parent_frame)

    def Second_Page(self):
        Atgp=About_The_Game_Page(self,self.parent_frame)

    def Third_Page(self):
        P_Introduction=Player_Introduction(self,self.parent_frame)

    def Fourth_Page(self):
        P_Selection=Player_Selection(self,self.parent_frame)
        
    def Fifth_Page(self):
        Dice_Play=Ludoo_Playing(self,self.parent_frame)

    def Sixth_Page(self):
        Winner=Play_Result(self,self.parent_frame)
        
    def Page_Close(self):
        if self.page_id=="dairy_page_submit":
            self.Second_Page()
        elif self.page_id=="about_page":
            self.Third_Page()
        elif self.page_id=="intro_page_prev":
            self.Second_Page()
        elif self.page_id=="intro_page_next":
            self.Fourth_Page()
        elif self.page_id=="selection_page_prev":
            self.Third_Page()
        elif self.page_id=="selection_page_next":
            self.Fifth_Page()
        elif self.page_id=="result_request":
            self.Sixth_Page()





     
               
        
class Initial_Dairy_Page(tk.Frame):
    
    def __init__(self,parent,controller):
    
        tk.Frame.__init__(self,controller)

        self.parent=parent
        
        self.configure(height=parent.y_dim,width=parent.x_dim,bg="#262626")
        self.pack()

#_____________creating_main_canvas_for_dairyimages______________________
        
        
        self.main_canvas=tk.Canvas(self,height=self.parent.My_App_Height,width=self.parent.My_App_Width/2,
                                   relief="flat",highlightthickness=0)
        self.main_canvas.place(x=((self.parent.x_dim)-(self.parent.My_App_Width/2))/2,
                                y=((self.parent.y_dim)-(self.parent.My_App_Height))/2)
        

#______________Diary_image________________________________________        

        photo=ImageTk.PhotoImage(file="./initials/Final_Front.jpg")

        self.photo=photo
        
        self.main_canvas.create_image(200,300,image=photo,anchor="center")

#______________exit_button_&_image____________________________________        
        
        exit_button_image=ImageTk.PhotoImage(file="./initials/close1.jpg")

        self.exit_button_image=exit_button_image

        self.exit_button=tk.Label(self.main_canvas,image=exit_button_image,cursor="hand2",
                                   relief="flat",bd=0)
        self.exit_button.bind("<ButtonRelease-1>",self.Exit_Button_Event)
        self.exit_button.place(x=378,y=578)


#_____________Setting_Button_&_iamge_____________________________________

        setting_button_image=ImageTk.PhotoImage(file="./initials/Settings.jpg")
        self.setting_button_image=setting_button_image

        self.setting_button=tk.Label(self.main_canvas,image=setting_button_image,bd=0,cursor="hand2",
                                      relief="flat")
        self.setting_button.place(x=374,y=3)
        self.setting_button.bind("<ButtonRelease-1>",self.Setting_App)

#_______________password_setting_spin_box____________________________

        self.pswd_spin1=tk.Spinbox(self.main_canvas,width=1,from_=0,to=9,bg="#fefefe",disabledbackground="#fefefe",
                              relief="flat")
        self.pswd_spin1.place(x=149,y=470)

        self.pswd_spin2=tk.Spinbox(self.main_canvas,width=1,from_=0,to=9,bg="#fefefe",disabledbackground="#fefefe",
                              relief="flat")
        self.pswd_spin2.place(x=195,y=470)

        self.pswd_spin3=tk.Spinbox(self.main_canvas,width=1,from_=0,to=9,bg="#fefefe",disabledbackground="#fefefe",
                              relief="flat")
        self.pswd_spin3.place(x=245,y=470)

#______________Submit_Button_&_Key_Image________________________________________________

        submit_key_image=ImageTk.PhotoImage(file="./initials/App_Key.jpg")

        self.submit_key_image=submit_key_image

        self.submit_button=tk.Label(self.main_canvas,image=self.submit_key_image,bd=0,
                                     relief="flat",cursor="hand2",text="dairy_page_submit")
        self.submit_button.place(x=185,y=349)
        self.submit_button.bind("<ButtonRelease-1>",self.Password_Check)


#_____________Bheem_canvas_______________________________________
        self.bh_flag=0
        
        self.bheem_canvas=tk.Canvas(self,height=200,width=160,highlightthickness=0,bg="#262626")
        self.bheem_canvas.place(x=(self.parent.x_dim-160)-3,y=(self.parent.y_dim-200)-3)

        bheem_image1=ImageTk.PhotoImage(file="./initials/welcome_bheem_normal.jpg")
        self.bheem_image1=bheem_image1
        
        self.B=self.bheem_canvas.create_image(0,0,image=bheem_image1,anchor="nw")
        
        
        bheem_image2=ImageTk.PhotoImage(file="./initials/welcome_bheem_happy.jpg")
        self.bheem_image2=bheem_image2

#_______________________________________________________________________________________________

        self.setting_button_flag=0
        self.password_change_counter=1
        self.user_password=None
        self.confirm_user_password=None
        self.pswd_frame_flag=0
        

#____________________________________________________________________________________________

    def Setting_App(self,event):
        global setting_button_flag

        if event.x>=0 and event.x<=23:
            if event.y>=0 and event.y<=24:
                
                if self.setting_button_flag==1:
                    self.setting_frame.destroy()
                    self.setting_button_flag=0
                    return
                elif self.setting_button_flag==0:
                    
                    self.setting_button_flag=1
                    
                    self.setting_frame=tk.Frame(self.main_canvas,bg="cyan")
                    self.setting_frame.place(x=275,y=4)

                    self.change_pswd_label=tk.Label(self.setting_frame,text="Change Password",bd=1,relief="flat",width=14,
                                               cursor="hand2",bg="cyan")
                    self.change_pswd_label.pack(side="top")

                    self.change_pswd_label.bind("<Enter>",self.Setting_On_Hover)
                    self.change_pswd_label.bind("<Leave>",self.Setting_Leave_Hover)
                    self.change_pswd_label.bind("<ButtonRelease-1>",self.Change_Password)

    def Setting_On_Hover(self,event):
        event.widget.configure(fg="red")
        
    def Setting_Leave_Hover(self,event):
        event.widget.configure(fg="black")
        
    def Change_Password(self,event):
        if event.x>=0 and event.x<=101:
            if event.y>=0 and event.y<=18:
                self.password_change_counter=1
                self.Password_Frame()
                
    def Password_Frame(self):
        global pswd_frame_flag
        global password_change_counter
        
        if self.password_change_counter==1:             # to check whether user is on Old_Password or New_Password or Confirm_Password
            self.setting_button.unbind("<ButtonRelease-1>")
            self.change_pswd_label.unbind("<ButtonRelease-1>")
        
            self.change_pswd_label.configure(text="Old Password",relief="solid")
            
        elif self.password_change_counter==2:
            self.change_pswd_label.configure(text="New Password")

        elif self.password_change_counter==3:
            self.change_pswd_label.configure(text="Confirm Password")
            
            
        if self.pswd_frame_flag==0:
            
            self.setting_frame.configure(height=100)
            self.pswd_entry=tk.Entry(self.setting_frame,width=14,fg="grey")
            self.pswd_entry.pack()
            self.pswd_entry.bind("<FocusIn>",self.On_Entry_Focus)
                    
            self.pswd_entry.insert(0,"3-digit number")
                    
            self.ok_button=tk.Label(self.setting_frame,text="Ok",bd=1,relief="solid",width=6,cursor="hand2",bg="cyan")
            self.ok_button.pack(side="left")
            self.ok_button.bind("<Enter>",self.Setting_On_Hover)
            self.ok_button.bind("<Leave>",self.Setting_Leave_Hover)
            self.ok_button.bind("<ButtonRelease-1>",self.Get_Password)
        
            self.cancel_button=tk.Label(self.setting_frame,text="Cancel",bd=1,relief="solid",width=6,cursor="hand2",bg="cyan")
            self.cancel_button.pack(side="right")
            self.cancel_button.bind("<Enter>",self.Setting_On_Hover)
            self.cancel_button.bind("<Leave>",self.Setting_Leave_Hover)
            self.cancel_button.bind("<ButtonRelease-1>",self.Cancel_Password_Change)
            self.pswd_frame_flag=1
            
                    
    def Get_Password(self,event):
        global user_password
        global password_change_counter
        global confirm_user_password
        
        if event.x>=0 and event.x<=45:
            if event.y>=0 and event.y<=18:
                
                self.user_password=self.pswd_entry.get()
                
                pswd_check_flag=self.Check_Password_Validations(self.user_password)
                
                if pswd_check_flag==False:
                    self.pswd_entry.delete(0,"end")
                    self.ok_button.focus()
                    self.On_Entry_Focus_Out()
                    return
                else:
                    pswd_check_flag=None

                    if self.password_change_counter==1:
                        pswd_check_flag=self.Check_Old_Password(self.user_password)
                    
                        if pswd_check_flag==False:
                            self.pswd_entry.delete(0,"end")
                            self.ok_button.focus()
                            self.On_Entry_Focus_Out()
                            return
                        else:
                            self.pswd_entry.delete(0,"end")
                            self.ok_button.focus()
                            self.On_Entry_Focus_Out()
                            self.password_change_counter=2
                            self.Password_Frame()
                            
                    elif self.password_change_counter==2:
                        self.confirm_user_password=self.user_password
                        
                        self.pswd_entry.delete(0,"end")
                        self.ok_button.focus()
                        self.On_Entry_Focus_Out()
                        self.password_change_counter=3
                        self.Password_Frame()
                        
                    elif self.password_change_counter==3:
                        if self.user_password==self.confirm_user_password:
                            fp=open(".\game_docs\password.txt","w")
                            fp.write(self.confirm_user_password+"\n")
                            self.setting_frame.destroy()
                        else:
                            self.pswd_entry.delete(0,"end")
                            self.ok_button.focus()
                            self.On_Entry_Focus_Out()
                            self.password_change_counter=2
                            self.Password_Frame()
                        
                        
                    
                    
                
    def Check_Old_Password(self,temp_user_password):
        
        fp=open(".\game_docs\password.txt","r")
        old_pswd=fp.readline().strip()
        
        if old_pswd!=temp_user_password:
            fp.close()
            return False
        else:
            fp.close()
            return True
        
        
    def Check_Password_Validations(self,temp_user_password):
        if temp_user_password==" ":
                return False
        else:
            if temp_user_password=="3-digit number":
                return False
            else:
                if len(temp_user_password)!=3:
                    return False
                else:
                    if not temp_user_password.isdigit():
                        return False
                    else:
                        return True
        
    def On_Entry_Focus(self,event):
         self.pswd_entry.delete(0,"end")
         self.pswd_entry.config(show="*",fg="black")
         
    def On_Entry_Focus_Out(self):
        self.pswd_entry.delete(0,"end")
        self.pswd_entry.config(show="",fg="grey")
        self.pswd_entry.insert(0,"3-digit number")
        
        
    def Read_From_File_Password(self):
        app_password=None
        
        fp=open(".\game_docs\password.txt","r")
        app_password=fp.readline().strip()
        fp.close()
        return app_password
        
    def Cancel_Password_Change(self,event):
        if event.x>=0 and event.x<=45:
            if event.y>=0 and event.y<=18:
                
                self.setting_button_flag=0
                
                self.pswd_frame_flag=0
                
                self.setting_button.bind("<ButtonRelease-1>",self.Setting_App)
                
                self.password_change_counter==1
                
                self.change_pswd_label.bind("<ButtonRelease-1>",self.Change_Password)
                
                self.setting_frame.destroy()
                
        
#_____________Valadating_Password_______________________________________________________
        
    def Password_Check(self,event):
        app_password=None
        temp_pswd1=None
        if event.x>=0 and event.x<=24:
            if event.y>=0 and event.y<=49:
                app_password=self.Read_From_File_Password()
                
                temp_pswd=[]
                temp_pswd.append(self.pswd_spin1.get())
                temp_pswd.append(self.pswd_spin2.get())
                temp_pswd.append(self.pswd_spin3.get())
                
                temp_pswd1="".join(temp_pswd)
                
                if temp_pswd1==app_password:
                    
                    self.parent.page_id=event.widget.cget("text")
                    
                    self.pswd_spin1.configure(state="disabled")
                    self.pswd_spin2.configure(state="disabled")
                    self.pswd_spin3.configure(state="disabled")
                    
                    self.bheem_canvas.delete("all")
                    
                    B=self.bheem_canvas.create_image(0,0,image=self.bheem_image2,anchor="nw")
                    
                    '''
                    while True:
                        self.bheem_canvas.move(B,0.2,0)
                        pos=self.bheem_canvas.coords(B)
                        if pos[0]>=160:
                            break
                        self.parent.update()
                        time.sleep(0.005)
                    '''
                    
                    self.parent.update()
                    time.sleep(1)                    
                    self.parent.Page_Close()
                    self.destroy()
                else:
                    pass
            else:
                pass
        else:
            pass
#--------------------------------------------------------------------------------------

    def Exit_Button_Event(self,event):
        if event.x>=0 and event.x<=17:
            if event.y>=0 and event.y<=17:
                self.parent.Quit()

'''        
        
  #      self.pwd_entry=tk.Entry(self.main_canvas,relief="flat",width=16,show="*",
 #                               font="Times")
#        self.pwd_entry.place(x=150,y=520)
 #       self.pwd_entry.focus_set()

  #      self.pwd_entry.bind('<Return>',self.Password_Check)


  def Password_Check(self,event):
        temp_pswd=""
        pswd_length=0
        temp_pswd=self.pwd_entry.get()

        if temp_pswd==self.user_password:
            self.parent.Window_Geo_Change()
            self.Quit()
        else:
            pswd_length=len(temp_pswd)
            self.pwd_entry.select_range(0,pswd_length+1)
            self.pwd_entry.delete(0,pswd_length+1)
'''            









#_______________________________________________________________________________________________            
        
class About_The_Game_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,controller)

        self.parent=parent  # use parent to access the methods of Kids_Ludoo_App class

        self.configure(height=parent.y_dim,width=parent.x_dim,bg="#262626")
        self.pack()

        self.About_Canvas=tk.Canvas(self,height=parent.My_App_Height+2,width=self.parent.My_App_Width+2,bg="#81d7e1",highlightthickness=0)
                            
        self.About_Canvas.place(x=((self.parent.x_dim)-(self.parent.My_App_Width+2))/2,
                               y=((self.parent.y_dim)-(self.parent.My_App_Height+2))/2)

        open_dairy_image=ImageTk.PhotoImage(file="./initials/dp.jpg")

        self.open_dairy_image=open_dairy_image

        self.About_Canvas.create_image(401,301,image=open_dairy_image,anchor="center")
        

    #   image will load center relative to 400,300 position


        self.About_Canvas.create_text(100,120,anchor="w",font="Helvetica",
            text="About The Game")
        self.About_Canvas.create_line(100,130,220,130)

        self.About_Canvas.create_text(100,150,font="Times",anchor="w",
                           text="This is a Game just like Ludoo. The main")
        
        self.About_Canvas.create_text(100,170,font="Times",anchor="w",
                           text="difference between a General Ludoo and ")
        
        self.About_Canvas.create_text(100,190,font="Times",anchor="w",
                           text="this App is that it has only two player.")
        
        self.About_Canvas.create_text(160,220,font="Times",anchor="w",
                           text="If talked about the core language")
        
        self.About_Canvas.create_text(100,240,font="Times",anchor="w",
                           text="of this game, it has developed on Python")

        self.About_Canvas.create_text(100,260,font="Times",anchor="w",
                           text="(ver. 2.7.12) with including its two package")
        
        self.About_Canvas.create_text(100,280,font="Times",anchor="w",
                           text="Tkinter for GUI(Graphical User Interface")        
        
        self.About_Canvas.create_text(100,300,font="Times",anchor="w",
                           text="and PIL(Python Imaging Library) for image")
        
        self.About_Canvas.create_text(100,320,font="Times",anchor="w",
                                 text="manipulation.")
        
        self.About_Canvas.create_text(160,350,font="Times",anchor="w",
                           text="Python is a widely used high-level,")
        
        self.About_Canvas.create_text(100,370,font="Times",anchor="w",
                           text="general purpose, interpreted, dynamic prog-")
        
        self.About_Canvas.create_text(100,390,font="Times",anchor="w",
                           text="ramming language. Its design philosophy em-")
        
        self.About_Canvas.create_text(100,410,font="Times",anchor="w",
                           text="phasizes code readability, and its syntax allows")
        
        self.About_Canvas.create_text(100,430,font="Times",anchor="w",
                           text="programers to express the concepts in fewer")
        
        self.About_Canvas.create_text(100,450,font="Times",anchor="w",
                                text="lines of code than possible in language such as")
        self.About_Canvas.create_text(100,470,font="Times",anchor="w",
                           text="C++ or Java.")
        
        self.About_Canvas.create_text(505,150,font="Times",anchor="w",
                           text="Tkinter is Python's de-facto(exit-")
            
        self.About_Canvas.create_text(445,170,font="Times",anchor="w",
                           text="ing in fact, although perhaps not intended, or")
        self.About_Canvas.create_text(445,190,font="Times",anchor="w",
                           text="accepted) standard GUI (Graphical User In-")
        self.About_Canvas.create_text(445,210,font="Times",anchor="w",
                                text="Interface) package. It is a thin object orient-")
        self.About_Canvas.create_text(445,230,font="Times",anchor="w",
                           text="ed layer on top of Tcl/Tk. Tkinter is not only")
        self.About_Canvas.create_text(445,250,font="Times",anchor="w",
                                text="GUI programming toolkit for Python. It is a")
        self.About_Canvas.create_text(445,270,font="Times",anchor="w",
                           text="most commonly used one.")

        self.About_Canvas.create_text(505,300,font="Times",anchor="w",
                           text="PIL is a free library for the Python")
        self.About_Canvas.create_text(445,320,font="Times",anchor="w",
                                text="programming language that adds support for")
        self.About_Canvas.create_text(445,340,font="Times",anchor="w",
                           text="opening, manipulating and saving many diff-")
        self.About_Canvas.create_text(445,360,font="Times",anchor="w",
                                text="erent image file formats.")
        self.About_Canvas.create_text(505,390,font="Times",anchor="w",
                           text="PIL offers several standard proce-")
        self.About_Canvas.create_text(445,410,font="Times",anchor="w",
                                text="dures for image manipulation like. These inc-")
        self.About_Canvas.create_text(445,430,font="Times",anchor="w",
                           text="ludes 'per-pixel manipulations, masking and")
        self.About_Canvas.create_text(445,450,font="Times",anchor="w",
                                text="transparency handling, image filtering such")
        self.About_Canvas.create_text(445,470,font="Times",anchor="w",
                           text="as bluring contouring, adjusting brightness etc.")

        
#----------------------page_turn_button---------------------------------------                                 
       
        self.pto_img=ImageTk.PhotoImage(file="./initials/PTO.jpg")

        self.pto_button=tk.Label(self.About_Canvas,relief="flat",bd=0,text="about_page",
                                 image=self.pto_img,cursor="hand2")
        self.pto_button.bind("<ButtonRelease-1>",self.Page_Turn_Event)
        self.pto_button.place(x=672,y=545,height=30,width=70)

#----------------------Exit_Button--------------------------------------------        

        exit_button_image=ImageTk.PhotoImage(file="./initials/close2.jpg")

        self.exit_button_image=exit_button_image

        self.exit_button=tk.Label(self.About_Canvas,image=exit_button_image,bd=0,cursor="hand2")
        self.exit_button.bind("<ButtonRelease-1>",self.Exit_Button_Event)
        self.exit_button.place(x=779,y=3)
    

#-----------------------------------------------------------------------------

    def Exit_Button_Event(self,event):
        if event.x>=0 and event.x<=17:
            if event.y>=0 and event.y<=17:
                self.parent.Quit()
            else:
                pass
        else:
            pass
#-------------------Page_Turn_Button_Event-----------------------------

    def Page_Turn_Event(self,event):
        if event.x>=0 and event.x<=69:
            if event.y>=0 and event.y<=34:
                self.parent.page_id=event.widget.cget("text")
                self.parent.Page_Close()
                self.destroy()
            else:
                pass
        else:
            pass
        

#-----------------------End of the Class----------------------------------------


        

class Player_Introduction(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,controller)
        self.pack()

        self.parent=parent      # use parent to access the methods of Kids_Ludoo_App class

        self.configure(height=parent.y_dim,width=parent.x_dim,bg="#262626")
        self.pack()


#--------------creating main canvas---------------------------------------------

        self.main_canvas=tk.Canvas(self,height=parent.My_App_Height+2,width=self.parent.My_App_Width+2,bg="#81d7e1",highlightthickness=0)
        self.main_canvas.place(x=((self.parent.x_dim)-(self.parent.My_App_Width+2))/2,
                               y=((self.parent.y_dim)-(self.parent.My_App_Height+2))/2)

        open_dairy_image=ImageTk.PhotoImage(file="./initials/dp.jpg")

        self.open_dairy_image=open_dairy_image

        self.main_canvas.create_image(401,301,image=open_dairy_image,anchor="center")              
  
#-------------------------Motu-------------------------------------------

        motu_image=ImageTk.PhotoImage(file="./players/motu.jpg")
        self.motu_image=motu_image
                                      
        self.motu_label=tk.Label(self.main_canvas,image=motu_image,relief="flat",
                                 bd=0,text="motu")
        
        self.motu_label.place(x=75,y=70)

        self.motu_label.bind("<Enter>",self.onhover_message)
        self.motu_label.bind("<Leave>",self.onmouse_leave)

#-------------------------John--------------------------------------------------
     
        john_image=ImageTk.PhotoImage(file="./players/john.jpg")
        self.john_image=john_image

        self.john_label=tk.Label(self.main_canvas,image=john_image,relief="flat",
                                 bd=0,text="john")
        self.john_label.place(x=240,y=70)

        self.john_label.bind("<Enter>",self.onhover_message)
        self.john_label.bind("<Leave>",self.onmouse_leave)

#--------------------------Ghasitaram-------------------------------------------
      
        ghasitaram_image=ImageTk.PhotoImage(file="./players/ghasitaram.jpg")
        self.ghasitaram_image=ghasitaram_image

        self.ghasitaram_label=tk.Label(self.main_canvas,image=ghasitaram_image,bd=0,
                                       relief="flat",text="ghasitaram")
        self.ghasitaram_label.place(x=75,y=310)

        self.ghasitaram_label.bind("<Enter>",self.onhover_message)
        self.ghasitaram_label.bind("<Leave>",self.onmouse_leave)

#----------------------------Dr.Jhataka-----------------------------------------
     
        jhataka_image=ImageTk.PhotoImage(file="./players/jhataka.jpg")
        self.jhataka_image=jhataka_image

        self.jhataka_label=tk.Label(self.main_canvas,image=jhataka_image,bd=0,
                                    relief="flat",text="jhataka")
        self.jhataka_label.place(x=260,y=310)

        self.jhataka_label.bind("<Enter>",self.onhover_message)
        self.jhataka_label.bind("<Leave>",self.onmouse_leave)

#-----------------------------Bheem---------------------------------------------
      
        bheem_image=ImageTk.PhotoImage(file="./players/bheem.jpg")
        self.bheem_image=bheem_image

        self.bheem_label=tk.Label(self.main_canvas,image=bheem_image,relief="flat",
                                  bd=0,text="bheem")
        self.bheem_label.place(x=440,y=75)

        self.bheem_label.bind("<Enter>",self.onhover_message)
        self.bheem_label.bind("<Leave>",self.onmouse_leave)

#----------------------------Kaliya---------------------------------------------
   
        kalia_image=ImageTk.PhotoImage(file="./players/kalia.jpg")
        self.kalia_image=kalia_image

        self.kalia_label=tk.Label(self.main_canvas,image=kalia_image,relief="flat",
                                   bd=0,text="kaliya")
        self.kalia_label.place(x=600,y=75)

        self.kalia_label.bind("<Enter>",self.onhover_message)
        self.kalia_label.bind("<Leave>",self.onmouse_leave)

#-------------------------------Raju--------------------------------------------
   
        raju_image=ImageTk.PhotoImage(file="./players/raju.jpg")
        self.raju_image=raju_image

        self.raju_label=tk.Label(self.main_canvas,image=raju_image,bd=0,relief="flat",
                                 text="raju")
        self.raju_label.place(x=442,y=335)
        self.raju_label.bind("<Enter>",self.onhover_message)
        self.raju_label.bind("<Leave>",self.onmouse_leave)

#-------------------------------Chhutki-----------------------------------------
    
        chhutki_image=ImageTk.PhotoImage(file="./players/chhutki.jpg")
        self.chhutki_image=chhutki_image

        self.chhutki_label=tk.Label(self.main_canvas,image=chhutki_image,bd=0,
                                    relief="flat",text="chhutki")
        self.chhutki_label.place(x=610,y=330)

        self.chhutki_label.bind("<Enter>",self.onhover_message)
        self.chhutki_label.bind("<Leave>",self.onmouse_leave)

#---------------------------------Intro_Label-----------------------------------
    
        intro_image=ImageTk.PhotoImage(file="./player's_intro/Intro_message.jpg")
        self.intro_image=intro_image

        self.intro_label=tk.Label(self.main_canvas,text="intro",image=intro_image,bd=0,
                             relief="flat")
        self.intro_label.place(x=62,y=265)

#-----------------------------P.T.O---Buttons---------------------------------------------
        
        pto_image=ImageTk.PhotoImage(file="./initials/PTO.jpg")

        self.pto_image=pto_image

        self.pto_next_button=tk.Label(self.main_canvas,image=pto_image,bd=0,text="intro_page_next",
                                  relief="flat",cursor="hand2")
        self.pto_next_button.place(x=672,y=545,height=30,width=70)
        self.pto_next_button.bind("<ButtonRelease-1>",self.Page_Turn_Event)

        self.pto_prev_button=tk.Label(self.main_canvas,image=pto_image,bd=0,relief="flat",
                                       text="intro_page_prev",cursor="hand2")
        self.pto_prev_button.place(x=60,y=545,height=30,width=70)
        self.pto_prev_button.bind("<ButtonRelease-1>",self.Page_Turn_Event)

        

#--------------------------------Exit-------------------------------------------
        
        exit_button_image=ImageTk.PhotoImage(file="./initials/close2.jpg")

        self.exit_button_image=exit_button_image

        self.exit_button=tk.Label(self.main_canvas,image=exit_button_image,bd=0,
                                  cursor="hand2")
        self.exit_button.bind("<ButtonRelease-1>",self.Exit_Button_Event)
        
        self.exit_button.place(x=779,y=3)
        
#-------------------------------------------------------------------------------        

        self.temp_image=""
        
        self.message_image={"motu":"./player's_intro/motu_intro.jpg",
                      "john":"./player's_intro/john_intro.jpg",
                      "ghasitaram":"./player's_intro/ghasitaram_intro.jpg",
                      "jhataka":"./player's_intro/jhatka_intro.jpg",
                      "bheem":"./player's_intro/bheem_intro.jpg",
                      "kaliya":"./player's_intro/kalia_intro.jpg",
                      "raju":"./player's_intro/raju_intro.jpg",
                      "chhutki":"./player's_intro/chutki_intro.jpg"}       

    
#------------Exit_Button_Event---------------------------------------------------
        
    def Exit_Button_Event(self,event):
        if event.x>=0 and event.x<=17:
            if event.y>=0 and event.y<=17:
                self.parent.Quit()
            else:
                pass
        else:
            pass
#--------------------Page_Turn_Event--------------------------------------
        
    def Page_Turn_Event(self,event):
        if event.x>=0 and event.x<=69:
            if event.y>=0 and event.y<=34:
                self.parent.page_id=event.widget.cget("text")
                self.parent.Page_Close()
                self.destroy()
            else:
                pass
        else:
            pass

#----------------mouse_events--------------------------------------------
        
    def onhover_message(self,event):
        self.temp_image=ImageTk.PhotoImage(file=self.message_image[event.widget.cget("text")])
        time.sleep(3/2)
        self.intro_label.configure(image=self.temp_image)

    def onmouse_leave(self,event):
        self.intro_label.configure(image=self.intro_image)


#----------------------------End of the Class---------------------------

        

class Player_Selection(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,controller)
        self.pack()

        self.parent=parent
        self.configure(height=parent.y_dim,width=parent.x_dim,bg="#262626")
        self.pack()

        self.main_canvas=tk.Canvas(self,height=parent.My_App_Height+2,width=self.parent.My_App_Width+2,bg="#81d7e1",highlightthickness=0)
        
        self.main_canvas.place(x=((self.parent.x_dim)-(self.parent.My_App_Width))/2,
                               y=((self.parent.y_dim)-(self.parent.My_App_Height))/2)

        open_dairy_image=ImageTk.PhotoImage(file="./initials/dp.jpg")

        self.open_dairy_image=open_dairy_image

        self.main_canvas.create_image(401,301,image=open_dairy_image,anchor="center")

        self.players_address={0:ImageTk.PhotoImage(file="./selection/player_back.jpg"),
                              1:ImageTk.PhotoImage(file="./selection/motu.jpg"),
                              2:ImageTk.PhotoImage(file="./selection/john.jpg"),
                              3:ImageTk.PhotoImage(file="./selection/ghasitaram.jpg"),
                              4:ImageTk.PhotoImage(file="./selection/jhatka.jpg"),
                              5:ImageTk.PhotoImage(file="./selection/bheem.jpg"),
                              6:ImageTk.PhotoImage(file="./selection/kalia.jpg"),
                              7:ImageTk.PhotoImage(file="./selection/raju.jpg"),
                              8:ImageTk.PhotoImage(file="./selection/chhutki.jpg")
                              }

#---------------------------------------------------------------------------------------------------------------------------------------------        
        
        self.selected_player_label1=tk.Label(self.main_canvas,image=self.players_address[0],bd=0,
                                    relief="flat")
        self.selected_player_label1.place(x=108,y=88)

        self.selected_player_label2=tk.Label(self.main_canvas,image=self.players_address[0],bd=0,
                                    relief="flat")
        self.selected_player_label2.place(x=434,y=88)

        sure_image=ImageTk.PhotoImage(file="./initials/sure.jpg")
        self.sure_image=sure_image

        delete_image=ImageTk.PhotoImage(file="./initials/delete_sign.jpg")
        self.delete_image=delete_image

        self.player1_sure_button=tk.Label(self.main_canvas,image=sure_image,text="p1_sure",state="disabled",bg="#d2c5b4",
                                          bd=0,relief="flat",cursor="hand2")
        self.player1_sure_button.place(x=270,y=160)
        
        
        self.player1_delete_button=tk.Label(self.main_canvas,image=delete_image,text="p1_delete",state="disabled",bg="#d2c5b4",
                                            bd=0,relief="flat",cursor="hand2")
        self.player1_delete_button.place(x=270,y=227)
        

        self.player2_sure_button=tk.Label(self.main_canvas,image=sure_image,text="p2_sure",state="disabled",bg="#d2c5b4",
                                          bd=0,relief="flat",cursor="hand2")
        self.player2_sure_button.place(x=596,y=160)
        

        self.player2_delete_button=tk.Label(self.main_canvas,image=delete_image,text="p2_delete",state="disabled",bg="#d2c5b4",
                                            bd=0,relief="flat",cursor="hand2")
        self.player2_delete_button.place(x=596,y=227)
        

#----------------------------------------------------------------------------------------------------------------------------------------------        

        rewind_image=ImageTk.PhotoImage(file="./initials/rewind.jpg")
        self.rewind_image=rewind_image
        
        self.backward_button=tk.Label(self.main_canvas,image=rewind_image,text="backward",
                                      bd=0,relief="flat",cursor="hand2")
        self.backward_button.place(x=62,y=412)
        self.backward_button.bind("<ButtonRelease-1>",self.Arrow_Button_Event)

        forward_image=ImageTk.PhotoImage(file="./initials/forward.jpg")
        self.forward_image=forward_image
        
        self.forward_button=tk.Label(self.main_canvas,image=forward_image,text="forward",
                                     bd=0,relief="flat",cursor="hand2")
        self.forward_button.place(x=698,y=412)
        self.forward_button.bind("<ButtonRelease-1>",self.Arrow_Button_Event)

#-------------------------------------------------------------------------------------------------------------------------------------------------        

                
        pto_image=ImageTk.PhotoImage(file="./initials/PTO.jpg")


        self.pto_image=pto_image
        self.pto_next_button=tk.Label(self.main_canvas,image=pto_image,bd=0,text="selection_page_next",
                                  relief="flat",cursor="hand2")
        self.pto_next_button.place(x=672,y=545,height=30,width=70)
        self.pto_next_button.bind("<ButtonRelease-1>",self.Page_Turn_Event)


        self.pto_prev_button=tk.Label(self.main_canvas,image=pto_image,bd=0,text="selection_page_prev",
                                       relief="flat",cursor="hand2")
        self.pto_prev_button.place(x=60,y=545,height=30,width=70)
        self.pto_prev_button.bind("<ButtonRelease-1>",self.Page_Turn_Event)



        exit_button_image=ImageTk.PhotoImage(file="./initials/close2.jpg")

        self.exit_button_image=exit_button_image

        self.exit_button=tk.Label(self.main_canvas,image=exit_button_image,bd=0,
                                  cursor="hand2")
        self.exit_button.bind("<ButtonRelease-1>",self.Exit_Button_Event)
        
        self.exit_button.place(x=779,y=3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------

        
        

        players_back_image=ImageTk.PhotoImage(file="./initials/players_canvas_image.jpg")
        self.players_back_image=players_back_image
        
        self.players_canvas=tk.Canvas(self.main_canvas,width=584,height=180,highlightthickness=0)
        self.players_canvas.place(x=108,y=350)
        self.players_canvas.create_image(289,90,image=players_back_image,anchor="center")
        
        

        self.player_label1=tk.Label(self.players_canvas,image=self.players_address[1],relief="flat",bd=0,text="p1")
        self.player_label1.place(x=0,y=10)
        self.player_label1.bind("<ButtonRelease-1>",self.Label_Click_Event)
        

        self.player_label2=tk.Label(self.players_canvas,image=self.players_address[2],relief="flat",bd=0,text="p2")
        self.player_label2.place(x=146,y=10)
        self.player_label2.bind("<ButtonRelease-1>",self.Label_Click_Event)
        

        self.player_label3=tk.Label(self.players_canvas,image=self.players_address[3],relief="flat",bd=0,text="p3")
        self.player_label3.place(x=292,y=10)
        self.player_label3.bind("<ButtonRelease-1>",self.Label_Click_Event)
        

        self.player_label4=tk.Label(self.players_canvas,image=self.players_address[4],relief="flat",bd=0,text="p4")
        self.player_label4.place(x=438,y=10)
        self.player_label4.bind("<ButtonRelease-1>",self.Label_Click_Event)
        
#-----------------------------------------------------------------------------------------------------------------------------------------


        self.head=1
        self.id_var=None
        self.selected_player_index=[0,0]
        self.temp_player_index=0
        
    def Arrow_Button_Event(self,event):
        global head

        imglist=[]
        if event.x>=0 and event.x<=39:
            if event.y>=0 and event.y<=43:
                if event.widget.cget("text")=="forward":
                    if self.head==5:
                        return
                    self.head+=1 
                if event.widget.cget("text")=="backward":
                    if self.head==1:
                        return
                    self.head-=1  
                    
                if self.id_var!=None:
                    self.Label_Pusher()
                    self.id_var=None
                        
                for i in range(self.head,self.head+4):
                    imglist.append(self.players_address[i])
                
                self.player_label1.configure(image=imglist[0])
                self.player_label2.configure(image=imglist[1])
                self.player_label3.configure(image=imglist[2])
                self.player_label4.configure(image=imglist[3])

            else:
                pass
        else:
            pass
        

    def Label_Lifter(self):
        if self.id_var=="p1":
            self.player_label1.configure(self.player_label1.place(x=0,y=0))
        elif self.id_var=="p2":
            self.player_label2.configure(self.player_label2.place(x=146,y=0))
        elif self.id_var=="p3":
            self.player_label3.configure(self.player_label3.place(x=292,y=0))
        elif self.id_var=="p4":
            self.player_label4.configure(self.player_label4.place(x=438,y=0))
            
    def Label_Pusher(self):
        if self.id_var=="p1":
            self.player_label1.configure(self.player_label1.place(x=0,y=10))
        elif self.id_var=="p2":
            self.player_label2.configure(self.player_label2.place(x=146,y=10))
        elif self.id_var=="p3":
            self.player_label3.configure(self.player_label3.place(x=292,y=10))
        elif self.id_var=="p4":
            self.player_label4.configure(self.player_label4.place(x=438,y=10))

    def Calc_Player_Index(self):
        pn=0
        if self.id_var=="p1":
            pn=self.head+0
        elif self.id_var=="p2":
            pn=self.head+1
        elif self.id_var=="p3":
            pn=self.head+2
        elif self.id_var=="p4":
            pn=self.head+3
        return pn
    


    def Label_Click_Event(self,event):
        if self.selected_player_index[0]!=0 and self.selected_player_index[1]!=0:
            return
        temp_id=None
        temp_id=event.widget.cget("text")
        if self.id_var==None:
            self.id_var=temp_id
            self.Label_Lifter()
            self.temp_player_index=self.Calc_Player_Index()
            self.Player_Shower()
        else:
            self.Label_Pusher()
            self.id_var=temp_id
            self.Label_Lifter()
            self.temp_player_index=self.Calc_Player_Index()
            self.Player_Shower()

    def Confirm_Player(self,event):
        if event.x>=0 and event.x<=94:
            if event.y>=0 and event.y<=29:
                
                if event.widget.cget("text")=="p1_sure":
                    
                    self.selected_player_index[0]=self.temp_player_index
                    self.temp_player_index=0
                
                    self.player1_sure_button.unbind("<ButtonRelease-1>")
                    self.player1_sure_button.configure(state="disabled")

                    self.player1_delete_button.configure(state="normal")
                    self.player1_delete_button.bind("<ButtonRelease-1>",self.Remove_Player)

                    if self.selected_player_index[1]==0:

                        self.player2_sure_button.configure(state="normal")
                        self.player2_sure_button.bind("<ButtonRelease-1>",self.Confirm_Player)
                    
                elif event.widget.cget("text")=="p2_sure":

                    self.selected_player_index[1]=self.temp_player_index
                    self.temp_player_index=0

                    self.player2_sure_button.unbind("<ButtonRelease-1>")
                    self.player2_sure_button.configure(state="disabled")

                    self.player2_delete_button.bind("<ButtonRelease-1>",self.Remove_Player)
                    self.player2_delete_button.configure(state="normal")

                        

                
    def Remove_Player(self,event):
        if event.x>=0 and event.x<=94:
            if event.y>=0 and event.y<=29:
                
                if event.widget.cget("text")=="p1_delete":
                    
                    self.selected_player_label1.configure(image=self.players_address[0])
                    self.selected_player_index[0]=0

                    self.player1_sure_button.unbind("<ButtonRelease-1>")
                    self.player1_sure_button.configure(state="disabled")
                
                    self.player1_delete_button.unbind("<ButtonRelease-1>")
                    self.player1_delete_button.configure(state="disabled")

                    if self.selected_player_index[1]==0:

                        self.selected_player_label2.configure(image=self.players_address[0])
                        
                        self.player2_sure_button.unbind("<ButtonRelease-1>")
                        self.player2_sure_button.configure(state="disabled")

                        self.player2_delete_button.unbind("<ButtonRelease-1>")
                        self.player2_delete_button.configure(state="disabled")
                        
                elif event.widget.cget("text")=="p2_delete":

                    self.selected_player_label2.configure(image=self.players_address[0])
                    self.selected_player_index[1]=0
        
                    self.player2_delete_button.unbind("<ButtonRelease-1>")
                    self.player2_delete_button.configure(state="disabled")

                    self.player2_sure_button.bind("<ButtonRelease-1>",self.Confirm_Player)
                    self.player2_sure_button.configure(state="normal")
                    
                
        
    def Player_Shower(self):

        if self.selected_player_index[0]==0 and self.temp_player_index!=self.selected_player_index[1]:
            
            self.selected_player_label1.configure(image=self.players_address[self.temp_player_index])
            self.player1_sure_button.configure(state="normal")
            self.player1_sure_button.bind("<ButtonRelease-1>",self.Confirm_Player)
            
        elif self.selected_player_index[1]==0 and self.temp_player_index!=self.selected_player_index[0]:
            
            self.selected_player_label2.configure(image=self.players_address[self.temp_player_index])
            
            
    def Exit_Button_Event(self,event):
        if event.x>=0 and event.x<=17:
            if event.y>=0 and event.y<=17:
                self.parent.Quit()
            else:
                pass
        else:
            pass

    def Page_Turn_Event(self,event):
        if event.x>=0 and event.x<=69:
            if event.y>=0 and event.y<=34:
                temp_id=event.widget.cget("text")
                if temp_id=="selection_page_prev":
                    self.parent.page_id=temp_id
                    self.parent.Page_Close()
                    self.destroy()
                elif temp_id=="selection_page_next":
                    if self.selected_player_index[0]!=0 and self.selected_player_index[1]!=0:
                        self.parent.selected_player_index=self.selected_player_index
                        self.parent.page_id=temp_id
                        self.parent.Page_Close()
                        self.destroy()
                    else:
                        pass
            else:
                pass
        else:
            pass

#-----------------------------------------------------------------------------------------------------------------------------------
        

class Ludoo_Playing(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,controller)
        self.pack()

        self.parent=parent
        
        self.configure(height=self.parent.y_dim,width=self.parent.x_dim,bg="#262626")

        self.main_canvas=tk.Canvas(self,height=self.parent.My_App_Height,width=self.parent.My_App_Width,
                                   bg="red",highlightthickness=1,highlightbackground="#81d7e1")
        self.main_canvas.place(x=((self.parent.x_dim)-(self.parent.My_App_Width))/2,
                               y=((self.parent.y_dim)-(self.parent.My_App_Height))/2)

        open_dairy_image=ImageTk.PhotoImage(file="./initials/dp.jpg")
        self.open_dairy_image=open_dairy_image

        self.main_canvas.create_image(1,1,image=open_dairy_image,anchor="nw")

        exit_button_image=ImageTk.PhotoImage(file="./initials/close2.jpg")

        self.exit_button_image=exit_button_image

        self.exit_button=tk.Label(self.main_canvas,image=exit_button_image,bd=0,
                                  cursor="hand2")
        self.exit_button.bind("<ButtonRelease-1>",self.Exit_Button_Event)
        
        self.exit_button.place(x=779,y=3)

        self.players_address={1:ImageTk.PhotoImage(file="./selection/motu.jpg"),
                              2:ImageTk.PhotoImage(file="./selection/john.jpg"),
                              3:ImageTk.PhotoImage(file="./selection/ghasitaram.jpg"),
                              4:ImageTk.PhotoImage(file="./selection/jhatka.jpg"),
                              5:ImageTk.PhotoImage(file="./selection/bheem.jpg"),
                              6:ImageTk.PhotoImage(file="./selection/kalia.jpg"),
                              7:ImageTk.PhotoImage(file="./selection/raju.jpg"),
                              8:ImageTk.PhotoImage(file="./selection/chhutki.jpg")
                              }
        self.dice_digits={0:ImageTk.PhotoImage(file="./dice_board/erase_dice.jpg"),
                          1:ImageTk.PhotoImage(file="./dice_board/one_up.jpg"),
                          2:ImageTk.PhotoImage(file="./dice_board/two_up.jpg"),
                          3:ImageTk.PhotoImage(file="./dice_board/three_up.jpg"),
                          4:ImageTk.PhotoImage(file="./dice_board/four_up.jpg"),
                          5:ImageTk.PhotoImage(file="./dice_board/five_up.jpg"),
                          6:ImageTk.PhotoImage(file="./dice_board/six_up.jpg")
                          }

        self.temp_choice=tk.IntVar()
        self.win_key=1


        self.player1=tk.Label(self.main_canvas,image=self.players_address[self.parent.selected_player_index[0]],
                              relief="flat",bd=0)
        self.player1.place(x=70,y=65)

        self.player2=tk.Label(self.main_canvas,image=self.players_address[self.parent.selected_player_index[1]],
                              relief="flat",bd=0)
        self.player2.place(x=585,y=65)

#-----------------------------win_key_Label_Frame_&_Radiobuttons----------------------------------------------

        self.win_option_frame=tk.LabelFrame(self.main_canvas,text="Winning Key",bg="#d2c5b4",relief="flat",bd=0)
        self.win_option_frame.place(x=230,y=65)

        self.win_option1=tk.Radiobutton(self.win_option_frame,text="Odd",value=1,variable=self.temp_choice,bg="#d2c5b4",fg="red",
                                        command=self.Set_Winning_Key)
        self.win_option1.pack()
        self.win_option1.select()

        self.win_option2=tk.Radiobutton(self.win_option_frame,text="Even",variable=self.temp_choice,value=0,bg="#d2c5b4",
                                        command=self.Set_Winning_Key)
        self.win_option2.pack()
        

#-----------------------Timer_Label_Frame--------------------------------------------------

        self.timer_frame=tk.LabelFrame(self.main_canvas,text="Set Timer",relief="flat",bg="#d2c5b4",bd=0)
        self.timer_frame.place(x=310,y=65)

        self.timer=tk.Spinbox(self.timer_frame,from_=1,to=30,width=2,justify="left",bd=0,relief="flat",bg="#d2c5b4",
                              disabledbackground="#d2c5b4")
        self.timer.pack()

#--------------------------Start_Game_Button----------------------------------------------------------------------------

        ok_image=ImageTk.PhotoImage(file="./dice_board/ok_game.jpg")
        self.ok_image=ok_image
        
        self.start_game_button=tk.Label(self.main_canvas,text="Start Game",image=ok_image,relief="flat",bg="#d2c5b4",
                                        bd=0,cursor="hand2")
        self.start_game_button.place(x=470,y=75)
        self.start_game_button.bind("<ButtonRelease-1>",self.Set_Game_Value)

#-------------------------Time_Shower_LabelFrame--------------------------------------------------------------------------

        self.rem_timer_show_frame=tk.LabelFrame(self.main_canvas,text="Remaining Time",bg="#d2c5b4",bd=0,relief="flat")
        self.rem_timer_show_frame.place(x=230,y=150)
        
        self.rem_time_label=tk.Label(self.rem_timer_show_frame,text="0 : 00",bg="#d2c5b4",bd=0,relief="flat",state="disabled")
        self.rem_time_label.pack()

        self.elap_timer_show_frame=tk.LabelFrame(self.main_canvas,text="Elapsed Time",bg="#d2c5b4",bd=0,relief="flat")
        self.elap_timer_show_frame.place(x=480,y=150)

        self.elap_time_label=tk.Label(self.elap_timer_show_frame,text="0 : 00",bd=0,relief="flat",bg="#d2c5b4",state="disabled")
        self.elap_time_label.pack()
        

#---------------------------------------------------------------------------------------------------------------------------        

        chingam_image=ImageTk.PhotoImage(file="./dice_board/half_chingam.jpg")
        self.chingam_image=chingam_image

        self.main_canvas.create_image(352,126,image=chingam_image,anchor="nw")

        board_image=ImageTk.PhotoImage(file="./dice_board/dice_board.jpg")
        self.board_image=board_image

        
        self.dice_board_canvas=tk.Canvas(self.main_canvas,height=312,width=692,bg="green",state="disabled",
                                         highlightthickness=0)
        self.dice_board_canvas.place(x=54,y=237)
 
        self.dice_board_canvas.create_image(-1,0,image=board_image,anchor="nw")

        self.dice_board_canvas.create_text(285,55,anchor="w",text="Completed Turns ")

        self.ct_counter=self.dice_board_canvas.create_text(390,55,anchor="w",text="0")

#-------------------------Stopped_Dice_Cup---------------------------------------------------------------------        

        dice_cup_image=ImageTk.PhotoImage(file="./dice_board/dice_cup.jpg")

        self.dice_cup_image=dice_cup_image

        self.stopped_dice_cup=self.dice_board_canvas.create_image(5,158,image=dice_cup_image,anchor="nw")

#---------------------------------------------------------------------------------------------------------------        

        rolled_left_dice_cup_image=ImageTk.PhotoImage(file="./dice_board/left_cup.jpg")

        self.rolled_left_dice_cup_image=rolled_left_dice_cup_image
        
        

        rolled_right_dice_cup_image=ImageTk.PhotoImage(file="./dice_board/right_cup.jpg")

        self.rolled_right_dice_cup_image=rolled_right_dice_cup_image
        
#---------------------------------------hand_image_&_its_event----------------------------------------------------

        left_hand_image=ImageTk.PhotoImage(file="./dice_board/left_page_hand.jpg")

        self.left_hand_image=left_hand_image

        self.left_hand_button=tk.Label(self.dice_board_canvas,image=left_hand_image,bd=0,relief="flat",bg="#d2c5b4",
                                      cursor="circle",text="left_player")
        self.left_hand_button.place(x=105,y=270)
        
        
#-------------                                                                 ------------------------------------
        
        right_hand_image=ImageTk.PhotoImage(file="./dice_board/right_page_hand.jpg")

        self.right_hand_image=right_hand_image

        self.right_hand_button=tk.Label(self.dice_board_canvas,image=right_hand_image,bd=0,relief="flat",bg="#d2c5b4",
                                       cursor="circle",text="right_player")
        self.right_hand_button.place(x=530,y=270)

#-------------------------------------------------------------------------------------------------------------------
        
    
        
        self.parent.points_table=[]
        self.game_on_flag=0
        self.total_time=0
        self.temp_total_time=0
        
        self.point_flag=0       # for determining the point value is displayed or not
        
        self.counter=1          # count and display total turns on dice board
        self.temp_marks=[0,0]
        

    def Set_Game_Value(self,event):
        if event.x>=0 and event.x<=66:
            if event.y>=0 and event.y<=34:
                self.temp_total_time=self.total_time=(int(self.timer.get()))*60
                
                self.game_on_flag=1
                
                self.win_option1.configure(state="disabled")
                self.win_option2.configure(state="disabled")
                
                self.timer.configure(state="disabled")
                
                event.widget.unbind("<ButtonRelease-1>")
                event.widget.configure(state="disabled")
                
                self.rem_time_label.configure(state="normal")
                self.elap_time_label.configure(state="normal")

                self.left_hand_button.configure(state="normal")
                self.left_hand_button.bind("<ButtonRelease-1>",self.Roll_Dice)

                self.right_hand_button.configure(state="disabled")

                self.Game_Timer()
                
                

    def Set_Winning_Key(self):
        self.win_key=self.temp_choice.get()
        if self.win_key==1:
            self.win_option1.configure(fg="red")
            self.win_option2.configure(fg="black")
        elif self.win_key==0:
            self.win_option1.configure(fg="black")
            self.win_option2.configure(fg="red")
            
    
    
    def Result_Timer(self):
        global temp_total_time
        if self.temp_total_time==0:
            self.Auto_Page_Turn()
            return
            
            
        self.temp_total_time-=1
        self.seconds_label.configure(text=str(self.temp_total_time))
        self.seconds_label.after(1000,self.Result_Timer)
        
    def After_Time_Out(self):
        
        self.temp_total_time=10                              # set 9 for result announcing seconds
                
        time_out_image=ImageTk.PhotoImage(file="./dice_board/time_out.jpg")
        self.time_out_image=time_out_image

        self.elap_timer_show_frame.place_forget()
        
        self.tout=self.main_canvas.create_image(433,127,image=time_out_image,anchor="nw")
                        
        self.rem_time_label.configure(state="disabled")

        self.left_hand_button.configure(state="normal")
        self.left_hand_button.unbind("<ButtonRelease-1>")

        self.right_hand_button.configure(state="normal")
        self.right_hand_button.unbind("<ButtonRelease-1>")

        self.result_announcement_label=tk.Label(self.dice_board_canvas,text="Result Announcement will be in",bg="#038137",
                                                relief="flat",bd=0)
        self.result_announcement_label.place(x=260,y=90)

        self.seconds_label=tk.Label(self.dice_board_canvas,text=" ",font=("Helvetica","50"),bg="#038137",
                                    relief="flat",bd=0)
        self.seconds_label.place(x=330,y=120)

        self.dice_board_canvas.create_text(330,220,anchor="w",text="Seconds")

        self.Result_Timer()

    def Game_Timer(self):
        global total_time
        global temp_total_time
        
        if self.temp_total_time==0:
            self.game_on_flag=0
            self.After_Time_Out()
            return
        
        self.temp_total_time-=1
        rem_temp_min=self.temp_total_time/60
        rem_temp_secs=self.temp_total_time%60

        elap_temp_min=((self.total_time) - (self.temp_total_time))/60
        elap_temp_secs=((self.total_time) - (self.temp_total_time))%60
        
        self.rem_time_label.configure(text=str(rem_temp_min)+" : "+str(rem_temp_secs))
        self.elap_time_label.configure(text=str(elap_temp_min)+" : "+str(elap_temp_secs))
        self.elap_time_label.after(1000,self.Game_Timer)

        
    def Roll_Dice(self,event):
        if self.game_on_flag!=1:                                                #game_on_flag is for when the game has to be end then reset this flag
            return
        
        temp_id=event.widget.cget("text")
        
        if event.x>=0 and event.x<=54:
            if event.y>=0 and event.y<=34:
                if temp_id=="left_player":
                    self.left_hand_button.configure(state="disabled")
                    self.left_hand_button.unbind("<ButtonRelease-1>")            # disable by click_event after clicking one time
                if temp_id=="right_player":
                    self.right_hand_button.configure(state="disabled")
                    self.right_hand_button.unbind("<ButtonRelease-1>")           # disable by click_event after clicking one time
                
                y_dist=158                                                      # y_dist is for stopped cup liffiting up
                
                while True:
                    self.dice_board_canvas.move(self.stopped_dice_cup,0,-1)
                    time.sleep(0.00098)
                    self.parent.update()
                    y_dist-=1
                    if y_dist<50:
                        if temp_id=="left_player":
                            self.dice_board_canvas.delete(self.stopped_dice_cup)
                            lcup=self.dice_board_canvas.create_image(34,8,image=self.rolled_left_dice_cup_image,anchor="nw")
                            break
                        elif temp_id=="right_player":
                            self.dice_board_canvas.delete(self.stopped_dice_cup)
                            rcup=self.dice_board_canvas.create_image(496,8,image=self.rolled_right_dice_cup_image,anchor="nw")
                            break
                    

                self.Rolling(temp_id)                                           #temp_digit is to store the final dice score after rolling
                
                if temp_id=="left_player":
                    self.dice_board_canvas.delete(lcup)

                    if self.game_on_flag==0:
                        self.stopped_dice_cup=self.dice_board_canvas.create_image(5,158,image=self.dice_cup_image,anchor="nw")
                        return
                    self.stopped_dice_cup=self.dice_board_canvas.create_image(575,158,image=self.dice_cup_image,anchor="nw")
                    
                    self.right_hand_button.configure(state="normal")
                    self.right_hand_button.bind("<ButtonRelease-1>",self.Roll_Dice)
                    
                            
                elif temp_id=="right_player":
                    self.dice_board_canvas.delete(rcup)

                    self.stopped_dice_cup=self.dice_board_canvas.create_image(5,158,image=self.dice_cup_image,anchor="nw")

                    if (self.game_on_flag==0 and self.point_flag==1) or (self.game_on_flag==1 and self.point_flag==1):  #here point_flag checks whether right player gets marks at finishing time or not
                        self.parent.points_table.append(self.temp_marks)          # storing the marks of both player for one turn
                            
                    self.temp_marks=[0,0]                                           # to erase the previous marks

                    self.counter+=1

                    self.point_flag=0
                    
                    self.left_hand_button.configure(state="normal")
                    self.left_hand_button.bind("<ButtonRelease-1>",self.Roll_Dice)

                    
                            
                else:
                    pass
            else:
                pass
        else:
            pass

        

        
        
         
                
    def Rolling(self,temp_id):
        rolling_digit_show=[1,2,3,4,5,6]        
        
        self.dice_label=tk.Label(self.dice_board_canvas,bd=0,relief="flat")
        
        if temp_id=="left_player":
            self.dice_label.place(x=180,y=114)
        elif temp_id=="right_player":
            self.dice_label.place(x=440,y=114)
            
        flag=0
        
        if temp_id=="left_player":
            x_coord=180
        elif temp_id=="right_player":
            x_coord=440
            
        y_coord=114
        
        while True:
            if self.game_on_flag!=1:
                break        
            time.sleep(0.009)
            random.shuffle(rolling_digit_show)
            
            temp_digit=random.choice(rolling_digit_show)
            
            self.dice_label.configure(image=self.dice_digits[temp_digit])
            self.dice_label.configure(self.dice_label.place(x=x_coord,y=y_coord))
            self.parent.update()            

            if temp_id=="left_player":                
                x_coord+=1
                if x_coord>440:
                    break     
            elif temp_id=="right_player":                
                x_coord-=1
                if x_coord<180:
                    break
                        
            if flag==0:                
                y_coord+=0.5
                if y_coord>=184:
                    flag=1
                
            if flag==1:                
                y_coord-=0.5

        if self.game_on_flag==0:
            self.dice_label.destroy()
            return
        
        self.Calc_Marks(temp_digit,temp_id)
        
        self.dice_label.configure(image=self.dice_digits[0])

    def Calc_Marks(self,tdigit,tid):
        if tid=="right_player":
            self.point_flag=1
            
        if self.win_key==0:
            if tid=="left_player":
                if tdigit%2==0:
                    if tdigit==6:
                        self.temp_marks[0]=5
                        msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+5 point")
                    else:
                        self.temp_marks[0]=1
                        msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+1 point")
                else:
                    self.temp_marks[0]=0
                    msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+0 point")
            elif tid=="right_player":
                if tdigit%2==0:
                    if tdigit==6:
                        self.temp_marks[1]=5
                        msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+5 point")
                    else:
                        self.temp_marks[1]=1
                        msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+1 point")
                else:
                    self.temp_marks[1]=0
                    msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+0 point")
                    
        elif self.win_key==1:
            if tid=="left_player":
                if tdigit%2!=0:
                    if tdigit==1:
                        self.temp_marks[0]=5
                        msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+5 point")
                    else:
                        self.temp_marks[0]=1
                        msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+1 point")
                else:
                    self.temp_marks[0]=0
                    msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+0 point")
            elif tid=="right_player":
                if tdigit%2!=0:
                    if tdigit==1:
                        self.temp_marks[1]=5
                        msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+5 point")
                    else:
                        self.temp_marks[1]=1
                        msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+1 point")
                else:
                    self.temp_marks[1]=0
                    msg=self.dice_board_canvas.create_text(325,120,anchor="w",text="+0 point")
        if tid=="right_player":
            self.dice_board_canvas.itemconfigure(self.ct_counter,text=str(self.counter))

        y=120
        
        while y>90:
            self.dice_board_canvas.move(msg,0,-1)
            self.parent.update()
            time.sleep(0.02)
            y-=1
            if self.game_on_flag!=1:
                self.dice_board_canvas.delete(msg)
                break
            
        self.dice_board_canvas.delete(msg)
        if self.game_on_flag==0:
            return
        
        time.sleep(0.5)

#-----------------------------------------------------------------------

    def Auto_Page_Turn(self):
        self.parent.page_id="result_request"
        self.parent.Page_Close()
        self.destroy()       

#------------Exit_Button_Event---------------------------------------------------
        
    def Exit_Button_Event(self,event):
        if event.x>=0 and event.x<=17:
            if event.y>=0 and event.y<=17:
                self.parent.Quit()
            else:
                pass
        else:
            pass

#-------------------------------------------------------------------------------------------

        
class Play_Result(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,controller)
        self.pack()

        self.parent=parent
        
        self.configure(height=self.parent.y_dim,width=self.parent.x_dim,bg="#262626")

        self.main_canvas=tk.Canvas(self,height=self.parent.My_App_Height+2,width=self.parent.My_App_Width+2,bg="#81d7e1",highlightthickness=0)
        self.main_canvas.place(x=((self.parent.x_dim)-(self.parent.My_App_Width))/2,
                               y=((self.parent.y_dim)-(self.parent.My_App_Height))/2)
        #self.main_canvas.bind("<ButtonRelease-1>",self.main_focus)

        open_dairy_image=ImageTk.PhotoImage(file="./winner/winner_dp.jpg")
        self.open_dairy_image=open_dairy_image

        self.main_canvas.create_image(1,1,image=open_dairy_image,anchor="nw")

#---------------------------------------------------------------------------------------------------        

        self.winner_details_canvas=tk.Canvas(self.main_canvas,height=188,width=216,bg="#d2c5b4",
                                             highlightthickness=0,highlightbackground="blue")
        self.winner_details_canvas.place(x=80,y=70)

#----------------------------------------------------------------------------------------------------        

        winner_banner_image=ImageTk.PhotoImage(file="./winner/winner_banner.jpg")
        self.winner_banner_image=winner_banner_image

        looser_banner_image=ImageTk.PhotoImage(file="./winner/looser_banner.jpg")
        self.looser_banner_image=looser_banner_image

        self.b1=self.winner_details_canvas.create_image(0,0,image=winner_banner_image,anchor="nw")
        self.b2=self.winner_details_canvas.create_image(0,0,image=looser_banner_image,anchor="nw")

        self.winner_details_canvas.lift(self.b1)
#---------------------------------------------------------------------------------------------------

        self.winner_image_canvas=tk.Canvas(self.main_canvas,height=156,width=98,highlightthickness=0)
        self.winner_image_canvas.place(x=342,y=7)

#-----------------------------------------------------------------------------------------------------
        
        self.looser_button=tk.Label(self.main_canvas,text="See Looser",bg="#d2c5b4",relief="solid",
                                    bd=1,cursor="hand2",height=1,width=10)
        
        self.looser_button.place(x=160,y=270)

#------------------------------------------------------------------------------------------------------

        certificate_image=ImageTk.PhotoImage(file="./winner/certificate_no1.jpg")
        self.certificate_image=certificate_image

        self.certificate_label=tk.Label(self.main_canvas,image=certificate_image,bd=0,
                                        relief="flat")
        self.certificate_label.place(x=470,y=70)

        winning_cup_locked_image=ImageTk.PhotoImage(file="./winner/locked_cup_treasure.jpg")
        self.winning_cup_locked_image=winning_cup_locked_image


        self.cup_treasure_label=tk.Label(self.main_canvas,image=winning_cup_locked_image,
                                         bd=0,relief="flat")
        self.cup_treasure_label.place(x=598,y=70)


#----------------------------------------------------------------------------------------------------------        

        replay_image=ImageTk.PhotoImage(file="./winner/replay.jpg")
        self.replay_image=replay_image

        self.replay_button=tk.Label(self.main_canvas,image=replay_image,bd=0,relief="flat",text="page_turn",
                                    cursor="hand2")
        self.replay_button.place(x=385,y=500)
        self.replay_button.bind("<ButtonRelease-1>",self.Page_Turn_Event)

#-------------------------------------------------------------------------------------------------------------
        
        self.treasure_point_label=tk.Label(self.main_canvas,text="Needs 500 points",bg="#d2c5b4",relief="flat",bd=0,
                                           height=1,width=14)
        self.treasure_point_label.place(x=635,y=314)

        self.show_winners_list_button=tk.Label(self.main_canvas,text="Treasure Winners",relief="solid",bd=1,height=1,width=14,
                                               bg="#d2c5b4",cursor="hand2")
        self.show_winners_list_button.place(x=636,y=340)
        self.show_winners_list_button.bind("<ButtonRelease-1>",self.Show_List)

#--------------------------------------------------------------------------------------------------------------
        exit_button_image=ImageTk.PhotoImage(file="./initials/close2.jpg")

        self.exit_button_image=exit_button_image

        self.exit_button=tk.Label(self.main_canvas,image=exit_button_image,bd=0,
                                  cursor="hand2")
        self.exit_button.bind("<ButtonRelease-1>",self.Exit_Button_Event)
        
        self.exit_button.place(x=779,y=3)
        

#============================================================================================================================        

        self.players_full_details={1:(ImageTk.PhotoImage(file="./winner/motu.jpg"),"Motu"),
                                   2:(ImageTk.PhotoImage(file="./winner/john.jpg"),"John"),
                                   3:(ImageTk.PhotoImage(file="./winner/ghasitaram.jpg"),"Ghasitaram"),
                                   4:(ImageTk.PhotoImage(file="./winner/jhatka.jpg"),"Dr Jhatka"),
                                   5:(ImageTk.PhotoImage(file="./winner/bheem.jpg"),"Bheem"),
                                   6:(ImageTk.PhotoImage(file="./winner/kalia.jpg"),"Kalia"),
                                   7:(ImageTk.PhotoImage(file="./winner/raju.jpg"),"Raju"),
                                   8:(ImageTk.PhotoImage(file="./winner/chutki.jpg"),"Chutki")
                                   }

        self.winner_index=0
        self.looser_index=0
        
        self.player_img1=None
        self.player_img2=None
        
        self.tie_index=[0,0]
        self.tie_flag=0
        self.list_show_flag=0
        self.list_file_flag=0
        
        
        self.Calculate_Total()
        self.Determining_Winner()
        self.Determining_Texts()

    def After_Winning_Treasure(self):
        self.show_winners_list_button.place_forget()
        self.congratulation_msg_label=tk.Label(self.main_canvas,text="Congratulations!!!\nYou Got It",relief="flat",bg="#d2c5b4",bd=1)
        self.congratulation_msg_label.place(x=636,y=335)
                
        self.add_name_button=tk.Label(self.main_canvas,text="Add Name",bg="#d2c5b4",relief="solid",bd=1,cursor="hand2",width=15,height=1)
        self.add_name_button.place(x=636,y=370)
        self.add_name_button.bind("<ButtonRelease-1>",self.Add_Name)
        

    def Show_List(self,event):
     
        global list_show_flag
        global list_file_flag
        temp_winners_list=[]
        
        if event.x>=0 and event.x<=108:
            if event.y>=0 and event.y<=18:
                
                event.widget.configure(text="Hide List")
                self.list_show_flag=1
                
                if self.list_show_flag==1:
                    event.widget.unbind("<ButtonRelease-1>")
                    event.widget.bind("<ButtonRelease-1>",self.Hide_List)
                    
                if self.list_file_flag==0:
                    self.winners_list_main_frame=tk.Frame(self.main_canvas)      #initiazing frame to contain listbox
                    
                    self.winners_list_sub_frame=tk.Frame(self.winners_list_main_frame)
                    self.winners_list_sub_frame.pack(side="top")
                    
                    self.x_scroll=tk.Scrollbar(self.winners_list_main_frame,orient="horizontal",width=14)
                    self.x_scroll.pack(fill="x",side="bottom")
                    

                    self.y_scroll=tk.Scrollbar(self.winners_list_sub_frame,orient="vertical",width=14)
                    self.y_scroll.pack(side="right",fill="y")
                    
                    
                    self.winners_list=tk.Listbox(self.winners_list_sub_frame,width=15,height=8,bg="#d2c5b4",
                                                 yscrollcommand=self.y_scroll.set,xscrollcommand=self.x_scroll.set,bd=0)   #initialize listbox
                    self.winners_list.pack(side="left")

                    self.y_scroll.configure(command=self.winners_list.yview)
                    self.x_scroll.configure(command=self.winners_list.xview)
                
                    
                    fp=open(".\game_docs\winner_list.txt","r")
                    for name in fp:                                                     #      name variable gets one line from file pointer 
                        self.winners_list.insert("end",(' '.join(name.split())).capitalize())         #.split() removes "\n" and return list of words
                        
                    fp.close()
                    self.list_file_flag=1
                    
                self.winners_list_main_frame.place(x=636,y=360)
            else:
                pass
        else:
            pass
                
        
    def Hide_List(self,event):
        
        global list_show_flag
        if event.x>=0 and event.x<=108:
            if event.y>=0 and event.y<=18:
                event.widget.configure(text="Treasure Winners")
                self.list_show_flag=0

                if self.list_show_flag==0:
                    event.widget.unbind("<ButtonRelease-1>")
                    event.widget.bind("<ButtonRelease-1>",self.Show_List)

                self.winners_list_main_frame.place_forget()        

     
    def Add_Name(self,event):
        if event.x>=0 and event.x<=108:
            if event.y>=0 and event.y<=18:
                self.congratulation_msg_label.place_forget()
                
                self.name_entry_box=tk.Entry(self.main_canvas,relief="solid",width=17)
                self.name_entry_box.place(x=636,y=340)
                self.name_entry_box.configure(fg="grey")
                self.name_entry_box.insert(0,"Winner Name Here")
                self.name_entry_box.bind("<ButtonRelease-1>",self.On_Entryclick)
                
                self.add_name_button.configure(text="Add")
                self.add_name_button.bind("<ButtonRelease-1>",self.Retrieve_Name)                
                self.add_name_button.place_configure(x=636,y=370)
                


    def On_Entryclick(self,event):
        if self.name_entry_box.get()=="Winner Name Here":
            self.name_entry_box.delete(0,len("Winner Name Here"))
            self.name_entry_box.insert(0,"")
            self.name_entry_box.configure(fg="black")
            
    def Retrieve_Name(self,event):
        if event.x>=0 and event.x<=108:
            if event.y>=0 and event.y<=18:
                treasure_winner_name=self.name_entry_box.get()
                if treasure_winner_name=="Winner Name Here" or treasure_winner_name=="":
                    pass
                else:
                    self.name_entry_box.place_forget()
                    self.add_name_button.place_forget()
                    fp=open(".\game_docs\winner_list.txt","a")
                    
                    fp.write(treasure_winner_name+"\n")
                    fp.close()
                    
        self.show_winners_list_button.place(x=636,y=340)

       
    def Determining_Texts(self):
        global tie_flag
        
        if self.tie_flag==1:
            self.Tie_Texts()  
        else:
            self.Winner_Texts()
            
        self.Determining_Prizes()

    def Determining_Winner(self):
        global winner_index
        global looser_index
        global tie_index
        global tie_flag
        
        player1=0
        player2=0
    
        player1=self.parent.selected_player_index[0]
        player2=self.parent.selected_player_index[1]
        

        if self.players_full_details[player1][2]>self.players_full_details[player2][2]:
            
            self.winner_index=player1
            self.looser_index=player2
            self.looser_button.bind("<Button-1>",self.Show_Looser_Result)
            self.looser_button.bind("<ButtonRelease-1>",self.Show_Winner_Result)
        
        elif self.players_full_details[player1][2]<self.players_full_details[player2][2]:
            
            self.winner_index=player2
            self.looser_index=player1
            self.looser_button.bind("<Button-1>",self.Show_Looser_Result)
            self.looser_button.bind("<ButtonRelease-1>",self.Show_Winner_Result)
        
        elif self.players_full_details[player1][2]==self.players_full_details[player2][2]:
            self.tie_index[0]=player1
            self.tie_index[1]=player2
            self.tie_flag=1
            
            self.looser_button.configure(text="Show Player2")
            self.looser_button.unbind("<Button-1>")
            self.looser_button.bind("<ButtonRelease-1>",self.Tie_Players_Show)

    
        
    def Tie_Players_Show(self,event):
        global player_img1
        global player_img2
        if event.x>=0 and event.x<=73:
            if event.y>=0 and event.y<=18:
                if event.widget.cget("text")=="Show Player1":
                    self.winner_image_canvas.lift(self.player_img1)
                    self.looser_button.configure(text="Show Player2")
                elif event.widget.cget("text")=="Show Player2":
                    self.winner_image_canvas.lift(self.player_img2)
                    self.looser_button.configure(text="Show Player1")
                
    def Determining_Prizes(self):
        global winner_index
        
        if self.players_full_details[self.winner_index][2]>=250 and self.players_full_details[self.winner_index][2]<=499:
            
            winning_cup_unlocked_image=ImageTk.PhotoImage(file="./winner/without_chain.jpg")
            self.winning_cup_unlocked_image=winning_cup_unlocked_image
            
            self.cup_treasure_label.configure(image=winning_cup_unlocked_image)
            
        if self.players_full_details[self.winner_index][2]>=500:
            
            winning_cup_opened_treasure_image=ImageTk.PhotoImage(file="./winner/open_treasure.jpg")
            self.winning_cup_opened_treasure_image=winning_cup_opened_treasure_image
            
            self.cup_treasure_label.configure(image=winning_cup_opened_treasure_image)
            self.After_Winning_Treasure()
            
            

    def Tie_Texts(self):
        global tie_index
        global winner_index
        global looser_index

        x1=0
        x2=0

        self.winner_index=self.tie_index[0]
        self.looser_index=self.tie_index[1]

        
        if self.winner_index==3:            # because name "ghasitaram" is long so to fit the name value of x is changed
            x1=100
            x2=168
        elif self.looser_index==3:
            x1=100
            x2=156
        else:
            x1=100
            x2=168

        

        

        self.Winner_Texts(x1)
        self.Looser_Texts(x2)
        
    def Winner_Texts(self,x=150):
        global winner_index
        global player_img1
        
        self.player_img1=self.winner_image_canvas.create_image(0,0,image=self.players_full_details[self.winner_index][0],anchor="nw")
        
        txt1=self.winner_details_canvas.create_text(x,40,text=self.players_full_details[self.winner_index][1],anchor="w")
        txt2=self.winner_details_canvas.create_text(x,68,text=self.players_full_details[self.winner_index][2],anchor="w")
        txt3=self.winner_details_canvas.create_text(x,91,text=self.players_full_details[self.winner_index][3],anchor="w")
        txt4=self.winner_details_canvas.create_text(x,118,text=self.players_full_details[self.winner_index][4],anchor="w")
        txt5=self.winner_details_canvas.create_text(x,148,text=self.players_full_details[self.winner_index][5],anchor="w")
        txt6=self.winner_details_canvas.create_text(x,175,text=self.players_full_details[self.winner_index][6],anchor="w")

    def Looser_Texts(self,x=150):
        global looser_index
        global player_img2
        global tie_flag

        if self.tie_flag==1:
            self.player_img2=self.winner_image_canvas.create_image(0,0,image=self.players_full_details[self.looser_index][0],anchor="nw")
            self.winner_image_canvas.lower(self.player_img2)
            
        txt1=self.winner_details_canvas.create_text(x,40,text=self.players_full_details[self.looser_index][1],anchor="w")
        txt2=self.winner_details_canvas.create_text(x,68,text=self.players_full_details[self.looser_index][2],anchor="w")
        txt3=self.winner_details_canvas.create_text(x,91,text=self.players_full_details[self.looser_index][3],anchor="w")
        txt4=self.winner_details_canvas.create_text(x,118,text=self.players_full_details[self.looser_index][4],anchor="w")
        txt5=self.winner_details_canvas.create_text(x,148,text=self.players_full_details[self.looser_index][5],anchor="w")
        txt6=self.winner_details_canvas.create_text(x,175,text=self.players_full_details[self.looser_index][6],anchor="w")
        
        

    def Show_Looser_Result(self,event):
        global b2     
        if event.x_root>=463 and event.x<=522:
            if event.y_root>=354 and event.y_root<=372:
                self.winner_details_canvas.lift(self.b2)
                self.Looser_Texts()
            else:
                pass
        else:
            pass
    def Show_Winner_Result(self,event):
        global b1
        if event.x_root>=463 and event.x<=522:
            if event.y_root>=354 and event.y_root<=372:
                self.winner_details_canvas.lift(self.b1)
                self.Winner_Texts()
            else:
                pass
        else:
            pass
        
    def Page_Turn_Event(self,event):
        if event.x>=0 and event.x<=26:
            if event.y>=0 and event.y<=26:
                self.parent.page_id="selection_page_next"
                self.parent.Page_Close()
                self.destroy()
            else:
                pass
        else:
            pass
    
    def Calculate_Total(self):
        i=0
        player1=None
        player2=None
        
        player1=self.parent.selected_player_index[0]
        player2=self.parent.selected_player_index[1]
        
        while i<2:
            total=0
            t_turns=0
            plus_five=0
            plus_one=0
            plus_zero=0
            temp_tuple=()
            
            for data in self.parent.points_table:
                total=total+data[i]
                if data[i]==5:
                    plus_five+=1
                if data[i]==1:
                    plus_one+=1
                if data[i]==0:
                    plus_zero+=1
                t_turns+=1
            temp_tuple=(total,t_turns,plus_five,plus_one,plus_zero)
            
            if i==0:                
                self.players_full_details[player1]=self.players_full_details[player1]+temp_tuple
            elif i==1:
                self.players_full_details[player2]=self.players_full_details[player2]+temp_tuple
            i+=1

#---------------------------------------------------------------------------------

            

#------------Exit_Button_Event---------------------------------------------------
        
    def Exit_Button_Event(self,event):
        if event.x>=0 and event.x<=17:
            if event.y>=0 and event.y<=17:
                self.parent.Quit()
            else:
                pass
        else:
            pass    
            
        
MyApp=Kids_Ludoo_App()
MyApp.mainloop()
