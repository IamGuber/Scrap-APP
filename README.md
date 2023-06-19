# Scrap-APP
"Domolazeriai" scraping APP. 

app.py:
The provided code appears to be a Python script that creates a graphical user interface (GUI) using the Tkinter library. The GUI includes a text box for displaying logs, two buttons for starting different functions, and a scheduling mechanism to automate the execution of those functions.
Overall, this code sets up a GUI with buttons to initiate the execution of scraping and email sending functions. Additionally, it includes a scheduling mechanism to automatically trigger these functions at specific times every day. The logs are displayed in a text widget within the GUI to provide feedback on the execution of the functions.

scrap.py:
The provided code is a Python script that performs web scraping using the BeautifulSoup library and automates web browsing tasks with the Selenium library. It extracts sales and shop names data from several Etsy shop URLs and saves the information in a CSV file.
Overall, the code performs web scraping to extract sales and shop names data from multiple Etsy shop URLs(in original working app scraps more like 500 sites). It uses Selenium for browser automation, BeautifulSoup for HTML parsing, and pandas for data manipulation. The extracted data is saved in a CSV file, and statistics like sales differences and sales per day are calculated and added to the file as well.

week_stats.py
The updated code performs additional operations on the extracted sales data from Etsy shop URLs.
The added code calculates the difference in sales between the first and last day of the week and saves the weekly statistics in a separate CSV file. It also provides the functionality to generate an information string for potential use in email sending.

monthly_stats.py
The updated code extends the previous code to calculate monthly statistics for sales data from Etsy shop URLs.
The added code calculates the difference in sales between the first and last day of the month and saves the monthly statistics in a separate CSV file. It also provides the functionality to generate an information string for potential use in email sending.

mail_sending.py
The updated code includes the functionality to send email notifications with the sales statistics.
The added code enables the sending of daily emails with the sorted sales statistics and weekly/monthly emails with sorted weekly/monthly statistics as attachments. The send_email() function handles the email sending functionality, and the schedule library is used to schedule the execution of the email sending functions at specified times.
