# Port Scanner

A simple Python-based port scanner that allows you to scan a target IP address for open ports within a specified range.

## Features

- Scan a target IP address for open ports
- Specify start and end port range
- Quick scanning with timeout settings
- Simple command-line interface

## Requirements

- Python 3.x
- No additional dependencies required

## Installation

1. Clone this repository:
```bash
git clone https://github.com/syedsherazkazmi613/port-scanner.git
cd port-scanner
```

## Usage

1. Run the script:
```bash
python app.py
```

2. When prompted, enter:
   - Target IP address (e.g., 127.0.0.1)
   - Start port number
   - End port number

Example:
```
Enter target IP (e.g. 127.0.0.1): 127.0.0.1
Start port: 80
End port: 443
```

The scanner will then check each port in the specified range and display any open ports it finds.

## Example Output

```
Scanning 127.0.0.1 from port 80 to 443...

Port 80 is OPEN
Port 443 is OPEN
```

## Notes

- The scanner uses a timeout of 0.5 seconds per port for quick scanning
- Only TCP ports are scanned
- Be mindful of scanning networks you don't own or have permission to scan

## License

This project is open source and available under the MIT License.
