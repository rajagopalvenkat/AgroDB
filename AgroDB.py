import Tkinter as Tk
import MySQLdb as sql
import string
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel
import numpy as np
import matplotlib.pyplot as plt
import Tkinter
from PIL import Image, ImageTk

root = Tk.Tk()

################################################      ENTRY 		  ############################################################

def call_entry():
	entry=Tk.Tk()
	entry.wm_title("Enter a Record")
	entry.minsize(100,100)
	entry.geometry("680x300")

	res1=Image.open('Shadowfigure-Crops_www.FullHDWpp.com_.jpg')
	res1=res1.resize((680,300), Image.ANTIALIAS)
	image1 = ImageTk.PhotoImage(res1)
	label = Tk.Label(entry, image = image1)
	label.pack(fill=Tk.BOTH, expand=1)
	
	var = Tk.StringVar()
	var.set('Select')
	choices = ['','Andhra Pradesh', 'Assam', 'Bihar', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Nagaland', 'Orissa', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttaranchal', 'West Bengal', 'Mordor']
	option = Tk.OptionMenu(entry, var, *choices)
	option.pack()
	option.place(x=300, y=75, width=150)
	
	def submit():
		cursor=db.cursor()
		table_name = var.get().replace(" ", "_")
		exec_submit = "INSERT INTO {0} VALUES('{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(table_name, dist_var.get(), int(year_var.get()), crop_var.get(), float(area_var.get()), float(production_var.get()), float(yield_var.get()))
		cursor.execute(exec_submit)
		db.commit()
		entry.destroy()
		call_menu()		

	submitbutton=Tk.Button(entry, text="Submit", command=submit)
	submitbutton.pack()
	submitbutton.place(x=480, y=250, width=100)

	Lab1 = Tk.Label(entry, text="District")
	Lab1.pack()
	Lab1.place(x=50, y=150, width=80)

	dist_var = Tk.StringVar()
	district_entry = Tk.Entry(entry, textvariable=dist_var)
	district_entry.pack()
	district_entry.place(x=50, y=180,  width=80)

	Lab2 = Tk.Label(entry, text="Year")
	Lab2.pack()
	Lab2.place(x=150, y=150, width=80)

	year_var = Tk.StringVar()
	year_entry = Tk.Entry(entry, textvariable=year_var)
	year_entry.pack()
	year_entry.place(x=150, y=180, width=80)

	Lab3 = Tk.Label(entry, text="Crop")
	Lab3.pack()
	Lab3.place(x=250, y=150, width=80)

	crop_var = Tk.StringVar()
	crop_entry = Tk.Entry(entry, textvariable=crop_var)
	crop_entry.pack()
	crop_entry.place(x=250, y=180,  width=80)

	Lab4 = Tk.Label(entry, text="Area")
	Lab4.pack()
	Lab4.place(x=350, y=150, width=80)

	area_var = Tk.StringVar()
	area_entry = Tk.Entry(entry, textvariable=area_var)
	area_entry.pack()
	area_entry.place(x=350, y=180,  width=80)

	Lab5 = Tk.Label(entry, text="Production")
	Lab5.pack()
	Lab5.place(x=450, y=150, width=80)

	production_var = Tk.StringVar()
	production_entry = Tk.Entry(entry, textvariable=production_var)
	production_entry.pack()
	production_entry.place(x=450, y=180,  width=80)	

	Lab6 = Tk.Label(entry, text="Yield")
	Lab6.pack()
	Lab6.place(x=550, y=150, width=80)

	yield_var = Tk.StringVar()
	yield_entry = Tk.Entry(entry, textvariable=yield_var)
	yield_entry.pack()
	yield_entry.place(x=550, y=180,  width=80)

	def back():
		entry.destroy()
		call_menu()

	back=Tk.Button(entry, text="Back", command=back)
	back.pack()
	back.place(x=400, y=250)

	entry.mainloop()

################################################      END ENTRY          #########################################################


################################################      RETRIEVE          #########################################################

