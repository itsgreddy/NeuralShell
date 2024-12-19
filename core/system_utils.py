import platform
import psutil
import socket
import os
from typing import Dict

class SystemUtils:
    @staticmethod
    def get_system_info() -> Dict:
        return {
            'os': platform.system(),
            'version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'hostname': socket.gethostname(),
            'python_version': platform.python_version()
        }
    
    @staticmethod
    def get_memory_info() -> Dict:
        mem = psutil.virtual_memory()
        return {
            'total': mem.total,
            'available': mem.available,
            'percent': mem.percent,
            'used': mem.used,
            'free': mem.free
        }
    
    @staticmethod
    def get_disk_info() -> Dict:
        disk = psutil.disk_usage('/')
        return {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free,
            'percent': disk.percent
        }
    
    @staticmethod
    def get_network_info() -> Dict:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return {
            'hostname': hostname,
            'ip_address': ip_address,
            'interfaces': psutil.net_if_addrs()
        }
    
    @staticmethod
    def get_process_info() -> list:
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return processes