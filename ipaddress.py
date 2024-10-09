# Find the valid ip addresses
import re

# Sample string containing IP addresses
text = """
    Here are some IP addresses:
    192.168.0.1
    10.0.0.1
    172.16.0.1
    and some invalid ones like 999.999.999.999 and 256.256.256.256
"""

# Regular expression pattern for matching IPv4 addresses
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

# Find all IP addresses in the string
ip_addresses = re.findall(ip_pattern, text)

# Filter out invalid IP addresses (0-255 range for each octet)
valid_ip_addresses = [ip for ip in ip_addresses if all(0 <= int(octet) <= 255 for octet in ip.split('.'))]

print("Extracted IP addresses:", valid_ip_addresses)

