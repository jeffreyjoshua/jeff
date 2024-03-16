
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


import sqlite3

master = Tk()
master.geometry("10000x10000")
master.title("insurance")
heading1=Label(text ="JEFFREY'S INSURANCE PVT-LTD",bg = "yellow",fg = "red", height = "2", width ="500",font =("Arial",36))
heading1.pack()



def create():
    conn = sqlite3.connect("insurance new.db")
    cursor=conn.cursor()
    conn.execute("CREATE TABLE IF NOT EXISTS vehicle_details(sno integer primary key autoincrement,carmake TEXT , modelname TEXT , year integer ,carvalue integer,accessoriesvalue integer )")
    conn.execute("CREATE TABLE IF NOT EXISTS insured_details(sno integer primary key autoincrement,firstname TEXT , lastname TEXT ,addressl1 TEXT,addressl2 TEXT,state TEXT,city TEXT,dob integer,experience TEXT)")
    conn.execute("CREATE TABLE IF NOT EXISTS policy_details(sno integer primary key autoincrement,policytype TEXT , term TEXT , effdate TEXT)")
    conn.commit()
    conn.close()
create()    





#vehicle details
vehicledet_text = Label(text ="Vehicle Details" ,font =("Arial",24))
vehicledet_text.place(x = 1,y = 310)
#text
carmake_text = Label(text = "Car Make",)
modelname_text = Label(text = "Model Name",)
year_text = Label(text ="Year of Purchased",)
carvalue_text = Label(text = "Car Value",)
accessoriesvalue_text = Label(text = "Accessories Value",)
year_text.place(x = 500,y = 370)
carvalue_text.place(x = 1,y = 440)
carmake_text.place(x = 1,y = 370)
modelname_text.place(x = 240,y = 370)
carvalue_text.place(x = 1,y = 440)
accessoriesvalue_text.place(x =240,y = 440)
#entry
carmake_entry = StringVar()
modelname_entry = StringVar()
year_entry = IntVar()
carvalue_entry = IntVar()
accessoriesvalue_entry = IntVar()
year_entry = ttk.Entry(textvariable = year_entry,width = "10")
carvalue_entry =ttk.Entry(textvariable = carvalue_entry,width = "15")
carmake_entry = ttk.Entry(textvariable = carmake_entry,width = "12")
modelname_entry = ttk.Entry(textvariable = modelname_entry,width = "12")
accessoriesvalue_entry = ttk.Entry(textvariable = accessoriesvalue_entry,width = "12")
year_entry.place(x = 630,y = 370)
carvalue_entry.place(x = 75,y = 440)
carmake_entry.place(x = 70,y = 370)
modelname_entry.place(x = 331,y = 370)
carvalue_entry.place(x = 75,y = 440)
accessoriesvalue_entry.place(x = 370,y =440)




#insured detials
insureddet_text = Label(text ="Insured Details",font =("Arial",24))
insureddet_text.place(x = 1,y = 110)
#text
firstname_text = Label(text = "First Name ",)
lastname_text = Label(text = "Last Name ",)
addressl1_text = Label(text = "Address Line 1",)
addressl2_text = Label(text = "Address Line 2",)
state_text = Label(text ="State",)
city_text = Label(text ="City",)
dob_text = Label(text = "Date Of Birth",)
experience_text = Label(text = "Experience",)
firstname_text.place(x = 1,y = 170)
lastname_text.place(x = 265,y = 170)
addressl1_text.place(x = 1,y = 240)
addressl2_text.place(x = 400,y = 240)
state_text.place(x = 800,y = 240)
city_text.place(x =1040,y = 240)
dob_text.place(x =555,y = 170)
experience_text.place(x =810,y = 170)
#entry
firstname_entry = StringVar()
lastname_entry = StringVar()
addressl1_entry = StringVar()
addressl2_entry = StringVar()
state_entry = StringVar()
city_entry = StringVar()
dob_entry = IntVar()
experience_entry = IntVar()
firstname_entry = ttk.Entry(textvariable = firstname_entry,width = "15")
lastname_entry = ttk.Entry(textvariable = lastname_entry,width = "17")
addressl1_entry = ttk.Entry(textvariable = addressl1_entry,width = "25")
addressl2_entry = ttk.Entry(textvariable = addressl2_entry,width = "25")
state_entry = ttk.Entry(textvariable = state_entry,width = "15")
city_entry = ttk.Entry(textvariable = city_entry,width = "12")
dob_entry = ttk.Entry(textvariable = dob_entry,width = "12")
experience_entry = ttk.Entry(textvariable = experience_entry,width = "9")
firstname_entry.place(x = 80,y = 170)
lastname_entry.place(x =345,y = 170)
addressl1_entry.place(x = 108,y = 240)
addressl2_entry.place(x =508 ,y = 240)
state_entry.place(x = 845,y = 240)
city_entry.place(x =1080,y = 240)
dob_entry.place(x =650,y = 170)
experience_entry.place(x = 900,y = 170)



#policy detials
policydet_text = Label(text ="Policy Details",font =("Arial",24))
policydet_text.place(x = 1,y = 510)
#text
policytype_text = Label(text = "Policy Type",)
term_text = Label(text = "No Of Years(term) ",)
effdate_text = Label(text = "Effective Date Of Insurance",)
policytype_text.place(x = 1,y =570 )
term_text.place(x = 300,y = 570)
effdate_text.place(x =630,y = 570)
#entry
policytype_entry = StringVar()
term_entry = StringVar()
effdate_entry = StringVar()
policytype_entry = ttk.Entry(textvariable = policytype_entry,width = "15")
term_entry = ttk.Entry(textvariable = term_entry,width = "15")
effdate_entry = ttk.Entry(textvariable = effdate_entry,width = "12")
policytype_entry.place(x = 90,y = 570)
term_entry.place(x = 430,y = 570)
effdate_entry.place(x = 820,y = 570)


