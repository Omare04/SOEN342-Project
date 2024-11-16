import threading
from utils.utils import read_csv as base_read_csv, write_csv as base_write_csv, append_csv as base_append_csv

class CSVLockManager:
    writer_lock = threading.RLock()  # Ensure writers operate in self-exclusion
    readers = 0  # Keep track of the number of readers
    condition = threading.Condition()  # Synchronize readers and writers

    @staticmethod
    def read_csv_safe(file_path):
        with CSVLockManager.condition:
            CSVLockManager.readers += 1
        try:
            return base_read_csv(file_path)
        finally:
            with CSVLockManager.condition:
                CSVLockManager.readers -= 1
                if CSVLockManager.readers == 0:
                    CSVLockManager.condition.notify_all()

    @staticmethod
    def write_csv_safe(file_path, data, fieldnames):
        with CSVLockManager.writer_lock:
            base_write_csv(file_path, data, fieldnames)

    @staticmethod
    def append_csv_safe(file_path, row, fieldnames):
        with CSVLockManager.writer_lock:
            base_append_csv(file_path, row, fieldnames)
