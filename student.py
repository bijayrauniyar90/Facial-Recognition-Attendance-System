# Python Imaging Library (expansion of PIL) is the de facto image processing package for Python language
from tkinter import *  # It is library used for making GUI application & software
from tkinter import ttk  # for stylying purposes
from PIL import Image, ImageTk  # For opening and displaying image files
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title = ("attendSure")

        # =============== Variables ====================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_stu_id = StringVar()
        self.var_stu_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # Top img
        img = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\img11.jpg")
        img = img.resize((1700, 150), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1700, height=150)

        # bg img
        img3 = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
        #     "20th Century Font", 30, "bold"), bg="white", fg="darkgreen")
        # title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=40, width=1500, height=650)

        # Left Side Label Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=800, height=620)

        img_left = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\handsup2.jpg")
        img_left = img_left.resize((790, 180), Image.BILINEAR)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=785, height=160)

        # Current Course Information
        current_course_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=17, y=160, width=785, height=120)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=(
            "times new roman", 12, "bold"), bg="white")
        # We make grid --> rows and column
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        # Combo Box
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 13, "bold"), state="read only", width=20)
        dep_combo['values'] = ("Select Department", "CSE",
                               "IT", "Electrical", "Elec.& Tele", "Mechanical", "Civil")
        # set the default value of combo box to first item
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        # Combo Box
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 13, "bold"), state="read only", width=20)
        course_combo['values'] = (
            "Select Course", "B.Tech", "BBA", "BCA", "BioTech", "MTech", "MCA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        # combo box
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 13, "bold"), state="read only", width=20)
        year_combo['values'] = ("Select Year", "2020-21",
                                "2021-22", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        # Check box
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 13, "bold"), state="read only", width=20)
        semester_combo['values'] = ("Select Semester", "Semester-1", "Semester-1", "Semester-2",
                                    "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        Class_Student_course_frame = LabelFrame(
            main_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        Class_Student_course_frame.place(x=17, y=280, width=785, height=340)

        # Student ID
        studentId_label = Label(Class_Student_course_frame, text="StudentId:", font=(
            "times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(Class_Student_course_frame, textvariable=self.var_stu_id, width=20, font=(
            "times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student name
        studenName_label = Label(Class_Student_course_frame, text="Student Name:", font=(
            "times new roman", 13, "bold"), bg="white")
        studenName_label.grid(row=0, column=2, padx=10, sticky=W)

        studentName_entry = ttk.Entry(
            Class_Student_course_frame, textvariable=self.var_stu_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, sticky=W)

        # Class division
        class_div_label = Label(Class_Student_course_frame, text="Class Division:", font=(
            "times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, sticky=W)

        # class_div_entry = ttk.Entry(Class_Student_course_frame, textvariable=self.var_div, width=20, font=(
        #     "times new roman", 13, "bold"))
        # class_div_entry.grid(row=1, column=1, padx=10, sticky=W)

        # combo box
        division_combo = ttk.Combobox(Class_Student_course_frame, textvariable=self.var_div, font=(
            "times new roman", 13, "bold"), state="read only", width=18)
        division_combo['values'] = ("CSE-1", "CSE-2", "CSE-3", "CSE-4", "CSE-5", "CSE-6", "CSE-7", "CSE-8", "CSE-9", "CSE-10", "CSE-11", "CSE-12", "CSE-13", "CSE-14", "CSE-15", "CSE-16", "CSE-17", "CSE-18",
                                    "CSE-19", "CSE-20", "CSE-21", "CSE-22", "CSE-23", "CSE-24", "CSE-25", "CSE-26", "CSE-27", "CSE-28", "CSE-29", "CSE-30", "CSE-31", "CSE-32", "CSE-33", "CSE-34", "CSE-35", "CSE-36", "CSE-37", "CSE-38")
        division_combo.current(0)
        division_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll Number
        roll_no_label = Label(Class_Student_course_frame, text="Roll No:", font=(
            "times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, sticky=W)

        roll_no_entry = ttk.Entry(Class_Student_course_frame, textvariable=self.var_roll,  width=20, font=(
            "times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, sticky=W)

        # Gender
        gender_label = Label(Class_Student_course_frame, text="Gender", font=(
            "times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        # gender_entry = ttk.Entry(Class_Student_course_frame, textvariable=self.var_gender, width=20, font=(
        #     "times new roman", 13, "bold"))
        # gender_entry.grid(row=2, column=1, padx=10, sticky=W)

        # combo box
        gender_combo = ttk.Combobox(Class_Student_course_frame, textvariable=self.var_gender, font=(
            "times new roman", 13, "bold"), state="read only", width=18)
        gender_combo['values'] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date Of Birth
        dob_label = Label(Class_Student_course_frame, text="Date Of Birth:", font=(
            "times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(Class_Student_course_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, sticky=W)

        # Email
        email_label = Label(Class_Student_course_frame, text="Email:", font=(
            "times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(Class_Student_course_frame, textvariable=self.var_email,  width=20, font=(
            "times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, sticky=W)

        # Phone No:
        phone_no_label = Label(Class_Student_course_frame, text="Phone No:", font=(
            "times new roman", 13, "bold"), bg="white")
        phone_no_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_no_entry = ttk.Entry(Class_Student_course_frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 13, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=10, sticky=W)

        # Address
        addresslabel = Label(Class_Student_course_frame, text="Address:", font=(
            "times new roman", 13, "bold"), bg="white")
        addresslabel.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        addressentry = ttk.Entry(Class_Student_course_frame, textvariable=self.var_address, width=20, font=(
            "times new roman", 13, "bold"))
        addressentry.grid(row=4, column=1, padx=10, sticky=W)

        # Teacher Name:
        teacher_label = Label(Class_Student_course_frame, text="Teacher Name:", font=(
            "times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(Class_Student_course_frame, textvariable=self.var_teacher, width=20, font=(
            "times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            Class_Student_course_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(
            Class_Student_course_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1)

        # button Frame
        btn_frame = Frame(Class_Student_course_frame,
                          bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=4, y=190, width=770, height=40)

        # Save button
        save_btn = Button(btn_frame, text="Save", command=self.add_date, width=19, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # update button
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=18, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        # delete button
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=18, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        # reset button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=19, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Sample photo and Update Sample Photo Frame
        btn_frame1 = Frame(Class_Student_course_frame,
                           bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=4, y=250, width=770, height=40)

        # Take a photo sample
        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take photo sample", width=38, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        # Update photo Sample
        update_photo_btn = Button(btn_frame1, text="Update photo sample", width=38, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # Right Side Label Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=820, y=10, width=670, height=620)

        img_right = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\studd.jpg")
        img_right = img_right.resize((780, 130), Image.BILINEAR)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=785, height=130)

        # ============= Search system =============
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=130, width=660, height=70)

        search_label = Label(Search_frame, text="Search By:", font=(
            "times new roman", 15, "bold"), bg="green", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # Check box
        search_combo = ttk.Combobox(Search_frame, font=(
            "times new roman", 12, "bold"), state="read only", width=15)
        search_combo['values'] = (
            "Select", "Name", "Roll Number", "Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Entry Fill
        search_entry = ttk.Entry(
            Search_frame, width=13, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # Search button
        search_btn = Button(Search_frame, text="Search", width=11, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=3)

        # Show All button
        ShowAll_btn = Button(Search_frame, text="Show All", width=11, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        ShowAll_btn.grid(row=0, column=4)

        # ===================== Table Frame in right Side ===================
        # table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        # table_frame.place(x=5, y=210, width=660, height=380)

        # Scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        # Scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
        #                                   "dob", "email", "gender", "phone", "address", "teacher", "photo"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        # # "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob","email", "gender", "phone", "address", "teacher", "photo"
        # Scroll_x.pack(side=BOTTOM, fill=X)
        # Scroll_y.pack(side=RIGHT, fill=Y)
        # Scroll_x.config(command=self.student_table.xview)
        # Scroll_y.config(command=self.student_table.yview)

        # self.student_table.heading("dep", text="Department")
        # self.student_table.heading("course", text="Course")
        # self.student_table.heading("year", text="Year")
        # self.student_table.heading("sem", text="Semester")
        # self.student_table.heading("id", text="StudentId")
        # self.student_table.heading("name", text="Name")
        # self.student_table.heading("div", text="Division")
        # self.student_table.heading("roll", text="RollNo")
        # self.student_table.heading("gender", text="Gender")
        # self.student_table.heading("dob", text="DOB")
        # self.student_table.heading("email", text="Email")
        # self.student_table.heading("phone", text="Phone")
        # self.student_table.heading("address", text="Address")
        # self.student_table.heading("teacher", text="Teacher")
        # self.student_table.heading("photo", text="PhotoSampleStatus")
        # self.student_table["show"] = "headings"

        # self.student_table.column("dep", width=100)
        # self.student_table.column("course", width=100)
        # self.student_table.column("year", width=100)
        # self.student_table.column("sem", width=100)
        # self.student_table.column("id", width=100)
        # self.student_table.column("name", width=100)
        # self.student_table.column("div", width=100)
        # self.student_table.column("roll", width=100)
        # self.student_table.column("gender", width=100)
        # self.student_table.column("dob", width=100)
        # self.student_table.column("email", width=100)
        # self.student_table.column("phone", width=100)
        # self.student_table.column("address", width=100)
        # self.student_table.column("teacher", width=100)
        # self.student_table.column("photo", width=150)

        # self.student_table.pack(fill=BOTH, expand=TRUE)
        # self.student_table.bind("<ButtonRelease>", self.get_cursor)
        # self.fetch_data()

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=690, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "dob",
                                          "email", "gender", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photosample")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ================= Function Declaration ================
    def add_date(self):
        if self.var_dep.get() == "Select Department" or self.var_stu_name.get() == "" or self.var_stu_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                # messagebox.showinfo("Successfull", "Successfully Saved")
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Aang@123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_stu_id.get(),
                    self.var_stu_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", " Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{
                                     str(es)}", parent=self.root)

    # ================== Fetch Data in Table ==================
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Aang@123", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "SELECT * FROM student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
                conn.commit()
        conn.close()

    # ================ Get Cursor ====================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_stu_id.set(data[4])
        self.var_stu_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # ============== Update Function ==================
    # def update_data(self):
    #     if self.var_dep.get() == "Select Department" or self.var_stu_name.get() == "" or self.var_stu_id.get() == "":
    #         messagebox.showerror(
    #             "Error", "All Fields are required", parent=self.root)

    #     else:
    #         try:
    #             Update = messagebox.askyesno(
    #                 "Update", "Do you want to update this student details", parent=self.root)
    #             if Update > 0:
    #                 conn = mysql.connector.connect(
    #                     host="localhost", username="root", password="Aang@123", database="face_recognizer")
    #                 my_cursor = conn.cursor()
    #                 my_cursor.execute("Update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where StudentId=%s",

    #                                   (
    #                                       self.var_dep.get(),
    #                                       self.var_course.get(),
    #                                       self.var_year.get(),
    #                                       self.var_semester.get(),
    #                                       self.var_stu_name.get(),
    #                                       self.var_div.get(),
    #                                       self.var_roll.get(),
    #                                       self.var_gender.get(),
    #                                       self.var_dob.get(),
    #                                       self.var_email.get(),
    #                                       self.var_phone.get(),
    #                                       self.var_address.get(),
    #                                       self.var_teacher.get(),
    #                                       self.var_radio1.get(),
    #                                       self.var_stu_id.get(),
    #                                   ))
    #             else:
    #                 if not Update:
    #                     return

    #             messagebox.showinfo(
    #                 "Success", "Student details successfully update completed", parent=self.root)
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due To:{
    #                                  str(es)}", parent=self.root)

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_stu_name.get() == "" or self.var_stu_id.get() == "":
            messagebox.showerror(
                "Error", "All field are requied", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do ypu want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Aang@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOb=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_stu_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_stu_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Student Details Successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {
                                     str(es)}", parent=self.root)

    # ============== Delete Function ======================
    # def delete_data(self):
    #     if self.var_stu_id.get() == "":
    #         messagebox.showerror(
    #             "Error", "Student id must be required", parent=self.root)
    #     else:
    #         try:
    #             delete = messagebox.askyesno(
    #                 "Student Delete Page", "Do you want to delete this record?", parent=self.root)
    #             if delete > 0:
    #                 conn = mysql.connector.connect(
    #                     host="localhost", username="root", password="Aang@123", database="face_recognizer")
    #                 my_cursor = conn.cursor()

    #                 sql = "delete from student where StudentId=%s"
    #                 val(self.var_stu_id.get(),)
    #                 my_cursor.execute(sql, val)
    #             else:
    #                 if not delete:
    #                     return
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #             messagebox.showinfo(
    #                 "Delete", "Successfully deleted student details", parent=self.root)

    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due To:{
    #                                  str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_stu_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Aang@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_stu_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully delete student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {
                                     str(es)}", parent=self.root)

    # ==================== Reset Function =====================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_stu_id.set("")
        self.var_stu_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ================== Generate DataSet || Take Photo Sample =================
    # def generate_dataset(self):
    #     if self.var_stu_id.get() == "Select Department" or self.var_stu_name.get() == "" or self.var_stu_id.get() == "":
    #         messagebox.showerror(
    #             "Error", "All Fields are required", parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(
    #                 host="localhost", username="root", password="Aang@123", database="face_recognizer")
    #             my_cursor = conn.cursor()
    #             my_cursor.execute("Select * from student")
    #             myresult = my_cursor.fetchall()
    #             id = 0
    #             for x in myresult:
    #                 id += 1

    #             my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOb=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

    #                 self.var_dep.get(),
    #                 self.var_course.get(),
    #                 self.var_year.get(),
    #                 self.var_semester.get(),
    #                 self.var_stu_name.get(),
    #                 self.var_div.get(),
    #                 self.var_roll.get(),
    #                 self.var_gender.get(),
    #                 self.var_dob.get(),
    #                 self.var_email.get(),
    #                 self.var_phone.get(),
    #                 self.var_address.get(),
    #                 self.var_teacher.get(),
    #                 self.var_radio1.get(),
    #                 self.var_stu_id.get() == id+1
    #             ))
    #             conn.commit()
    #             self.fetch_data()
    #             self.reset_data()
    #             conn.close()

    #             # =================== Load predefined data on face frontals from opencv ===============

    #             face_classifier = cv2.CascadeClassifier(
    #                 "haarcascade_frontalface_default.xml")

    #             def face_cropped(img):
    #                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #                 faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    #                 # Scaling Factor=1.3
    #                 # Min Neighbors=5

    #                 for (x, y, w, h) in faces:
    #                     face_cropped = img[y:y+h, x:x+w]
    #                     return face_cropped

    #                 cap = cv2.VideoCapture(0)
    #                 img_id = 0
    #                 while True:
    #                     ret, my_frame = cap.read()
    #                     if face_cropped(my_frame) is not None:
    #                         img_id += 1
    #                     face = cv2.resize(face_cropped(my_frame), (450, 450))
    #                     face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    #                     file_name_path = "data/user." + \
    #                         str(id)+"."+str(img_id)+".jpg"
    #                     cv2.imwrite(file_name_path, face)
    #                     cv2.putText(face, str(img_id), (50, 50),
    #                                 cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
    #                     cv2.imshow('Face Cropper', face)

    #                     if cv2.waitKey(1) == 13 or int(img_id) == 100:
    #                         break

    #                 cap.release()
    #                 cv2.destroyAllWindows()
    #                 messagebox.showinfo(
    #                     "Result", "Generating data sets completed!")

    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due To: {
    #                 str(es)}", parent=self.root)

    # ================== Generate DataSet || Take Photo Sample =================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_stu_name.get() == "" or self.var_stu_id.get() == "":
            messagebox.showerror(
                "Error", "All field are requied", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Aang@123",
                                               database="face_recognizer", auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOb=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_stu_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_stu_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ==load predifiend data on face frontals from opencv==
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        # scalling factor=1.3
        # minimum Neighbor=5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 200:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating data sets are completed!")
            except Exception as es:
                messagebox.showerror(
                    "Error", "Due To: " + str(es), parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
