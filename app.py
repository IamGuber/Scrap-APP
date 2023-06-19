# imports

import tkinter as tk
import subprocess
import schedule
import time
import threading
import datetime


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DomoLazeriai scrap APP. By IamGuber.")
        
        # info log

        self.log = tk.Text(self.root, height=10, width=50)
        self.log.pack()
        
        # push button

        self.button = tk.Button(self.root, text="Start scrap", command=self.start_function)
        self.button.pack()

         # push button2

        self.button = tk.Button(self.root, text="Start email", command=self.start_function2)
        self.button.pack()
        
        # schedule the Start button to be clicked every day by clock

        schedule.every().day.at("06:00").do(self.start_function)

        # schedule the Start button2 to be clicked every day by clock

        schedule.every().day.at("09:00").do(self.start_function2)


    def start_function2(self):
        self.log.insert(tk.END, "\nStarting email sending...\n")

        # start email file sending

        try:
            subprocess.Popen(["python", "/Users/voisk/Desktop/SCRAPING APP/mail_sending.py"])
            self.log.insert(tk.END, "Email send successfully.\n" f"{datetime.datetime.now()}")
        except Exception as e:
            self.log.insert(tk.END, f"Error sending email file: {str(e)}\n")
        

    def start_function(self):
        self.log.insert(tk.END, "\nStarting scrap function...\n")

        # start scrap file 

        try:
            subprocess.Popen(["python", "/Users/voisk/Desktop/SCRAPING APP/scrap.py"])
            self.log.insert(tk.END, "Scrap file started successfully.\n" f"{datetime.datetime.now()}")
        except Exception as e:
            self.log.insert(tk.END, f"Error starting scrap file: {str(e)}\n")


    def run(self):

        # start the scheduler in a new thread

        schedule_thread = threading.Thread(target=self.schedule_loop, daemon=True)
        schedule_thread.start()
        
        # start the GUI

        self.root.mainloop()
    

    def schedule_loop(self):

        # run the scheduler loop in the background

        while True:
            schedule.run_pending()
            time.sleep(1)


# create and run the GUI

gui = GUI()
gui.run()