def savedata():
    conn = sqlite3.connect("insurance new.db")
    cursor=conn.cursor()
    conn.execute("INSERT INTO insured_details(firstname,lastname,addressl1,addressl2,state,city,dob,experience) VALUES (?,?,?,?,?,?,?,?)",(firstname_entry.get(), lastname_entry.get(),addressl1_entry.get(),addressl2_entry.get(),state_entry.get(),city_entry.get(),dob_entry.get(),experience_entry.get()))                 
    conn.execute("INSERT INTO vehicle_details(carmake,modelname,year,carvalue,accessoriesvalue) VALUES (?,?,?,?,?)",(carmake_entry.get(), modelname_entry.get(),year_entry.get(),carvalue_entry.get(),accessoriesvalue_entry.get()))
    conn.execute("INSERT INTO policy_details(policytype,term,effdate) VALUES (?,?,?)",(policytype_entry.get(),term_entry.get(),effdate_entry.get()))

    conn.commit()

    btn2 = ttk. Button(master,text = "register",command=register)
    btn2.place(x=500  , y = 690)

def search():
    try:
        conn = sqlite3.connect("insurance new.db")
        cursor = conn.cursor()
        sql = "SELECT * FROM vehicle_details WHERE carmake = ?"
        cursor.execute(sql, (carmake_entry.get(),))
        result = cursor.fetchone()
        if result:
            modelname_entry.delete(0, END)
            modelname_entry.insert(0, result[2])  
            year_entry.delete(0, END)
            year_entry.insert(0, result[3])  
            carvalue_entry.delete(0, END)
            carvalue_entry.insert(0, result[4])  
            accessoriesvalue_entry.delete(0, END)
            accessoriesvalue_entry.insert(0, result[5])  
        else:
            messagebox.showinfo("No Data", "No data found for the specified car make.")
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

        
        
        
        
    
btn = ttk. Button(master,text = "Submit",command=savedata)
btn.place(x=350  , y = 690)

btn = ttk. Button(master,text = "search",command=search)
btn.place(x=800 , y = 690)

def register():
    
    
    if carmake_entry.get() == "maruti":
        carmake_value = 500
    if modelname_entry.get() == "swift":
        modelname_value = 50
    if modelname_entry.get() == "xl6":
        modelname_value = 60
    if modelname_entry.get() == "ertiga":
        modelname_value = 70
    
    if carmake_entry.get() == "hyuandai":
        carmake_value = 600
    if modelname_entry.get() == "i10":
        modelname_value = 25
    if modelname_entry.get() == "i20":
        modelname_value = 50
    if modelname_entry.get() == "creta":
        modelname_value = 75    

    if carmake_entry.get() == "kia":
        carmake_value = 700   
    if modelname_entry.get() == "seltose":
        modelname_value = 40
    if modelname_entry.get() == "sonet":
        modelname_value = 55
    if modelname_entry.get() == "carnival":
        modelname_value = 80

    
    if  int(carvalue_entry.get()) >= 0 and int(carvalue_entry.get()) <= 100000:
        carpremium = 800
    elif int(carvalue_entry.get()) >= 100001 and int(carvalue_entry.get()) <= 500000:
        carpremium = 1000
    elif int(carvalue_entry.get()) >= 500001 and int(carvalue_entry.get()) <= 1000000:
        carpremium = 1200
    else:
        carpremium = 1400
        

  
   
    accessoriesamt = int(accessoriesvalue_entry.get())*0.05
    total = carmake_value + modelname_value + carpremium + accessoriesamt
    experiencevalue = int(experience_entry.get())/100*total
    totalfinal = total -  experiencevalue

    screen = Tk()
    screen.geometry("500x500")
    screen.title("new tab")
    heading1=Label(screen,text ="JEFFREY'S INSURANCE PVT-LTD",bg = "yellow",fg = "red", height = "1", width ="300",font =("Arial",20))
    heading1.pack()
    amount_text = Label(screen,text =(f"""

Policy Type: {policytype_entry.get()} insurance     Term: {term_entry.get()}

                Effective Date: {effdate_entry.get()}

 
Premium For Carmake =  {carmake_value}

Premium For Model =   +{modelname_value}

Premium For Carvalue =  +{carpremium}

Premium For Accessories =  +{accessoriesamt}


Discount For Experience =  -{experiencevalue}
[{experience_entry.get()}% discount]


TOTAL PREMIUM TO BE PAID =  {totalfinal}

                                      """))
    amount_text.place(x = 10,y =35)

    firstname_entry.delete(0,END)
    lastname_entry.delete(0,END)
    experience_entry.delete(0,END)
    accessoriesvalue_entry.delete(0,END)
    carvalue_entry.delete(0,END)
    carmake_entry.delete(0,END)
    modelname_entry.delete(0,END)
    addressl1_entry.delete(0,END)
    addressl2_entry.delete(0,END)
    state_entry.delete(0,END)
    city_entry.delete(0,END)
    effdate_entry.delete(0,END)
    policytype_entry.delete(0,END)




master.mainloop()

