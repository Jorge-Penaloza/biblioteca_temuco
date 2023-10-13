from tkinter import *
  
class Table: 
    def __init__(self,root, lst): 
        total_rows = len(lst) 
        total_columns = len(lst[0]) 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = Entry(root, width=20, fg='blue', 
                               font=('Arial',8), state="readonly") 
                
                self.e.grid(row=i, column=j) 
                self.e.insert(END, lst[i][j])