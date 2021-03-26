import tkinter
import mysql.connector

def server_sql():
    # connect aan de database
    conn = mysql.connector.connect(host="145.74.104.145",
                                   user="rtlrc",
                                   password="Brimed@01",
                                   auth_plugin='mysql_native_password',
                                   db="MySQL"

    # open een cursor
    cursor = conn.cursor()

    return conn, cursor


def disconnect(conn, cursor):
        cursor.close()
        conn.close()


class GUI:
    def __init__(self):

        self.__tag = ""
        self.__messages = []
        self.__index = 0

        self.main_window = tkinter.Tk()
        self.main_window.title("PIEP")

        # plaats frames aan mainwindow
        self.top = tkinter.Frame(self.main_window)
        self.middle = tkinter.Frame(self.main_window)
        self.bottom = tkinter.Frame(self.main_window)

        # pack de frames
        self.top.pack()
        self.middle.pack()
        self.bottom.pack()

        # voeg label toe aan frames
        self.message_label = tkinter.Entry(self.top, width=68)
        self.filter_label = tkinter.Label(self.middle,
                                          text="Filter op #:")
        self.tag_label = tkinter.Entry(self.middle, text="")

        # pack labels.
        self.message_label.pack(side="left")
        self.tag_label.pack(side="right")

        # plaats een listbox in mainwindow
        self.listbox = tkinter.Listbox(self.bottom,
                                       selectmode="single",
                                       width=200)

        # voeg items aan listbox toe
        for i in self.__messages:
            self.listbox.insert(self.__index, i)
            self.__index += 1

        # laat listbox zien
        self.listbox.pack(side="left")

        # plaats button op mainwindow
        self.plaats_knop = tkinter.Button(self.top,
                                          text="plaats bericht",
                                          command=self.plaats,
                                          fg="green", )

        self.show_knop = tkinter.Button(self.middle,
                                        text="laat zien",
                                        command=self.show)

        self.quit_button = tkinter.Button(self.bottom, text="quit",
                                          command=self.main_window.destroy,
                                          fg="red")

        # laat de buttons zien,.
        self.plaats_knop.pack(side="left")
        self.quit_button.pack(side="top")
        self.filter_label.pack(side="right")
        self.show_knop.pack(side="right")

        self.main_window.mainloop()

    def plaats(self):
            ber = self.message_label.get()

            if ber != "":
                cursor.execute("insert into piep (bericht, datum, tijd,"
                               " student_nr) "
                        "values ('" + ber + "', curdate(), "
                                            "curtime(), 658542)")
                    conn.commit()

    def show(self):
        tag = self.tag_label.get()
        self.__messages = []

        if tag != "":
            cursor.execute(
                "select voornaam, bericht "
                "from piep join student using (student_nr) "
                "where bericht like '%#" + tag + "%' "
                                                 "order by piep_id desc")
            rij = cursor.fetchall()
            for i in range(len(rij)):
                bericht = (str(rij[i][1]) + " (" +
                           str(rij[i][0]) + ")")
                self.__messages.append(bericht)
        else:
            cursor.execute(
                "select voornaam, bericht "
                "from piep join student using (student_nr) "
                "order by piep_id desc")
            rij = cursor.fetchall()
            for i in range(len(rij)):
                bericht = (str(rij[i][1]) + " (" +
                           str(rij[i][0]) + ")")
                self.__messages.append(bericht)

        self.listbox.delete(0, "end")

        # Add the new items to the listbox.
        for a in self.__messages:
            self.listbox.insert(self.__index, a)
            self.__index += 1

        # Show the listbox.
        self.listbox.pack(side="left")

if __name__ == '__main__':
    conn, cursor = sql_server()
    GUI()
    disconnect(conn, cursor)