def call_retrieve():

	retrieve=Tk.Tk()
	retrieve.wm_title("Search")
	retrieve.geometry("680x325")

	res1=Image.open('Sun_Crops_Wallpaper_o6ujr.jpg')
	res1=res1.resize((680,325), Image.ANTIALIAS)
	image1 = ImageTk.PhotoImage(res1)
	label = Tk.Label(retrieve, image = image1)
	label.pack(fill=Tk.BOTH, expand=1)

	label_state=Tk.Label(retrieve, text="State")
	label_state.pack()
	label_state.place(x=50, y=50, width=150)

	var = Tk.StringVar()
	var.set('Select')
	choices = ['','Andhra Pradesh', 'Assam', 'Bihar', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Nagaland', 'Orissa', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttaranchal', 'West Bengal', 'Mordor']
	option = Tk.OptionMenu(retrieve, var, *choices)
	option.pack()
	option.place(x=50, y=75, width=150)

	Lab1 = Tk.Label(retrieve, text="District")
	Lab1.pack()
	Lab1.place(x=250, y=50, width=150)

	dist_var = Tk.StringVar()
	district_entry = Tk.Entry(retrieve, textvariable=dist_var)
	district_entry.pack()
	district_entry.place(x=250, y=75,  width=150)

	Lab3 = Tk.Label(retrieve, text="Crop")
	Lab3.pack()
	Lab3.place(x=450, y=50, width=150)

	crop_var = Tk.StringVar()
	crop_entry = Tk.Entry(retrieve, textvariable=crop_var)
	crop_entry.pack()
	crop_entry.place(x=450, y=75,  width=150)

	Lab2 = Tk.Label(retrieve, text="Year")
	Lab2.pack()
	Lab2.place(x=50, y=125, width=150)

	year_var = Tk.StringVar()
	year_entry = Tk.Entry(retrieve, textvariable=year_var)
	year_entry.pack()
	year_entry.place(x=50, y=150, width=150)

	Lab2_beg = Tk.Label(retrieve, text="Year From")
	Lab2_beg.pack()
	Lab2_beg.place(x=250, y=125, width=150)

	year_beg_var = Tk.StringVar()
	year_beg_entry = Tk.Entry(retrieve, textvariable=year_beg_var)
	year_beg_entry.pack()
	year_beg_entry.place(x=250, y=150, width=150)

	Lab2_end = Tk.Label(retrieve, text="Year To")
	Lab2_end.pack()
	Lab2_end.place(x=450, y=125, width=150)

	year_end_var = Tk.StringVar()
	year_end_entry = Tk.Entry(retrieve, textvariable=year_end_var)
	year_end_entry.pack()
	year_end_entry.place(x=450, y=150, width=150)

	Lab4_beg = Tk.Label(retrieve, text="Area From")
	Lab4_beg.pack()
	Lab4_beg.place(x=50, y=175, width=100)

	area_beg_var = Tk.StringVar()
	area_beg_entry = Tk.Entry(retrieve, textvariable=area_beg_var)
	area_beg_entry.pack()
	area_beg_entry.place(x=50, y=200,  width=100)

	Lab4_end = Tk.Label(retrieve, text="Area To")
	Lab4_end.pack()
	Lab4_end.place(x=175, y=175, width=100)

	area_end_var = Tk.StringVar()
	area_end_entry = Tk.Entry(retrieve, textvariable=area_end_var)
	area_end_entry.pack()
	area_end_entry.place(x=175, y=200,  width=100)

	Lab5_beg = Tk.Label(retrieve, text="Production From")
	Lab5_beg.pack()
	Lab5_beg.place(x=350, y=175, width=100)

	production_beg_var = Tk.StringVar()
	production_beg_entry = Tk.Entry(retrieve, textvariable=production_beg_var)
	production_beg_entry.pack()
	production_beg_entry.place(x=350, y=200,  width=100)	

	Lab5_end = Tk.Label(retrieve, text="Production To")
	Lab5_end.pack()
	Lab5_end.place(x=500, y=175, width=100)

	production_end_var = Tk.StringVar()
	production_end_entry = Tk.Entry(retrieve, textvariable=production_end_var)
	production_end_entry.pack()
	production_end_entry.place(x=500, y=200,  width=100)

	Lab6_beg = Tk.Label(retrieve, text="Yield From")
	Lab6_beg.pack()
	Lab6_beg.place(x=175, y=225, width=100)

	yield_beg_var = Tk.StringVar()
	yield_beg_entry = Tk.Entry(retrieve, textvariable=yield_beg_var)
	yield_beg_entry.pack()
	yield_beg_entry.place(x=175, y=250,  width=100)

	Lab6_end = Tk.Label(retrieve, text="Yield To")
	Lab6_end.pack()
	Lab6_end.place(x=350, y=225,width=100)

	yield_end_var = Tk.StringVar()
	yield_end_entry = Tk.Entry(retrieve, textvariable=yield_end_var)
	yield_end_entry.pack()
	yield_end_entry.place(x=350, y=250,  width=100)

	def back():
		retrieve.destroy()
		call_menu()

	back=Tk.Button(retrieve, text= "Back", command=back)
	back.pack()
	back.place(x=50, y=275)

	def call_table():

		if str(var.get()) == "Mordor":
			retrieve.destroy()
			mordor=Tk.Tk()
			mordor.wm_title("Welcome to Mordor")
			mordor.geometry("680x325")
			res1=Image.open('sauron_by_spartank42-d502g9o.jpg')
			res1=res1.resize((680,325), Image.ANTIALIAS)
			image1 = ImageTk.PhotoImage(res1)
			label = Tk.Label(mordor, image = image1)
			label.pack(fill=Tk.BOTH, expand=1)
			onering=Tk.Label(mordor, text="One ring to rule them all, One ring to find them.", font="eufm10")
			onering2=Tk.Label(mordor, text="One ring to rule bring them all and in the darkness bind them.", font="eufm10")
			onering3=Tk.Label(mordor, text="In the land of Mordor where the shadows lie.", font="eufm10")
			onering.place(x=170, y=250)
			onering2.place(x=130, y=270)
			onering3.place(x=180, y=290)
			mordor.mainloop()
			return

		cursor=db.cursor()

		commandstring = "SELECT * FROM {0}".format(var.get().replace(" ","_"))

		if dist_var.get()!= "" or crop_var.get()!= "" or year_var.get()!= "" or year_beg_var.get()!= "" or year_end_var.get()!= "" or area_beg_var.get() != "" or area_end_var.get()!= "" or production_beg_var.get()!= "" or production_end_var.get()!= "" or yield_beg_var.get()!= "" or yield_end_var.get()!= "":
			commandstring += " WHERE "

		count=0;

		if dist_var.get()!="":
			commandstring += "District = \"{0}\"".format(dist_var.get())
			count+=1
		if crop_var.get()!="":
			if count > 0:
				commandstring += " AND "
			commandstring += "Crop = \"{0}\"".format(crop_var.get())
			count+=1
		if year_var.get()!="":
			if count > 0:
				commandstring += " AND "
			commandstring += "Year = {0}".format(int(year_var.get()))
			count+=1
		if year_beg_var.get()!="":
			if count > 0:
				commandstring += " AND "
			commandstring += "Year >= {0}".format(int(year_beg_var.get()))
			count+=1
		if year_end_var.get()!="":
			if count > 0:
				commandstring += " AND "
			commandstring += "Year <= {0}".format(int(year_end_var.get()))
			count+=1
		if production_beg_var.get()!="":
			if count > 0:
				commandstring += " AND "
			commandstring += "Production >= {0}".format(float(production_beg_var.get()))
			count+=1
		if production_end_var.get()!="":
			if count > 0:
				commandstring += " AND "
			commandstring += "Production <= {0}".format(float(production_end_var.get()))
			count+=1
		if yield_beg_var.get()!="":
			if count > 0:
				commandstring += " AND "
			commandstring += "Yield >= {0}".format(float(yield_beg_var.get()))
			count+=1
		if yield_end_var.get()!="":
			if count > 0:
				commandstring += " AND "
			commandstring += "Yield <= {0}".format(float(yield_end_var.get()))
			count+=1
		if area_beg_var.get()!="":
			if count > 0:
				commandstring += " AND "
			commandstring += "Area >= {0}".format(float(area_beg_var.get()))
			count+=1
		if area_end_var.get()!="":
			if count > 0:
				commandstring += " AND "
			commandstring += "Area <= {0}".format(float(area_end_var.get()))
			count+=1
		commandstring += ";"

		print commandstring
		cursor.execute(commandstring)
		dict={}
		index=(0,1,2,3,4,5)
		desc=('District', 'Year', 'Crop', 'Area', 'Production', 'Yield')
		d2={}
		c=1
		for i in cursor:
			num=0
			d2={}
			for j in i:
				d2[desc[num]]=j
				num+=1
			dict['a' + str(c)] = d2
			c+=1

		master = Tk.Tk()
		master.geometry("800x300")
		tframe = Tk.Frame(master)
		tframe.pack(fill="both")
		model = TableModel()
		table = TableCanvas(tframe, model=model)
		model = table.model
		model.importDict(dict)
		table.createTableFrame()
		table.redrawTable()
		master.mainloop()
		

	search=Tk.Button(retrieve, text="Search", command=call_table)
	search.pack()
	search.place(x=600,y=275)

	retrieve.mainloop()
