def read_log_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []


# Test the function
if __name__ == "__main__":
    log_file_path = "sample.log"
    log_lines = read_log_file(log_file_path)
    print(f"Read {len(log_lines)} lines from {log_file_path}")
import re


def parse_log_line(line):
    """
    Parse a single log line to extract the IP, endpoint, and status code.
    Returns a tuple (IP, endpoint, status_code) or None if the line is invalid.
    """
    log_pattern = (
        r"(?P<ip>\d+\.\d+\.\d+\.\d+) - - "
        r"\[.*?\] "
        r'"(?:GET|POST) (?P<endpoint>\S+) .*?" '
        r"(?P<status>\d+)"
    )
    match = re.match(log_pattern, line)
    if match:
        return match.group("ip"), match.group("endpoint"), int(match.group("status"))
    return None


def process_log_file(file_path):
    parsed_data = []
    with open(file_path, "r") as file:
        for line in file:
            parsed_entry = parse_log_line(line)
            if parsed_entry:
                parsed_data.append(parsed_entry)
    return parsed_data


# Test the function
log_file_path = "sample.log"
parsed_data = process_log_file(log_file_path)
print(f"Parsed {len(parsed_data)} valid log entries.")
print(parsed_data[:5])  # Show the first 5 entries
from collections import Counter


def count_requests_per_ip(parsed_data):
    """
    Count the number of requests made by each IP address.
    Returns a sorted list of tuples (IP, count) in descending order of count.
    """
    ip_counts = Counter(entry[0] for entry in parsed_data)
    sorted_ip_counts = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_ip_counts


# Test the function
ip_request_counts = count_requests_per_ip(parsed_data)
print("Requests per IP Address:")
for ip, count in ip_request_counts:
    print(f"{ip}: {count}")
import csv


def save_requests_per_ip_to_csv(ip_request_counts, filename="log_analysis_results.csv"):
    """
    Saves the requests per IP data to a CSV file.
    """
    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP Address", "Request Count"])  # Header
        writer.writerows(ip_request_counts)
    print(f"Requests per IP data saved to {filename}")


# Call the function
save_requests_per_ip_to_csv(ip_request_counts)
import csv
from collections import Counter


def parse_log_file(log_file_path):
    log_entries = []
    with open(log_file_path, "r") as file:
        lines = file.readlines()
        print(f"Read {len(lines)} lines from {log_file_path}")
        for line in lines:
            # Sample log entry: 192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
            parts = line.split(" ")
            if len(parts) > 6:
                ip_address = parts[0]
                endpoint = parts[6]
                status_code = int(parts[8])
                log_entries.append((ip_address, endpoint, status_code))
    print(f"Parsed {len(log_entries)} valid log entries.")
    return log_entries


def find_most_accessed_endpoint(log_entries):
    """
    Finds the most frequently accessed endpoint from the log entries.
    """
    endpoints = [entry[1] for entry in log_entries]
    endpoint_counts = Counter(endpoints)
    most_accessed_endpoint, count = endpoint_counts.most_common(1)[0]
    return most_accessed_endpoint, count


def save_most_accessed_endpoint_to_csv(
    endpoint, count, filename="log_analysis_results.csv"
):
    """
    Saves the most accessed endpoint data to the CSV file.
    """
    with open(filename, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([endpoint, count])
    print(f"Most accessed endpoint data saved to {filename}")


# Main logic
log_file_path = "sample.log"
log_entries = parse_log_file(log_file_path)

# Find the most accessed endpoint
most_accessed_endpoint, access_count = find_most_accessed_endpoint(log_entries)

# Display the result
print(
    f"Most Frequently Accessed Endpoint: {most_accessed_endpoint} (Accessed {access_count} times)"
)

# Save the result to CSV
save_most_accessed_endpoint_to_csv(most_accessed_endpoint, access_count)
from collections import defaultdict


def detect_suspicious_activity(log_entries, threshold=5):
    """
    Detects suspicious activity based on failed login attempts (HTTP status 401).
    """
    failed_attempts = defaultdict(
        int
    )  # Default dictionary to count failed attempts per IP
    for entry in log_entries:
        ip_address, endpoint, status_code = entry
        if status_code == 401 and "/login" in endpoint:
            failed_attempts[ip_address] += 1

    suspicious_ips = {
        ip: count for ip, count in failed_attempts.items() if count > threshold
    }
    return suspicious_ips


def save_suspicious_activity_to_csv(
    suspicious_ips, filename="log_analysis_results.csv"
):
    """
    Saves suspicious activity data to the CSV file.
    """
    with open(filename, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for ip, count in suspicious_ips.items():
            writer.writerow([ip, f"Suspicious: {count} failed login attempts"])
    print(f"Suspicious activity data saved to {filename}")


# Main logic (continuing from previous code)
suspicious_ips = detect_suspicious_activity(log_entries, threshold=5)

# Display the suspicious IPs
if suspicious_ips:
    print("Suspicious Activity Detected:")
    for ip, count in suspicious_ips.items():
        print(f"IP {ip} has {count} failed login attempts")
    save_suspicious_activity_to_csv(suspicious_ips)
else:
    print("No suspicious activity detected.")
