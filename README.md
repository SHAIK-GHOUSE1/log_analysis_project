# **Log Analysis Project**

## **Project Overview**
This project analyzes web server log files to gather insights on the traffic, endpoints, and suspicious activity. It parses the logs, extracts useful information, and generates detailed reports. The results are displayed in the terminal and saved to a CSV file for further analysis.

## **Features**
### **1. Requests Per IP Address**
- Analyzes how many requests were made by each IP address.
- Displays the count for each IP.

### **2. Most Accessed Endpoint**
- Finds the most frequently accessed endpoint on the server.
- Displays the endpoint and its access count.

### **3. Suspicious Activity Detection**
- Identifies suspicious activity such as failed login attempts (status code 401).
- Displays the IP addresses with multiple failed login attempts.

## **Technologies Used**
- **Python** (for scripting and data analysis)
- **CSV** (for data storage and reporting)
- **Regular Expressions** (for log parsing)


## **Getting Started**
### **1. Clone the Repository**
git clone https://github.com/SHAIK-GHOUSE1/log_analysis_project.git
## **2. Run the Script**
### Execute the script to analyze the log file:
python log_analysis.py

## **How It Works**
**Log Parsing**: The script reads and parses the log file line by line using regular expressions.</br>
**Data Extraction**: Information such as IP addresses, request endpoints, and status codes are extracted.
## **Analysis:**
The number of requests per IP is calculated.</br>
The most frequently accessed endpoint is identified.</br>
Suspicious activity (failed login attempts) is flagged.</br>
**Results:**
Displays the results in the terminal.</br>
Saves the results to a CSV file named log_analysis_results.csv.</br>
 ## CSV Output Structure
The CSV file will contain three sections:

## Requests per IP:</br>
**Columns:** IP Address, Request Count
## Most Accessed Endpoint:</br>
**Columns:** Endpoint, Access Count
 ## Suspicious Activity:</br>
**Columns:** IP Address, Failed Login Count</br>

## Terminal Output:</br>
**Requests per IP Address**</br>
203.0.113.5: 8</br>
198.51.100.23: 8</br>
192.168.1.1: 7</br>
10.0.0.2: 6</br>

**Most Frequently Accessed Endpoint**</br>
/login (Accessed 13 times)</br>
**Suspicious Activity Detected**</br>
IP 203.0.113.5 has 8 failed login attempts</br>
## CSV Output
![Screenshot 2024-12-07 122818](https://github.com/user-attachments/assets/e42eaea3-e652-49c1-9067-9c486925fa3b)
## **Contact Information**
- **Name**: Shaik Mohammed Ghouse
- **Email**: shaikghousemohammed045@gmail.com