################################################      END RETRIEVE          #########################################################



################################################          ANALYZE		  ###########################################################


def call_analyze():

	analyze=Tk.Tk()
	analyze.wm_title("Graphs")
	analyze.geometry("650x650")

	res1=Image.open('landscapes_nature_fields_crops_desktop_1920x1200_wallpaper-1049121-600x375.jpg')
	res1=res1.resize((650,650), Image.ANTIALIAS)
	image1 = ImageTk.PhotoImage(res1)
	label = Tk.Label(analyze, image = image1)
	label.pack(fill=Tk.BOTH, expand=1)

	states=('Andhra_Pradesh', 'Assam', 'Bihar', 'Gujarat', 'Haryana', 'Himachal_Pradesh', 'Jammu_and_Kashmir', 'Karnataka', 'Kerala', 'Madhya_Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Nagaland', 'Orissa', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil_Nadu', 'Tripura', 'Uttar_Pradesh', 'Uttaranchal', 'West_Bengal', 'Mordor')

	check0=Tk.IntVar()
	check1=Tk.IntVar()
	check2=Tk.IntVar()
	check3=Tk.IntVar()
	check4=Tk.IntVar()
	check5=Tk.IntVar()
	check6=Tk.IntVar()
	check7=Tk.IntVar()
	check8=Tk.IntVar()
	check9=Tk.IntVar()
	check10=Tk.IntVar()
	check11=Tk.IntVar()
	check12=Tk.IntVar()
	check13=Tk.IntVar()
	check14=Tk.IntVar()
	check15=Tk.IntVar()
	check16=Tk.IntVar()
	check17=Tk.IntVar()
	check18=Tk.IntVar()
	check19=Tk.IntVar()
	check20=Tk.IntVar()
	check21=Tk.IntVar()
	check22=Tk.IntVar()
	check23=Tk.IntVar()
	check24=Tk.IntVar()

	c_all=Tk.Checkbutton(analyze, text = "All States", variable = check24, onvalue=1, offvalue=0, height=1, width=20)
	c_all.pack()
	c_all.place(x=10, y=0)

	c0 = Tk.Checkbutton(analyze, text = "Andhra Pradesh", variable = check0, onvalue=1, offvalue=0, height=1, width=20)
	c0.pack()
	c0.place(x=10, y=25)

	c1 = Tk.Checkbutton(analyze, text = "Assam", variable = check1, onvalue=1, offvalue=0, height=1, width=20)
	c1.pack()
	c1.place(x=10, y=50)

	c2 = Tk.Checkbutton(analyze, text = "Bihar", variable = check2, onvalue=1, offvalue=0, height=1, width=20)
	c2.pack()
	c2.place(x=10, y=75)

	c3 = Tk.Checkbutton(analyze, text = "Gujarat", variable = check3, onvalue=1, offvalue=0, height=1, width=20)
	c3.pack()
	c3.place(x=10, y=100)

	c4 = Tk.Checkbutton(analyze, text = "Haryana", variable = check4, onvalue=1, offvalue=0, height=1, width=20)
	c4.pack()
	c4.place(x=10, y=125)

	c5 = Tk.Checkbutton(analyze, text = "Himachal Pradesh", variable = check5, onvalue=1, offvalue=0, height=1, width=20)
	c5.pack()
	c5.place(x=10, y=150)

	c6 = Tk.Checkbutton(analyze, text = "Jammu and Kashmir", variable = check6, onvalue=1, offvalue=0, height=1, width=20)
	c6.pack()
	c6.place(x=10, y=175)

	c7 = Tk.Checkbutton(analyze, text = "Karnataka", variable = check7, onvalue=1, offvalue=0, height=1, width=20)
	c7.pack()
	c7.place(x=10, y=200)

	c8 = Tk.Checkbutton(analyze, text = "Kerala", variable = check8, onvalue=1, offvalue=0, height=1, width=20)
	c8.pack()
	c8.place(x=10, y=225)

	c9 = Tk.Checkbutton(analyze, text = "Madhya Pradesh", variable = check9, onvalue=1, offvalue=0, height=1, width=20)
	c9.pack()
	c9.place(x=10, y=250)

	c10 = Tk.Checkbutton(analyze, text = "Maharashtra", variable = check10, onvalue=1, offvalue=0, height=1, width=20)
	c10.pack()
	c10.place(x=10, y=275)

	c11 = Tk.Checkbutton(analyze, text = "Manipur", variable = check11, onvalue=1, offvalue=0, height=1, width=20)
	c11.pack()
	c11.place(x=10, y=300)

	c12 = Tk.Checkbutton(analyze, text = "Meghalaya", variable = check12, onvalue=1, offvalue=0, height=1, width=20)
	c12.pack()
	c12.place(x=10, y=325)

	c13 = Tk.Checkbutton(analyze, text = "Nagaland", variable = check13, onvalue=1, offvalue=0, height=1, width=20)
	c13.pack()
	c13.place(x=10, y=350)

	c14 = Tk.Checkbutton(analyze, text = "Orissa", variable = check14, onvalue=1, offvalue=0, height=1, width=20)
	c14.pack()
	c14.place(x=10, y=375)

	c15 = Tk.Checkbutton(analyze, text = "Punjab", variable = check15, onvalue=1, offvalue=0, height=1, width=20)
	c15.pack()
	c15.place(x=10, y=400)

	c16 = Tk.Checkbutton(analyze, text = "Rajasthan", variable = check16, onvalue=1, offvalue=0, height=1, width=20)
	c16.pack()
	c16.place(x=10, y=425)

	c17 = Tk.Checkbutton(analyze, text = "Sikkim", variable = check17, onvalue=1, offvalue=0, height=1, width=20)
	c17.pack()
	c17.place(x=10, y=450)

	c18 = Tk.Checkbutton(analyze, text = "Tamil Nadu", variable = check18, onvalue=1, offvalue=0, height=1, width=20)
	c18.pack()
	c18.place(x=10, y=475)

	c19 = Tk.Checkbutton(analyze, text = "Tripura", variable = check19, onvalue=1, offvalue=0, height=1, width=20)
	c19.pack()
	c19.place(x=10, y=500)

	c20 = Tk.Checkbutton(analyze, text = "Uttar Pradesh", variable = check20, onvalue=1, offvalue=0, height=1, width=20)
	c20.pack()
	c20.place(x=10, y=525)

	c21 = Tk.Checkbutton(analyze, text = "Uttaranchal", variable = check21, onvalue=1, offvalue=0, height=1, width=20)
	c21.pack()
	c21.place(x=10, y=550)

	c22 = Tk.Checkbutton(analyze, text = "West Bengal", variable = check22, onvalue=1, offvalue=0, height=1, width=20)
	c22.pack()
	c22.place(x=10, y=575)

	c23 = Tk.Checkbutton(analyze, text = "Mordor", variable = check23, onvalue=1, offvalue=0, height=1, width=20)
	c23	.pack()
	c23.place(x=10, y=600)

	district_label = Tk.Label(analyze, text="District")
	district_label.pack()
	district_label.place(x=350, y=75)

	district_entry_var=Tk.StringVar()
	district_entry = Tk.Entry(analyze, textvariable = district_entry_var)
	district_entry.pack()
	district_entry.place(x=350, y=100)

	crop_label = Tk.Label(analyze, text="Crop")
	crop_label.pack()
	crop_label.place(x=350, y=150)

	crop_entry_var=Tk.StringVar()
	crop_entry = Tk.Entry(analyze, textvariable = crop_entry_var)
	crop_entry.pack()
	crop_entry.place(x=350, y=175)

	year_beg_label = Tk.Label(analyze, text="From Year")
	year_beg_label.pack()
	year_beg_label.place(x=350, y=225)

	year_beg_entry_var=Tk.StringVar()
	year_beg_entry = Tk.Entry(analyze, textvariable = year_beg_entry_var)
	year_beg_entry.pack()
	year_beg_entry.place(x=350, y=250)

	year_end_label = Tk.Label(analyze, text="To Year")
	year_end_label.pack()
	year_end_label.place(x=350, y=300)

	year_end_entry_var=Tk.StringVar()
	year_end_entry = Tk.Entry(analyze, textvariable = year_end_entry_var)
	year_end_entry.pack()
	year_end_entry.place(x=350, y=325)


	check_area_var=Tk.IntVar()
	check_area=Tk.Checkbutton(analyze, text="Plot Area", variable=check_area_var, onvalue=1, offvalue=0, height=1, width=20)
	check_area.pack()
	check_area.place(x=350, y=375)

	check_production_var=Tk.IntVar()
	check_production=Tk.Checkbutton(analyze, text="Plot Production", variable=check_production_var, onvalue=1, offvalue=0, height=1, width=20)
	check_production.pack()
	check_production.place(x=350, y=425)

	check_yield_var=Tk.IntVar()
	check_yield=Tk.Checkbutton(analyze, text="Plot Yield", variable=check_yield_var, onvalue=1, offvalue=0, height=1, width=20)
	check_yield.pack()
	check_yield.place(x=350, y=475)

	def data_feed():
		cursor2=db.cursor()
		cursor=db.cursor()
		commandstring=""
		count=0
		count2=0
		set=0
		global year
		global val
		year=()
		val=()
		vararray = (check0, check1, check2, check3, check4, check5, check6, check7, check8, check9, check10, check11, check12, check13, check14, check15, check16, check17, check18, check19, check20, check21, check22, check23)
		global cmdpass
		cmdpass=''
		tempyear=()

		if check_area_var.get()==1:
			cmdpass='Area'
		elif check_production_var.get()==1:
			cmdpass='Production'
		elif check_yield_var.get()==1:
			cmdpass='Yield'

		if check24.get() == 1:
			cursor.execute("SELECT information_schema.TABLES.TABLE_NAME FROM information_schema.TABLES where table_schema='AGRICULTURE'")

			for i in cursor:
				for x in i:
					commandstring=""
					cmd2=""
					count2=0
					cmd2 += "SELECT Year FROM {0}".format(x)

					commandstring += "SELECT {0} FROM {1}".format(str(cmdpass), x)
					count+=1

					if district_entry_var.get()!="" or crop_entry_var.get()!="" or year_beg_entry.get()!="" or year_end_entry.get()!="":
						commandstring+= " WHERE "
						cmd2+=" WHERE "

					if count2 > 0 and district_entry_var.get()!="":
						commandstring+= " AND "
						cmd2+= " AND "
					if district_entry_var.get()!="":
						commandstring+="District = \"{0}\"".format(district_entry_var.get())
						cmd2+="District = \"{0}\"".format(district_entry_var.get())
						count2+=1;
					if count2 > 0 and crop_entry_var.get()!="":
						commandstring+= " AND "
						cmd2+= " AND "
					if crop_entry_var.get()!="":
						commandstring+="Crop = \"{0}\"".format(crop_entry_var.get())
						cmd2+="Crop = \"{0}\"".format(crop_entry_var.get())
						count2+=1;
					if count2 > 0 and year_beg_entry.get()!="":
						commandstring+= " AND "
						cmd2+= " AND "
					if year_beg_entry.get()!="":
						commandstring+="Year >= {0}".format(int(year_beg_entry.get()))
						cmd2+="Year >= {0}".format(int(year_beg_entry.get()))
						count2+=1;
					if count2 > 0 and year_end_entry.get()!="":
						commandstring+= " AND "
						cmd2+= " AND "
					if year_end_entry.get()!="":
						commandstring+="Year <= {0}".format(int(year_end_entry.get()))
						cmd2+="Year <= {0}".format(int(year_end_entry.get()))
						count2+=1;
					commandstring+=";"
					cmd2+=";"
					cursor.execute(commandstring)
					cursor2.execute(cmd2)
					temp=()
					for i in cursor:
						for j in i:
							temp += (j,)
					val+=(temp,)
			
			for i in cursor2:
				for j in i:
					year += (int(j),)
		
				
					
		else:

			if check23.get()==1:
				analyze.destroy()
				mordor=Tk.Tk()
				mordor.wm_title("Welcome to Mordor")
				mordor.geometry("650x350")
				res1=Image.open('Sauron_eye_barad_dur.jpg')
				res1=res1.resize((650,350), Image.ANTIALIAS)
				image1 = ImageTk.PhotoImage(res1)
				label = Tk.Label(mordor, image = image1)
				label.pack(fill=Tk.BOTH, expand=1)
				onering=Tk.Label(mordor, text="You cannot hide. I see all.", font="eufm10")
				onering2=Tk.Label(mordor, text="There is no life in the void.", font="eufm10")
				onering3=Tk.Label(mordor, text="Only Death!", font="eufm10")
				onering.place(x=230, y=235)
				onering2.place(x=230, y=255)
				onering3.place(x=280, y=275)
				mordor.mainloop()
				return

			for i in range(0,23):
				count2=0	
				commandstring=""
				cmd2=""
				if  vararray[i].get()== 1:
					cmd2 += "SELECT Year FROM {0}".format(states[i])
					commandstring += "SELECT {0} FROM {1}".format(str(cmdpass), states[i])
					set=1
					count+=1
				if (district_entry_var.get()!="" or crop_entry_var.get()!="" or year_beg_entry.get()!="" or year_end_entry.get()!="") and commandstring!=""	and set==1:
						commandstring+= " WHERE "
						cmd2+= " WHERE "
				if count2 > 0 and district_entry_var.get()!="" and set==1:
					commandstring+= " AND "
					cmd2+= " AND "
				if district_entry_var.get()!="" and commandstring!="" and set==1:
					commandstring+="District = \"{0}\"".format(district_entry_var.get())
					cmd2+="District = \"{0}\"".format(district_entry_var.get())
					count2+=1;
				if count2 > 0 and crop_entry_var.get()!="" and set==1:
					commandstring+= " AND "
					cmd2+= " AND "
				if crop_entry_var.get()!="" and commandstring!="" and set==1:
					commandstring+="Crop = \"{0}\"".format(crop_entry_var.get())
					cmd2+="Crop = \"{0}\"".format(crop_entry_var.get())
					count2+=1;
				if count2 > 0 and year_beg_entry.get()!="" and set==1:
					commandstring+= " AND "
					cmd2+= " AND "
				if year_beg_entry.get()!="" and commandstring!="" and set==1:
					commandstring+="Year >= {0}".format(int(year_beg_entry.get()))
					cmd2+="Year >= {0}".format(int(year_beg_entry.get()))
					count2+=1;
				if count2 > 0 and year_end_entry.get()!="" and set==1:
					commandstring+= " AND "
					cmd2+= " AND "
				if year_end_entry.get()!="" and commandstring!="" and set==1:
					commandstring+="Year <= {0}".format(int(year_end_entry.get()))
					cmd2+="Year <= {0}".format(int(year_end_entry.get()))
					count2+=1;
				set=0	
				if commandstring!="":
					commandstring+=";"
					cursor.execute(commandstring)
					temp=()

					for j in cursor:
						for i in j:
							temp += j
					
					val += (temp,)
					

				if cmd2!="":
					cmd2+=";"
					
					cursor2.execute(cmd2)
			
			for i in cursor2:
				for j in i:
					year += (int(j)	,)

		mx=0
		ct2=0
		for i in val:
			ct2=0
			for j in i:
				ct2+=1
			if ct2>mx:
				mx=ct2
		
		val=list(val)
		ct2=0
		for i in val:
			if len(i)<mx:
				for m in range(len(i),mx):
					val[ct2] += (0.0, )
			ct2+=1


	def plot_pie():
		data_feed()		
		n=0;
		for i in val:
			n+=1

		for i in range(0, n):
			colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','yellowgreen', 'gold', 'lightskyblue', 'lightcoral','yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
			plt.pie(val[i], labels=year, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)		
			plt.axis('equal')
			plt.show()


	def plot_bar():
		color=('r','g','b','y','r','g','b','y','r','g','b','y','r','g','b','y','r','g','b','y','r','g','b','y')
		
		N=0
		ctr=0
		data_feed()
		
		for i in val:
			ctr+=1
		for j in val[0]:
			N+=1
		
		r=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		ind = np.arange(N)
		width = 0.15
		fig, ax = plt.subplots()
		
		for i in range(ctr):
			
			r[i]=ax.bar(ind+(i*width), val[i], width, color=color[i])
			ax.set_ylabel(cmdpass)
			ax.set_title(cmdpass)
			ax.set_xticks(ind+(i*width))
			ax.set_xticklabels(year)
		plt.show()


	def plot_scatter():
		data_feed()
		print val, year
		colors=('r','g','b','y','r','g','b','y','r','g','b','y','r','g','b','y','r','g','b','y','r','g','b','y')
		for i in val:
			plt.scatter(year, i, s=10, c=colors, alpha=0.5)
			plt.plot(year,i)
		plt.show()



	bar = Tk.Button(analyze, text="Plot Bar Graph", command=plot_bar)
	bar.pack()
	bar.place(x=450, y=550)

	pie = Tk.Button(analyze, text="Plot Pie Chart", command=plot_pie)
	pie.pack()
	pie.place(x=325, y=550)

	scatter = Tk.Button(analyze, text="Plot Scatter", command=plot_scatter)
	scatter.pack()
	scatter.place(x=200, y=550)

	def back():
		analyze.destroy()
		call_menu()

	back=Tk.Button(analyze, text="Back", command=back)
	back.pack()
	back.place(x=350, y=600)

	analyze.mainloop()


################################################          END ANALYZE		  #######################################################





################################################              MENU		    ############################################################


def data_entry():
	menu.destroy()
	call_entry()

def data_retrieve():
	menu.destroy() 
	call_retrieve()

def data_analyze():
	menu.destroy()
	call_analyze()

def call_menu():
	global menu
	menu=Tk.Tk()
	menu.wm_title("Menu")
	menu.minsize(100,100)
	menu.geometry("450x400")

	res1=Image.open('047efdff0f8e9a00483204ee49945b74.jpg')
	res1=res1.resize((450,400), Image.ANTIALIAS)
	image1 = ImageTk.PhotoImage(res1)
	label = Tk.Label(menu, image = image1)
	label.pack(fill=Tk.BOTH, expand=1)


	label2=Tk.Label(menu, text="Choose an Option", bd=5)
	label2.pack()
	label2.place(x=170, y=50)

	entry=Tk.Button(menu, text="Enter New Record", command=data_entry)
	entry.pack()
	entry.place(x=160, y=100)

	retrieve=Tk.Button(menu, text="Search", command=data_retrieve)
	retrieve.pack()
	retrieve.place(x=185, y=200)

	analyze=Tk.Button(menu, text="Plot Graph", command=data_analyze)
	analyze.pack()
	analyze.place(x=175, y=300)
	
	menu.mainloop()

################################################      END  MENU		  ############################################################



#########################################   LOGIN WINDOW    ############################################################

root.wm_title("AgroDB")
root.minsize(100, 100)
root.geometry("400x400")

res1=Image.open('stockvault-field-of-yellow114610.jpg')
res1=res1.resize((400,400), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(res1)
label = Tk.Label(root, image = image1)
label.pack(fill=Tk.BOTH, expand=1)

label1 = Tk.Label(root, text = "Welcome to AgroDB", bg="White")
label1.pack()
label1.place(x=120, y=75)


def login():
	user_name = username.get()
	passwd = password.get()
	global db
	db=sql.connect("localhost", user_name, passwd, "AGRICULTURE")

	if "connection open to 'localhost' at" in str(db):
		print 'Credentials Verified'
		root.destroy()
		call_menu()		
		global cursor		
		cursor=db.cursor()


L1 = Tk.Label(root, text="User Name")
L1.pack( side = Tk.LEFT)
L1.place(x=50, y=200)

username = Tk.Entry(root,bd =5)
username.pack(side = Tk.RIGHT)
username.place(x=150, y=200)


L2 = Tk.Label(root, text="Password")
L2.pack( side = Tk.LEFT)
L2.place(x=50, y=250)

password = Tk.Entry(root,bd =5, show="*c")
password.pack(side = Tk.RIGHT)
password.place(x=150, y=250)


login=Tk.Button(root, text="Login", command=login)
login.pack()
login.place(x=150, y=300)

root.mainloop()

################################################  END LOGIN WINDOW    ############################################################


