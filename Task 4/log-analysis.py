import re
from collections import Counter, defaultdict

LOG_FILE = 'access.log'
# No additional code needed here. This placeholder can be left empty.
LOG_PATTERN = re.compile(
  r'(?P<ip>\S+) \S+ \S+ \[(?P<date>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<code>\d{3}) \S+'
)

def parse_log_line(line):
  match = LOG_PATTERN.match(line)
  if match:
    return match.groupdict()
  return None

def analyze_log(file_path):
  ip_counter = Counter()
  code_counter = Counter()
  url_counter = Counter()
  error_lines = 0

  with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
      data = parse_log_line(line)
      if data:
        ip_counter[data['ip']] += 1
        code_counter[data['code']] += 1
        url_counter[data['url']] += 1
      else:
        error_lines += 1

  return ip_counter, code_counter, url_counter, error_lines

def display_summary(ip_counter, code_counter, url_counter, error_lines):
  print("\nTop 10 IP Addresses:")
  for ip, count in ip_counter.most_common(10):
    print(f"{ip}: {count} times")

  print("\nResponse Codes:")
  for code, count in code_counter.most_common():
    print(f"{code}: {count} times")

  print("\nTop 10 URLs Accessed:")
  for url, count in url_counter.most_common(10):
    print(f"{url}: {count} times")

  print(f"\nLines failed to parse: {error_lines}")

if __name__ == "__main__":
  ip_counter, code_counter, url_counter, error_lines = analyze_log(LOG_FILE)
  display_summary(ip_counter, code_counter, url_counter, error_lines)