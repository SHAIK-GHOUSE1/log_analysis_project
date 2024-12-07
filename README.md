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
## **How It Works**
1. **Log Parsing**: The script reads and parses the log file line by line using regular expressions.
2. **Data Extraction**: Information such as IP addresses, request endpoints, and status codes are extracted.
3. **Analysis**:
   - The number of requests per IP is calculated.
   - The most frequently accessed endpoint is identified.
   - Suspicious activity (failed login attempts) is flagged.
4. **Results**: 
   - Displays the results in the terminal.
   - Saves the results to a CSV file named `log_analysis_results.csv`.

## **CSV Output Structure**
The CSV file will contain three sections:
1. **Requests per IP**:
   - **Columns**: `IP Address`, `Request Count`
2. **Most Accessed Endpoint**:
   - **Columns**: `Endpoint`, `Access Count`
3. **Suspicious Activity**:
   - **Columns**: `IP Address`, `Failed Login Count`

## **Example**
### **Terminal Output**
