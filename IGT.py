from  Tkinter import *
import ttk 
import ScrolledText
from Tkinter import Menu
import os
import subprocess
import time

radiovalue=1

win =Tk()
win.title('IGT')
#icon = PhotoImage(file='3.png')
#win.tk.call('wm','iconphoto',win._w,icon)
win.configure(background='black')

scrollbar = Scrollbar(win)
scrollbar.pack(side=RIGHT , fill =Y)

tex = Text(master=win , yscrollcommand=scrollbar.set)
tex.pack(side=RIGHT)

scrollbar.config(command=tex.yview)
#Creating Tab --------------

tabcontrol = ttk.Notebook(win)

tab1_home = ttk.Frame(tabcontrol)
tabcontrol.add(tab1_home,text =" Port Scanning")

tab2_ping = ttk.Frame(tabcontrol)
tabcontrol.add(tab2_ping,text =" Ping ")

tab3_AT = ttk.Frame(tabcontrol)
tabcontrol.add(tab3_AT,text =" Attacks ")

tab4_SI = ttk.Frame(tabcontrol)
tabcontrol.add(tab4_SI,text ="System Info.")

tab5_OS = ttk.Frame(tabcontrol)
tabcontrol.add(tab5_OS,text ="OS Detection")

tab6_SV = ttk.Frame(tabcontrol)
tabcontrol.add(tab6_SV,text = "Service version")

tabcontrol.pack(expand=1, fill="both")

#address entry box
ipadd = StringVar()
ipaddbox = ttk.Entry(tab2_ping , width = 20 ,textvariable = ipadd).grid(column =0 ,row =5 ,padx=35)

#ping packetnumber
ippacketnumber = StringVar()
ippacketnumberbox = ttk.Entry(tab2_ping,width=20 ,textvariable = ippacketnumber).grid(column=0,row=7)

#ping packetnumber
ippacketsize = StringVar()
ippacketsizebox = ttk.Entry(tab2_ping,width=20 ,textvariable = ippacketsize).grid(column=0,row=9)

def _quit():
    win.quit()
    win.destroy()
    exit()
def clear():
    tex.delete(1.0,10000000.0)

def hdinfo():
    tex.delete(1.0,10000000.0)
    proc=subprocess.Popen(['lscpu'],stdout=subprocess.PIPE,shell=True)
    (out,err) = proc.communicate()
    tex.insert(END,out)

def kvinfo():
    tex.delete(1.0,10000000.0)
    proc=subprocess.Popen(['cat /proc/version'],stdout=subprocess.PIPE,shell=True)
    (out,err) = proc.communicate()
    tex.insert(END,out)

def mdinfo():
    tex.delete(1.0,10000000.0)
    proc=subprocess.Popen(['cat /proc/meminfo'],stdout=subprocess.PIPE,shell=True)
    (out,err) = proc.communicate()
    tex.insert(END,out)

def ipinfo():
    tex.delete(1.0,10000000.0)
    proc=subprocess.Popen(['ifconfig'],stdout=subprocess.PIPE,shell=True)
    (out,err) = proc.communicate()
    tex.insert(END,out)

def biosinfo():
    tex.delete(1.0,10000000.0)
    proc=subprocess.Popen(['sudo dmidecode -t bios'],stdout=subprocess.PIPE,shell=True)
    (out,err) = proc.communicate()
    tex.insert(END,out)
    
def pingme():
    tex.delete(1.0,10000000.0)
    str ="4"                                            # default packet number in ping tab
    str1="32"
    if len(ippacketnumber.get())!= 0:
        str=ippacketnumber.get()
    if len(ippacketsize.get()) != 0:
        str1=ippacketsize.get()
    str2=ipadd.get()
    pstr='ping -i 0.01 -c '+str+' -s '+str1+' '+str2

    #os.system('ping -c '+str+' -s '+str1+' '+ ipadd.get())
    proc=subprocess.Popen([pstr],stdout=subprocess.PIPE,shell=True)
    (out,err) = proc.communicate()
    tex.insert(END,out)

def portscan1():
    global selection
    selection = var.get()
    tex.delete(1.0,10000000.0)
    a=pscanip.get()
    b=pscanport.get()
    p1='nmap -sS --top-ports '+b+' '+a+' >ran.txt'
    p2='nmap -sA --top-ports '+b+' '+a+' >ran.txt'
    p3="awk ' /closed/ || /open/ {print $0}' ran.txt"
    p4="awk ' /filtered/ {print $0}' ran.txt"

    if selection==1:
	subprocess.Popen([p1],stdout=subprocess.PIPE,shell=True)
        time.sleep(15)
        proc=subprocess.Popen([p3],stdout=subprocess.PIPE,shell=True)
        (out,err) = proc.communicate()
        tex.insert(END,out)
    else :
        subprocess.Popen([p2],stdout=subprocess.PIPE,shell=True)
        time.sleep(15)
        proc=subprocess.Popen([p4],stdout=subprocess.PIPE,shell=True)
        (out,err) = proc.communicate()
        tex.insert(END,out)
         

