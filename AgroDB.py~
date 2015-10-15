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
