import sqlite3 

class DB:

    def sqlite_connection(self):
        try:
            con = sqlite3.connect('times.db')
        except sqlite3.OperationalError:
            print('Error')
        return con

    def create_time_table(self):
        con = self.sqlite_connection() 
        cur = con.cursor()
        try: 
            cur.execute('''create table time 
                            (t_total real, 
                            t_max real,
                            t_min real, 
                            t_average real)
                        ''')
            con.commit()  
            print()
        except sqlite3.OperationalError:
            print('Table already exist')
            
    def insert_times(self,values_time):
        con = self.sqlite_connection() 
        cur = con.cursor()
        try:
            cur.execute('insert into time values(?, ?, ?, ?)',
                        (values_time[0],
                        values_time[1],
                        values_time[2],
                        values_time[3])
            )
            con.commit()
            print('Data inserted correctly')
        except sqlite3.OperationalError:
            print('Error on insert times')    
            con.close()