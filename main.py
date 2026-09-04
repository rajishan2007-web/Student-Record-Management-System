import tkinter as tk
from tkinter import messagebox
import psycopg2

DB_URL = "postgresql://postgres:dzZl1109OF5DLc0Q@db.mjzrcupgarflnzmconow.supabase.co:5432/postgres"

BG, CARD, BORDER = "#0c0c0c", "#131313", "#222222"
TEXT, MUTED, WHITE, HOVER = "#f0f0f0", "#555555", "#ffffff", "#1a1a1a"
F_TITLE = ("Segoe UI Light", 22)
F_SUB   = ("Segoe UI", 9)
F_LBL   = ("Segoe UI", 8)
F_ENTRY = ("Segoe UI", 11)
F_BTN   = ("Segoe UI Semibold", 9)
F_LIST  = ("Consolas", 10)
F_HEAD  = ("Consolas", 9)

conn, cur, rows = None, None, []

try:
    conn = psycopg2.connect(DB_URL, sslmode='require')
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
        student_id SERIAL PRIMARY KEY, name VARCHAR(100),
        course VARCHAR(50), marks INT, attendance INT)""")
except Exception as e:
    print("Error:", e)

def show_data():
    global rows
    listbox.delete(0, tk.END)
    if not cur: return
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for r in rows:
        listbox.insert(tk.END,
            f"  {str(r[0]).rjust(3)}  {str(r[1] or '').ljust(22)}"
            f"{str(r[2] or '').ljust(16)}{str(r[3] or '').rjust(5)}   {str(r[4] or '').rjust(3)}%")

def clear_fields():
    for e in [e_name, e_course, e_marks, e_att]: e.delete(0, tk.END)

def add_student():
    if not cur: return
    if not e_name.get(): messagebox.showerror("Error", "Name is required"); return
    cur.execute("INSERT INTO students (name,course,marks,attendance) VALUES (%s,%s,%s,%s)",
                (e_name.get(), e_course.get(), e_marks.get(), e_att.get()))
    clear_fields(); show_data()

def update_student():
    sel = listbox.curselection()
    if not cur or not sel: messagebox.showerror("Error", "Select a record"); return
    cur.execute("UPDATE students SET name=%s,course=%s,marks=%s,attendance=%s WHERE student_id=%s",
                (e_name.get(), e_course.get(), e_marks.get(), e_att.get(), rows[sel[0]][0]))
    clear_fields(); show_data()

def delete_student():
    sel = listbox.curselection()
    if not cur or not sel: messagebox.showerror("Error", "Select a record"); return
    cur.execute("DELETE FROM students WHERE student_id=%s", (rows[sel[0]][0],))
    clear_fields(); show_data()

def search_student():
    global rows
    listbox.delete(0, tk.END)
    if not cur: return
    cur.execute("SELECT * FROM students WHERE name ILIKE %s", ('%' + e_name.get() + '%',))
    rows = cur.fetchall()
    for r in rows:
        listbox.insert(tk.END,
            f"  {str(r[0]).rjust(3)}  {str(r[1] or '').ljust(22)}"
            f"{str(r[2] or '').ljust(16)}{str(r[3] or '').rjust(5)}   {str(r[4] or '').rjust(3)}%")

def select_item(event):
    sel = listbox.curselection()
    if sel and sel[0] < len(rows):
        r = rows[sel[0]]; clear_fields()
        e_name.insert(0, r[1] or ""); e_course.insert(0, r[2] or "")
        e_marks.insert(0, str(r[3]) if r[3] is not None else "")
        e_att.insert(0, str(r[4]) if r[4] is not None else "")

def make_btn(parent, text, cmd, primary=False):
    bg0 = WHITE if primary else CARD
    fg0 = BG if primary else TEXT
    bgh = "#dedede" if primary else HOVER
    hl0 = WHITE if primary else BORDER
    b = tk.Label(parent, text=text, font=F_BTN, bg=bg0, fg=fg0,
                 padx=22, pady=10, cursor="hand2",
                 highlightthickness=1, highlightbackground=hl0)
    b.bind("<Enter>",    lambda e: b.config(bg=bgh, highlightbackground=WHITE))
    b.bind("<Leave>",    lambda e: b.config(bg=bg0, highlightbackground=hl0))
    b.bind("<Button-1>", lambda e: cmd())
    return b

def make_entry(parent, label):
    wrap = tk.Frame(parent, bg=CARD, highlightthickness=1, highlightbackground=BORDER)
    tk.Label(wrap, text=label, font=F_LBL, bg=CARD, fg=MUTED).pack(anchor="w", padx=12, pady=(9,0))
    e = tk.Entry(wrap, font=F_ENTRY, bg=CARD, fg=TEXT, bd=0,
                 insertbackground=WHITE, highlightthickness=0)
    e.pack(fill="x", padx=12, pady=(3,9))
    e.bind("<FocusIn>",  lambda ev: wrap.config(highlightbackground=WHITE))
    e.bind("<FocusOut>", lambda ev: wrap.config(highlightbackground=BORDER))
    return wrap, e

root = tk.Tk()
root.title("Student Record Manager")
root.geometry("660x700"); root.resizable(False, False)
root.configure(bg=BG)
root.attributes('-alpha', 0.0)

def fade_in(a=0.0):
    a = min(a + 0.06, 1.0)
    root.attributes('-alpha', a)
    if a < 1.0: root.after(16, fade_in, a)
root.after(50, fade_in)

hdr = tk.Frame(root, bg=BG)
hdr.pack(fill="x", padx=36, pady=(30, 18))
tk.Label(hdr, text="STUDENT RECORDS", font=F_TITLE, bg=BG, fg=WHITE).pack(anchor="w")
tk.Label(hdr, text="add · update · search · delete", font=F_SUB, bg=BG, fg=MUTED).pack(anchor="w", pady=(3,0))

tk.Frame(root, bg=BORDER, height=1).pack(fill="x", padx=36)

form = tk.Frame(root, bg=BG)
form.pack(fill="x", padx=36, pady=18)

row1 = tk.Frame(form, bg=BG); row1.pack(fill="x", pady=(0, 8))
f_name, e_name = make_entry(row1, "NAME")
f_name.pack(side="left", fill="x", expand=True, padx=(0, 8))
f_course, e_course = make_entry(row1, "COURSE")
f_course.pack(side="left", fill="x", expand=True)

row2 = tk.Frame(form, bg=BG); row2.pack(fill="x")
f_marks, e_marks = make_entry(row2, "MARKS")
f_marks.pack(side="left", fill="x", expand=True, padx=(0, 8))
f_att, e_att = make_entry(row2, "ATTENDANCE %")
f_att.pack(side="left", fill="x", expand=True)

btns = tk.Frame(root, bg=BG)
btns.pack(fill="x", padx=36, pady=(14, 0))
make_btn(btns, "ADD", add_student, primary=True).pack(side="left", padx=(0, 8))
make_btn(btns, "UPDATE", update_student).pack(side="left", padx=(0, 8))
make_btn(btns, "DELETE", delete_student).pack(side="left", padx=(0, 8))
make_btn(btns, "SEARCH", search_student).pack(side="left")

tk.Frame(root, bg=BORDER, height=1).pack(fill="x", padx=36, pady=20)

tk.Label(root, font=F_HEAD, bg=BG, fg=MUTED,
         text=f"  {'ID':>3}  {'NAME':<22}{'COURSE':<16}{'MARKS':>5}   {'ATT':>3}"
         ).pack(anchor="w", padx=38, pady=(0, 6))

lb_wrap = tk.Frame(root, bg=CARD, highlightthickness=1, highlightbackground=BORDER)
lb_wrap.pack(fill="both", expand=True, padx=36, pady=(0, 28))

sb = tk.Scrollbar(lb_wrap, orient="vertical", bg=CARD, troughcolor=CARD, bd=0, width=6)
sb.pack(side="right", fill="y", pady=4)

listbox = tk.Listbox(lb_wrap, font=F_LIST, bg=CARD, fg=TEXT, bd=0,
                     highlightthickness=0, selectbackground=HOVER,
                     selectforeground=WHITE, activestyle="none",
                     cursor="hand2", yscrollcommand=sb.set)
listbox.pack(fill="both", expand=True, padx=6, pady=6)
sb.config(command=listbox.yview)
listbox.bind("<<ListboxSelect>>", select_item)

show_data()
root.mainloop()
