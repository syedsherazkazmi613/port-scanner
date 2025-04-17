import socket
import tkinter as tk
from tkinter import ttk, messagebox

def scan_ports(target_ip, start_port, end_port, result_text):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Scanning {target_ip} from port {start_port} to {end_port}...\n\n")
    result_text.update()
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # short timeout for speed
        result = s.connect_ex((target_ip, port))
        if result == 0:
            result_text.insert(tk.END, f"Port {port} is OPEN\n")
            result_text.update()
            open_ports.append(port)
        s.close()
    
    if not open_ports:
        result_text.insert(tk.END, "\nNo open ports found in the specified range.")
    
    result_text.insert(tk.END, "\nScanning completed!")
    result_text.update()

def validate_inputs():
    try:
        target_ip = ip_entry.get()
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
        
        if start_port < 0 or end_port < 0 or start_port > 65535 or end_port > 65535:
            raise ValueError("Ports must be between 0 and 65535")
        if start_port > end_port:
            raise ValueError("Start port must be less than end port")
            
        scan_ports(target_ip, start_port, end_port, result_text)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except socket.gaierror:
        messagebox.showerror("Error", "Invalid IP address")

# Create main window
root = tk.Tk()
root.title("Port Scanner")
root.geometry("500x600")

# Create input frame
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(fill=tk.X)

# IP input
ttk.Label(input_frame, text="Target IP:").pack(anchor=tk.W)
ip_entry = ttk.Entry(input_frame)
ip_entry.insert(0, "127.0.0.1")
ip_entry.pack(fill=tk.X, pady=(0, 10))

# Port range inputs
port_frame = ttk.Frame(input_frame)
port_frame.pack(fill=tk.X)

ttk.Label(port_frame, text="Start Port:").pack(side=tk.LEFT)
start_port_entry = ttk.Entry(port_frame, width=10)
start_port_entry.pack(side=tk.LEFT, padx=(5, 20))

ttk.Label(port_frame, text="End Port:").pack(side=tk.LEFT)
end_port_entry = ttk.Entry(port_frame, width=10)
end_port_entry.pack(side=tk.LEFT, padx=5)

# Scan button
ttk.Button(input_frame, text="Scan Ports", command=validate_inputs).pack(pady=10)

# Results area
result_text = tk.Text(root, height=20, width=50)
result_text.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)

root.mainloop()
