#!/usr/bin/env python3

import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def run_dump():
    db_type = db_var.get()
    host = host_var.get()
    user = user_var.get()
    password = pw_var.get()
    dbname = dbname_var.get()
    exclude_tables = exclude_var.get()
    file_name = filename_var.get() + ".sql"
    path = path_var.get()
    full_path = os.path.join(path, file_name)

    if db_type == "postgres":
        exclude_opts = ' '.join([f"--exclude-table={t}" for t in exclude_tables.split(',') if t.strip()])
        cmd = (
            f"PGPASSWORD='{password}' pg_dump -h {host} -U {user} {exclude_opts} {dbname} > '{full_path}'"
        )
    else:  # mysql
        exclude_opts = ' '.join([f"--ignore-table={dbname}.{t.strip()}" for t in exclude_tables.split(',') if t.strip()])
        cmd = (
            f"mysqldump -h {host} -u {user} --password='{password}' {exclude_opts} {dbname} > '{full_path}'"
        )
    try:
        result = subprocess.run(cmd, shell=True, check=True, stderr=subprocess.PIPE)
        messagebox.showinfo("Success", f"Dump generated at {full_path}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error: {e.stderr.decode()}")

def browse_path():
    dir_selected = filedialog.askdirectory()
    path_var.set(dir_selected)

root = tk.Tk()
root.title("DB Dump Tool")

db_var = tk.StringVar(value="postgres")
host_var = tk.StringVar()
user_var = tk.StringVar()
pw_var = tk.StringVar()
dbname_var = tk.StringVar()
exclude_var = tk.StringVar()
filename_var = tk.StringVar()
path_var = tk.StringVar()

fields = [
    ("DB (postgres/mysql):", ttk.Combobox(root, textvariable=db_var, values=["postgres", "mysql"])),
    ("Host Name:", tk.Entry(root, textvariable=host_var)),
    ("Username:", tk.Entry(root, textvariable=user_var)),
    ("Password:", tk.Entry(root, textvariable=pw_var, show="*")),
    ("Database Name:", tk.Entry(root, textvariable=dbname_var)),
    ("Tables to Exclude (comma separated):", tk.Entry(root, textvariable=exclude_var)),
    ("File Name:", tk.Entry(root, textvariable=filename_var)),
    ("Path:", tk.Entry(root, textvariable=path_var))
]

for i, (label, widget) in enumerate(fields):
    tk.Label(root, text=label).grid(row=i, column=0, sticky=tk.W)
    widget.grid(row=i, column=1, sticky=tk.EW)

tk.Button(root, text="Browse", command=browse_path).grid(row=7, column=2)
tk.Button(root, text="Generate Dump", command=run_dump).grid(row=8, column=0, columnspan=3)
root.mainloop()