def portscan2():
	tex.delete(1.0,10000000.0)
        a=pscanip.get()
        b=pscanport.get()
        p1='nmap -sS -p '+b+' '+a+' >ran.txt'
        p2='nmap -sA -p '+b+' '+a+' >ran.txt'
        p3="awk '/'"+b+"'/ {print $2}' ran.txt"
	subprocess.Popen([p1],stdout=subprocess.PIPE,shell=True)
	time.sleep(15)
	proc=subprocess.Popen([p3],stdout=subprocess.PIPE,shell=True)
        (out,err) = proc.communicate()
        tex.insert(END,out)

        #proc="---------------------------------------------"
	#(out,err) = proc.communicate() 
        #tex.insert(END,out)

        subprocess.Popen([p2],stdout=subprocess.PIPE,shell=True)
	time.sleep(15)
	proc=subprocess.Popen([p3],stdout=subprocess.PIPE,shell=True)
        (out,err) = proc.communicate()
        tex.insert(END,out)
	

def portscan3():
	tex.delete(1.0,10000000.0)
        p1="nmap -A "+pscanip5.get()+" >ran.txt"
	p2="awk ' /OS:/ ||/   OS CPE:/ || /Computer name:/ || /NetBios computer name:/ || /Domain name:/ || /Forest name:/ || /FQDN:/ || /System time:/ || /Workgroup/ || /NetBios MAC/ || /Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed por/ || /All 1000/ {print $0} ' ran.txt "

	subprocess.Popen([p1],stdout=subprocess.PIPE,shell=True)
        time.sleep(100)
	
	proc=subprocess.Popen([p2],stdout=subprocess.PIPE,shell=True)
        (out,err) = proc.communicate()
        tex.insert(END,out)

def sel1():
	portscanlabel.config(text="Enter top ports :")
        R1.configure(state=NORMAL)
        R2.configure(state=NORMAL)
        scanbutton.configure(command=portscan1)

def sel2():
	portscanlabel.config(text="Enter ports No. :")
        R1.configure(state=DISABLED)
        R2.configure(state=DISABLED)
	scanbutton.configure(command=portscan2)
def server():
	tex.delete(1.0,10000000.0)
        a=pscanip2.get()
        b=pscanport2.get()
        p1='nmap -A -p '+b+' '+a+' >ran.txt'
        p2="awk '/'"+b+"'/ {print $0}' ran.txt"
	subprocess.Popen([p1],stdout=subprocess.PIPE,shell=True)
	time.sleep(40)
	proc=subprocess.Popen([p2],stdout=subprocess.PIPE,shell=True)
        (out,err) = proc.communicate()
        tex.insert(END,out)

def ddospannel():
	print('hello')
	pnumlabel.configure(text="Number of Packets :")
	portlabel.configure(state=NORMAL)
	flaglabel.configure(state=NORMAL)  
	desportbox.configure(state=NORMAL) 
	flagbox.configure(state=NORMAL)

	attackbutton.configure(command=ddosattack)

def smurfpannel():
    
	pnumlabel.configure(text = "Broadcast IP    :")
	portlabel.configure(state=DISABLED)
	flaglabel.configure(state=DISABLED)  
	desportbox.configure(state=DISABLED) 
	flagbox.configure(state=DISABLED)

	attackbutton.configure(command=ddosattack)
 
 
def ddosattack():
    str ='hping3 -c '+npack.get()+' -p '+desport.get()+' -'+flag.get()+' '+desip.get()
    print(str)
    os.system('hping3 -c '+npack.get()+' -p '+desport.get()+' -'+flag.get()+' '+desip.get())

def smurfattack():
    os.system('hping3 -1 --flood -a '+desip.get()+' '+npack.get())
#Tab 1 scanning .........
#labels
var=IntVar()
pscanip = StringVar()
pscanport =StringVar()
ttk.Label(tab1_home, text = "Target IP          :").grid(column=0,row=1)
ttk.Entry(tab1_home, width = 20 ,textvariable = pscanip).grid(column =1 ,row =1)

Radiobutton(tab1_home, text="All ports  ",value=1,command=sel1).grid(column=0,row=0)
Radiobutton(tab1_home, text="Specific port ",value=2,command=sel2).grid(column=1,row=0)


portscanlabel=ttk.Label(tab1_home, text = "Enter top ports :")
portscanlabel.grid(column=0,row=3)
pentry=ttk.Entry(tab1_home, width = 20 ,textvariable = pscanport)
pentry.grid(column =1 ,row =3)

R1=Radiobutton(tab1_home, text="Open/Closed",value=1,variable=var)
R1.grid(column=0,row=4)
R2=Radiobutton(tab1_home, text="Filtered/Unfiltered",value=2,variable=var)
R2.grid(column=0,row=5)

