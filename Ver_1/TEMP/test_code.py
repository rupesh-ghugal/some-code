# import mysql
# import mysql.connector
# import datetime
#
# def Entry_get_update_data(number_p):
#     time = str(datetime.datetime.now())
#     conn = mysql.connector.connect(host="localhost", username="root", password="rakesh",database="anpr_final_db")
#     my_cursor = conn.cursor()
#
#     sql = "INSERT INTO `anpr_final_db`.`rto` (`Vehicle_number`, `Entry_time`) VALUES (%s,%s);"
#
#     data = (number_p,time)
#
#     try:
#         my_cursor.execute(sql,data)
#         result = my_cursor.fetchall()
#         conn.commit()
#     except:
#         print("Data base is not conect")



# Entry_get_update_data("MH28AB1520")



# temp = []

# for i in result:
    
#     data_1 = str(i[2])
#     date_1, time_1 = data_1.split(' ')
#     time_1 = time_1[:8]

#     data_2 = str(i[3])
#     date_2, time_2 = data_2.split(' ')
#     time_2 = time_2[:8]

#     temp.append((i[1],date_1,time_1,date_2,time_2))

# for i in temp:
#     print(i)

# file = open("password",'w+')
# file.write("Himanshu")
# file.seek(0)
# print(file.read())

# import os
# path = "password.txt"
# isExist = os.path.exists(path)
# if isExist == False:
#     file = open("password.txt",'w+')


# from tkinter import *
# from tkinter import messagebox

	
# # object of TK()
# main = Tk()

# function to use the 
# askquestion() function
# def Submit(): 
#     print(messagebox.askquestion("Form","Do you want to Submit"))
	
# # setting geometry of window 
# # instance
# main.geometry("100x100")

# # creating Window
# B1 = Button(main, text = "Submit", command = Submit) 

# # Button positioning 
# B1.pack() 

# # infinite loop till close
# main.mainloop() 

# import datetime
#
# temp = [(1, 'MH28AB420', datetime.datetime(2023, 9, 13, 1, 0, 15, 62430), datetime.datetime(2023, 8, 11, 12, 0, 15, 62430)),
# (2, 'MH28AB420', datetime.datetime(2023, 10, 13, 12, 0, 15, 62430), datetime.datetime(2023, 10, 13, 12, 0, 15, 62430))]

# data = []
# for i,v in enumerate(temp):
#     data.append((v[2].strftime('%m/%d/%Y %I:%M%p')))
#
# print(data)

# data =['10/13/2023 12:00PM','09/13/2023 01:00AM']
# from datetime import datetime
# # print(data)
# sorted_lst = sorted(data, key=lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M%p'))
# for i in sorted_lst:
#     j = data.index(i)
#     print(temp[j])

# lst = [datetime.datetime(2023, 9, 13, 1, 0, 15, 62430), datetime.datetime(2023, 8, 11, 12, 0, 15, 62430),
# 'MH28AB420', datetime.datetime(2023, 10, 13, 12, 0, 15, 62430), datetime.datetime(2023, 10, 13, 12, 0, 15, 62430)]

# sorted_lst = sorted(lst, key=lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M %p'))
# print(lst)


# # # creating thread
# #             t1 = threading.Thread(target=self.open_video, args=(self.vid_widget1,))
# #             t2 = threading.Thread(target=self.open_video, args=(self.vid_widget1,))

# #             t1.start()
# #             t2.start()

# # creating thread
#                 # t1 = threading.Thread(target=self.open_video, args=(self.vid_widget1,))
#                 # t2 = threading.Thread(target=self.open_video, args=(self.vid_widget1,))

#                 t1 = threading.Thread(self.open_video, self.vid_widget1)
#                 t2 = threading.Thread(self.open_video, self.vid_widget1)

#                 t1.start()
#                 t2.start()


   # def find_vhic_data(self):
    #     time = datetime.datetime.now()
    #     V_num = "MH02AB1236"
    #     self.root = Tk()
    #     self.root.title("Find Vhical informetion ")
    #     self.root.geometry("400x400")

    #     conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="rto_copy")
    #     my_cursor=conn.cursor()

    #     sql ="""UPDATE `rto_copy`.`rto` SET `Entry_time` = %s, `Exit_time` = %s WHERE (`Vehicle_number` = %s);"""
    #     data = (time,time,V_num)
    #     try:
    #         my_cursor.execute(sql)
    #         conn.commit()
    #     except (MySQLdb.Error, MySQLdb.Warning) as e:
    #         print(e)
    #         print("server conection fell")

# obj=Find()
# obj.find_vhic_data()









#
#
# import mysql
# import mysql.connector
# import datetime
# from datetime import datetime
#
# def Entry_get_update_data():
#
#     time = str(datetime.now())
#     conn = mysql.connector.connect(host="localhost", username="root", password="rakesh",database="anpr_final_db")
#     my_cursor = conn.cursor()
#
#     sql = "select * from anpr_final_db.rto "
#     data = []
#     try:
#         my_cursor.execute(sql)
#         result = my_cursor.fetchall()
#     except:
#         print("Data base is not conect")
#     finally:
#         conn.close()
#
#     for i in result:
#         data.append((i[2].strftime('%m/%d/%Y %I:%M%p')))
#
#
#     sorted_lst = sorted(data, key=lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M%p'))
#     for i in sorted_lst:
#         j = data.index(i)
#         print(result[j][2].strftime('%b/%d/%Y %I:%M%p'))
#
#
#
# Entry_get_update_data()





import os
p = (os.path.abspath(__file__))
os.remove("E:/Ver_1/Text/psaa.py")

