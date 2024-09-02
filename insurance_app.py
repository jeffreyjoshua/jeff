
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


import sqlite3

def create_tables():
    conn = sqlite3.connect("insurance_new.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS vehicle_details (sno INTEGER PRIMARY KEY AUTOINCREMENT, carmake TEXT, modelname TEXT, year INTEGER, carvalue INTEGER, accessoriesvalue INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS insured_details (sno INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, addressl1 TEXT, addressl2 TEXT, state TEXT, city TEXT, dob INTEGER, experience TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS policy_details (sno INTEGER PRIMARY KEY AUTOINCREMENT, policytype TEXT, term TEXT, effdate TEXT)")
    conn.commit()
    conn.close()

def login_screen():
    global login_frame
    login_frame = Frame(master)
    login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(login_frame, text="Username: ").grid(row=0, column=0, padx=5, pady=5)
    Label(login_frame, text="Password: ").grid(row=1, column=0, padx=5, pady=5)

    global username_entry, password_entry
    username_entry = Entry(login_frame)
    password_entry = Entry(login_frame, show="*")

    username_entry.grid(row=0, column=1, padx=5, pady=5)
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    Button(login_frame, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=5)
    Button(login_frame, text="Sign Up", command=signup_screen).grid(row=3, column=0, columnspan=2, pady=5)

def signup_screen():
    login_frame.destroy()
    global signup_frame
    signup_frame = Frame(master)
    signup_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(signup_frame, text="Username: ").grid(row=0, column=0, padx=5, pady=5)
    Label(signup_frame, text="Password: ").grid(row=1, column=0, padx=5, pady=5)

    global username_entry_signup, password_entry_signup
    username_entry_signup = Entry(signup_frame)
    password_entry_signup = Entry(signup_frame, show="*")

    username_entry_signup.grid(row=0, column=1, padx=5, pady=5)
    password_entry_signup.grid(row=1, column=1, padx=5, pady=5)

    Button(signup_frame, text="Sign Up", command=signup).grid(row=2, column=0, columnspan=2, pady=5)
    Button(signup_frame, text="Back to Login", command=login_screen).grid(row=3, column=0, columnspan=2, pady=5)

def signup():
    username = username_entry_signup.get()
    password = password_entry_signup.get()
    conn = sqlite3.connect("insurance_new.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User created successfully!")
        login_screen()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    conn.close()

def login():
    username = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect("insurance_new.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        messagebox.showinfo("Success", "Login successful!")
        main_screen()
    else:
        messagebox.showerror("Error", "Invalid username or password!")


        

def main_screen():
    login_frame.destroy()

    master.geometry("10000x10000")
    
    heading1=Label(text ="JEFFREY'S INSURANCE PVT-LTD",bg = "yellow",fg = "red", height = "2", width ="500",font =("Arial",36))
    heading1.pack()
  


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
        conn = sqlite3.connect("insurance_new.db")
        cursor=conn.cursor()
        conn.execute("INSERT INTO insured_details(firstname,lastname,addressl1,addressl2,state,city,dob,experience) VALUES (?,?,?,?,?,?,?,?)",(firstname_entry.get(), lastname_entry.get(),addressl1_entry.get(),addressl2_entry.get(),state_entry.get(),city_entry.get(),dob_entry.get(),experience_entry.get()))                 
        conn.execute("INSERT INTO vehicle_details(carmake,modelname,year,carvalue,accessoriesvalue) VALUES (?,?,?,?,?)",(carmake_entry.get(), modelname_entry.get(),year_entry.get(),carvalue_entry.get(),accessoriesvalue_entry.get()))
        conn.execute("INSERT INTO policy_details(policytype,term,effdate) VALUES (?,?,?)",(policytype_entry.get(),term_entry.get(),effdate_entry.get()))

        conn.commit()

        btn2 = ttk. Button(master,text = "Quote",command=register)
        btn2.place(x=500  , y = 690)

    def search():
        try:
            conn = sqlite3.connect("insurance_new.db")
            cursor = conn.cursor()
            # Specify the table name in your query and use placeholders to prevent SQL injection
            sql = "SELECT * FROM vehicle_details WHERE carmake = ?"
            cursor.execute(sql, (carmake_entry.get(),))
            result = cursor.fetchone()
            # Check if result is not None before accessing its elements
            if result:
                # Update entry fields with the fetched data
                modelname_entry.delete(0, END)
                modelname_entry.insert(0, result[2])  # Assuming modelname is at index 2 in the result
                year_entry.delete(0, END)
                year_entry.insert(0, result[3])  # Assuming year is at index 3 in the result
                carvalue_entry.delete(0, END)
                carvalue_entry.insert(0, result[4])  # Assuming carvalue is at index 4 in the result
                accessoriesvalue_entry.delete(0, END)
                accessoriesvalue_entry.insert(0, result[5])  # Assuming accessoriesvalue is at index 5 in the result
            else:
                # Notify the user if no data is found
                messagebox.showinfo("No Data", "No data found for the specified car make.")
            conn.close()
        except Exception as e:
            # Catch and display any exceptions that occur during the process
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

        def save_to_pdf():
            filename = "filename.pdf"
            c = canvas.Canvas(filename, pagesize=letter)
            # Drawing text on the canvas
            c.drawString(100, 750, "Policy Details")
            c.drawString(100, 730, f"Policy Type: {policytype_entry.get()} insurance     Term: {term_entry.get()}")
            c.drawString(100, 710, f"Effective Date: {effdate_entry.get()}")
            c.drawString(100, 690, f"Premium For Carmake =  {carmake_value}")
            c.drawString(100, 670, f"Premium For Model =   +{modelname_value}")
            c.drawString(100, 650, f"Premium For Carvalue =  +{carpremium}")
            c.drawString(100, 630, f"Premium For Accessories =  +{accessoriesamt}")
            c.drawString(100, 610, f"Discount For Experience =  -{experiencevalue} [{experience_entry.get()}% discount]")
            c.drawString(100, 590, f"TOTAL PREMIUM TO BE PAID =  {totalfinal}")
            c.save()
            print(f"PDF saved as {filename}")

        # Add a button in your Tkinter window to trigger the save_to_pdf function
        save_pdf_button = Button(screen, text="Print", command=save_to_pdf)
        save_pdf_button.place(x=150  , y = 690)
        save_pdf_button.pack()
        
        
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

master = Tk()
master.geometry("500x500")
master.title("insurance")


create_tables()
login_screen()

master.mainloop()


    

