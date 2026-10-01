import os
import json
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

CONFIG_FILE = "bat_launcher_config.json"


class BatLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Bat Launcher")
        self.root.geometry("700x500")
        self.folder = None
        self.bat_files = []
        self.load_config()
        self.build_ui()
        if self.folder and os.path.isdir(self.folder):
            self.refresh_list()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.folder = data.get("folder")
            except Exception:
                self.folder = None

    def save_config(self):
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"folder": self.folder}, f, ensure_ascii=False, indent=2)

    def build_ui(self):
        top = tk.Frame(self.root)
        top.pack(fill="x", padx=10, pady=10)

        self.folder_label = tk.Label(top, text=self.folder or "No folder selected", anchor="w")
        self.folder_label.pack(side="left", fill="x", expand=True)

        tk.Button(top, text="Select Folder", command=self.choose_folder).pack(side="right")
        tk.Button(top, text="Refresh", command=self.refresh_list).pack(side="right", padx=5)

        mid = tk.Frame(self.root)
        mid.pack(fill="both", expand=True, padx=10)

        self.listbox = tk.Listbox(mid, font=("Consolas", 11))
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<Double-Button-1>", lambda e: self.run_selected())

        scrollbar = tk.Scrollbar(mid, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        bottom = tk.Frame(self.root)
        bottom.pack(fill="x", padx=10, pady=10)

        tk.Button(bottom, text="▶ Run", command=self.run_selected,
                  bg="#2e7d32", fg="white", font=("Arial", 10, "bold")).pack(side="left")
        tk.Button(bottom, text="📝 Open in Notepad", command=self.open_in_notepad).pack(side="left", padx=5)
        tk.Button(bottom, text="✖ Exit", command=self.root.quit).pack(side="right")

    def choose_folder(self):
        folder = filedialog.askdirectory(title="Select folder with .bat files")
        if folder:
            self.folder = folder
            self.save_config()
            self.folder_label.config(text=self.folder)
            self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        self.bat_files = []
        if not self.folder or not os.path.isdir(self.folder):
            return
        for name in sorted(os.listdir(self.folder)):
            if name.lower().endswith(".bat"):
                self.bat_files.append(name)
                self.listbox.insert(tk.END, name)

    def get_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Nothing selected", "Select a .bat file from the list.")
            return None
        return os.path.join(self.folder, self.bat_files[sel[0]])

    def run_selected(self):
        path = self.get_selected()
        if not path:
            return
        try:
            subprocess.Popen(["cmd", "/c", "start", "", path], shell=False)
        except Exception as e:
            messagebox.showerror("Launch error", str(e))

    def open_in_notepad(self):
        path = self.get_selected()
        if not path:
            return
        try:
            subprocess.Popen(["notepad.exe", path])
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = BatLauncher(root)
    root.mainloop()import os
import json
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

CONFIG_FILE = "bat_launcher_config.json"


class BatLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Bat Launcher")
        self.root.geometry("700x500")
        self.folder = None
        self.bat_files = []
        self.load_config()
        self.build_ui()
        if self.folder and os.path.isdir(self.folder):
            self.refresh_list()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.folder = data.get("folder")
            except Exception:
                self.folder = None

    def save_config(self):
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"folder": self.folder}, f, ensure_ascii=False, indent=2)

    def build_ui(self):
        top = tk.Frame(self.root)
        top.pack(fill="x", padx=10, pady=10)

        self.folder_label = tk.Label(top, text=self.folder or "No folder selected", anchor="w")
        self.folder_label.pack(side="left", fill="x", expand=True)

        tk.Button(top, text="Select Folder", command=self.choose_folder).pack(side="right")
        tk.Button(top, text="Refresh", command=self.refresh_list).pack(side="right", padx=5)

        mid = tk.Frame(self.root)
        mid.pack(fill="both", expand=True, padx=10)

        self.listbox = tk.Listbox(mid, font=("Consolas", 11))
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<Double-Button-1>", lambda e: self.run_selected())

        scrollbar = tk.Scrollbar(mid, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        bottom = tk.Frame(self.root)
        bottom.pack(fill="x", padx=10, pady=10)

        tk.Button(bottom, text="▶ Run", command=self.run_selected,
                  bg="#2e7d32", fg="white", font=("Arial", 10, "bold")).pack(side="left")
        tk.Button(bottom, text="📝 Open in Notepad", command=self.open_in_notepad).pack(side="left", padx=5)
        tk.Button(bottom, text="✖ Exit", command=self.root.quit).pack(side="right")

    def choose_folder(self):
        folder = filedialog.askdirectory(title="Select folder with .bat files")
        if folder:
            self.folder = folder
            self.save_config()
            self.folder_label.config(text=self.folder)
            self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        self.bat_files = []
        if not self.folder or not os.path.isdir(self.folder):
            return
        for name in sorted(os.listdir(self.folder)):
            if name.lower().endswith(".bat"):
                self.bat_files.append(name)
                self.listbox.insert(tk.END, name)

    def get_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Nothing selected", "Select a .bat file from the list.")
            return None
        return os.path.join(self.folder, self.bat_files[sel[0]])

    def run_selected(self):
        path = self.get_selected()
        if not path:
            return
        try:
            subprocess.Popen(["cmd", "/c", "start", "", path], shell=False)
        except Exception as e:
            messagebox.showerror("Launch error", str(e))

    def open_in_notepad(self):
        path = self.get_selected()
        if not path:
            return
        try:
            subprocess.Popen(["notepad.exe", path])
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = BatLauncher(root)
    root.mainloop()