scanbutton=Button(tab1_home, text =" SCAN ",command=portscan1,activebackground='blue')
scanbutton.grid(column=3,row=8)
    
 
#Tab 2 ping items
ttk.Label(tab2_ping , text = " ").grid(column=0,row=0)
ttk.Label(tab2_ping , text = " ").grid(column=0,row=1)
ttk.Label(tab2_ping , text = " ").grid(column=0,row=2)
pingiplabel = ttk.Label(tab2_ping , text = "IP / Host name :").grid(column=0,row=4,)
pingpacketnumber = ttk.Label(tab2_ping , text = "Number of Packets :").grid(column=0,row=6)
pingpacketsize = ttk.Label(tab2_ping , text = "Packets Size :").grid(column=0,row=8)
# creating button
click = Button(tab2_ping, text ="PING",command=pingme,activebackground='blue',height = 2 ,width = 10).grid(column=0,row=10 ,pady=10)

#Tab 4 system info
B0 = Button(tab4_SI, text ="Interface config",command=ipinfo,activebackground='blue',height = 3 ,width = 25).grid(column=0,row=0,padx= 10)
B1 = Button(tab4_SI, text ="Hardware Information",command=hdinfo,activebackground='blue',height = 3 ,width = 25).grid(column=0,row=1)
B2 = Button(tab4_SI, text ="Kernel Version",command=kvinfo,activebackground='blue',height = 3 ,width = 25).grid(column=0,row=2)
B3 = Button(tab4_SI, text ="Memory Details",command=mdinfo,activebackground='blue',height = 3 ,width = 25).grid(column=0,row=3)
B4 = Button(tab4_SI, text ="BIOS Information",command=biosinfo,activebackground='blue',height = 3 ,width = 25).grid(column=0,row=4)

# Tab 3 Attacks items
Button(tab3_AT, text ="DOS Attack",command=ddospannel,activebackground='blue',height = 3 ,width = 25).grid(column=0,row=0,padx= 10)
Button(tab3_AT, text ="Smurf Attack",command=smurfpannel,activebackground='blue',height = 3 ,width = 25).grid(column=1,row=0,padx= 10)
desip = StringVar()
npack = StringVar()
desport = StringVar()
flag = StringVar()

#labels
tgiplabel = ttk.Label(tab3_AT , text = "Target IP                :")
tgiplabel.place(x=80,y=100)
pnumlabel = ttk.Label(tab3_AT , text = "Number of Packets :")
pnumlabel.place(x=80,y=120)
portlabel = ttk.Label(tab3_AT , text = "Destination Port     :")
portlabel.place(x=80,y=140)
flaglabel = ttk.Label(tab3_AT , text = "Packets Type         :")
flaglabel.place(x=80,y=160)  
#entry
desipbox = ttk.Entry(tab3_AT, width = 20 ,textvariable = desip)
desipbox.place(x=210,y=100)
npackbox = ttk.Entry(tab3_AT, width = 20 ,textvariable = npack)
npackbox.place(x=210,y=120)
desportbox = ttk.Entry(tab3_AT, width = 20 ,textvariable = desport)
desportbox.place(x=210,y=140) 
flagbox = ttk.Entry(tab3_AT, width = 20 ,textvariable = flag)
flagbox.place(x=210,y=160)
a=npack.get()
attackbutton = Button(tab3_AT, text ="Launch",command=ddosattack,activebackground='blue',height = 2 ,width = 10)
attackbutton.place(x=300,y=200)
 


# Tab 5 OS Detection
pscanip5 = StringVar()
ttk.Label(tab5_OS , text = "Target IP :").grid(column=0,row=0)
ttk.Entry(tab5_OS, width = 20 ,textvariable = pscanip5).grid(column =0 ,row =1)
Button(tab5_OS, text ="SCAN",command=portscan3,activebackground='blue').grid(column=0,row=11)

# Tab 6 Service version
pscanip2 = StringVar()
pscanport2 =StringVar()
ttk.Label(tab6_SV, text = "Target IP          :").grid(column=0,row=1)
ttk.Entry(tab6_SV, width = 20 ,textvariable = pscanip2).grid(column =1 ,row =1)

portscanlabel2=ttk.Label(tab6_SV, text = "Enter port no :")
portscanlabel2.grid(column=0,row=2)
pentry2=ttk.Entry(tab6_SV, width = 20 ,textvariable = pscanport2)
pentry2.grid(column =1 ,row =2)
Button(tab6_SV, text="SCAN",command=server,activebackground='blue').grid(column=3,row=3)

#creating a menu bar......
menubar = Menu(win)

# create a pulldown menu, and add it to the menu bar

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=clear)
#filemenu.add_separator()                                        #filemenu
filemenu.add_command(label="Exit", command=_quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")                             #helpmenu
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
win.config(menu=menubar)

win.mainloop()
