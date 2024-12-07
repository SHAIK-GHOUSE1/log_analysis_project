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
- **Pandas** (for data handling and analysis)

## **Getting Started**
### **1. Clone the Repository**
```bash
git clone https://github.com/SHAIK-GHOUSE1/log_analysis_project.git
