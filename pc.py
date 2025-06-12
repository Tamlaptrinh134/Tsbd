import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.dialogs import Messagebox
from datetime import datetime
import time 
Window_main = ttk.Window(themename="darkly")
Window_main.title("Tsbd")
Window_main.geometry("1000x800")
TOPRIGHTE = "toprighte"
TOPLEFTE = "toplefte"
BOTTOMRIGHTE = "bottomrighte"
BOTTOMLEFTE = "bottomlefte"
class DataToCreate:
    def __init__(self):
        self.this_year = datetime.now().year
        self.sbdwithname = {}
        self.table = {
            "data": [],
            "position": [None, 190]
        }
        self.school = ""
        self.administrative = ""
        self.title_name = "SƠ ĐỒ ĐÁNH SỐ BÁO DANH"
        self.school_year = f"{self.this_year} - {self.this_year + 1}"
        self.day = ""
        self.sbd_from = 1
        self.sbd_to = 40
        self.size_of_box = 30
        self.distance = 0
        self.margin = [5, 5]
        self.corridor_margin = [15, 5]
        self.table_group = {
            "size": [2, 1],
            "auto": True
        }
        self.table_teacher = {
            "position": [None, 110, 100, 50]
        }
        self.entrance = {
            "type": ["⬅", "➡"],
            "size": 40,
            "anchor": [E, W],
            "position": [None, 150]
        }
        self.top_class = {
            "position": [None, 110, None, self.table_teacher["position"][3]],
            "type": [TOPRIGHTE, TOPLEFTE, BOTTOMRIGHTE, BOTTOMLEFTE]
        }
        self.way_of_arrange = ""
        self.type_this_way = ""
class Commands:
    def List() -> None:
        def close_window():
            Window_list.destroy()
            Button_SBDwithname.config(bootstyle=LIGHT, state=NORMAL)
            Spinbox_SBD_from.config(bootstyle=LIGHT, state=NORMAL)
            Spinbox_SBD_to.config(bootstyle=LIGHT, state=NORMAL)
       
        def add_SBD_with_name():
            nonlocal sbd
            if Entry_name.get() == "":
                Messagebox.show_error("Vui lòng nhập tên học sinh...", "Lỗi")
                return
            if Entry_name.get() in data.sbdwithname.values():
                Messagebox.show_error("Tên học sinh đã tồn tại...", "Lỗi")
                return
            TreeView_list.insert("", "end", values=(Spinbox_SBD.get(), Entry_name.get()))
            Entry_name.delete(0, END)
            sbd += 1 if sbd < int(Spinbox_SBD_to.get()) else 0
            Spinbox_SBD.set(sbd)

        if Spinbox_SBD_from.get() == "" or Spinbox_SBD_to.get() == "":
            Messagebox.show_error("Vui lòng nhập SBD từ.. và đến...", "Lỗi")
            return
        sbd = int(Spinbox_SBD_from.get())
        Spinbox_SBD_from.config(bootstyle=LIGHT, state=DISABLED)
        Spinbox_SBD_to.config(bootstyle=LIGHT, state=DISABLED)
        Button_SBDwithname.config(bootstyle=WARNING, state=DISABLED)

        Window_list = ttk.Toplevel(Window_main)
        Window_list.title("Danh sách SBD với tên")
        Window_list.geometry("600x400")

        Label_list_title = ttk.Label(Window_list, text="Danh sách SBD với tên", font=("Arial", 18), bootstyle=INFO)
        Label_list_title.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky=W)

        Labelframe_enter_directly = ttk.Labelframe(Window_list, text="Nhập trực tiếp", bootstyle=INFO)

        TreeView_list = ttk.Treeview(Labelframe_enter_directly, columns=("SBD", "Tên"), show="headings", bootstyle=LIGHT)
        TreeView_list.heading("SBD", text="SBD")
        TreeView_list.heading("Tên", text="Tên")
        TreeView_list.column("SBD", width=70, anchor=CENTER)
        TreeView_list.column("Tên", width=300, anchor=W)
        TreeView_list.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky=W)

        Label_SBD = ttk.Label(Labelframe_enter_directly, text=f"SBD: ", bootstyle=INFO)
        Label_SBD.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        Spinbox_SBD = ttk.Spinbox(Labelframe_enter_directly, name="sbd", from_=sbd, to=sbd + 1000, width=5, bootstyle=LIGHT)
        Spinbox_SBD.set(sbd)
        Spinbox_SBD.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        type_only_numbers(Spinbox_SBD)

        Label_name = ttk.Label(Labelframe_enter_directly, text="Tên: ", bootstyle=INFO)
        Label_name.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        Entry_name = ttk.Entry(Labelframe_enter_directly, width=30, bootstyle=LIGHT)
        Entry_name.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        placeholder(Entry_name, "Nhập tên của học sinh")

        Button_add = ttk.Button(Labelframe_enter_directly, text="Thêm", bootstyle=SUCCESS)
        Button_add.config(command=lambda: add_SBD_with_name())
        Button_add.grid(row=1, column=4, padx=5, pady=5, sticky=W)

        Labelframe_enter_directly.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        Window_list.protocol("WM_DELETE_WINDOW", close_window)
    def Run_to_create() -> None:
        global tab_list
        for widget in Label_frame_info.winfo_children() + Label_frame_title.winfo_children() + Label_frame_arrange.winfo_children():
            widget.config(state=DISABLED)
        Button_run.config(state=DISABLED)
        data.school = Entry_school.get()
        data.administrative = Entry_administrative.get()
        data.sbdwithname = {} #Temp
        data.table = [[True for _ in range(int(Spinbox_col.get()))] for _ in range(int(Spinbox_row.get()))]
        tab_list += [ttk.Frame(Notebook_preview, bootstyle=DARK)]
        tab_list[-1].pack(fill=BOTH, expand=True)
        Notebook_preview.add(tab_list[-1], text=f"{DataToCreate.school} - {DataToCreate.administrative}")
def px_to_pt(px):
    dpi = Canvas_review.winfo_fpixels('1i')
    pt = px * (72 / dpi)
    return round(pt)
def placeholder(Entry, text) -> None:
    global list_empty_string
    def on_focus_in(event):
        if Entry.get() == text:
            Entry.delete(0, END)
            Entry.config(foreground="white")
    def on_focus_out(event):
        if Entry.get() == "":
            Entry.insert(0, text)
            Entry.config(foreground="grey")
    if Entry.get() == "":
        Entry.config(foreground="grey")
        Entry.insert(0, text)
    list_empty_string += [text]
    Entry.bind("<FocusIn>", on_focus_in)
    Entry.bind("<FocusOut>", on_focus_out)
def check_spinbox(Spinweight):
    check = True
    if not Spinweight.get().isdigit():
        check = False
        print("OH")
    else:
        if Spinweight.cget("from") <= int(Spinweight.get()) <= Spinweight.cget("to"):
            if Spinweight.winfo_name() in ["sbdfrom", "sbdto", "sbdrow", "sbdcol"]:
                if Spinbox_SBD_to.get() != "" and Spinbox_SBD_from.get() != "":
                    if int(Spinbox_SBD_to.get()) < int(Spinbox_SBD_from.get()):
                        check = False
                    elif (int(Spinbox_SBD_to.get()) - int(Spinbox_SBD_from.get()) + 1) > (int(Spinbox_row.get()) * int(Spinbox_col.get())):
                        check = False
            elif Spinweight.winfo_name() == "sbd":
                if Spinweight.get() != "":
                    if int(Spinweight.get()) < int(Spinbox_SBD_from.get()) or int(Spinweight.get()) > int(Spinbox_SBD_to.get()):
                        check = False
            elif Spinweight.winfo_name() == "distance":
                if Spinweight.get() != "":
                    if int(Spinbox_col.get()) * int(Spinbox_row.get()) / (int(Spinweight.get()) + 1) < (int(Spinbox_SBD_to.get()) - int(Spinbox_SBD_from.get()) + 1):
                        check = False
        else:
            check = False
    return check
def type_only_numbers(Spinweight):
    def on_press(event=''):
        check = True
        if not Spinweight.get().isdigit():
            Spinweight.config(bootstyle=DANGER)
            check = False
        else:
            if Spinweight.cget("from") <= int(Spinweight.get()) <= Spinweight.cget("to"):
                Spinweight.config(bootstyle=SUCCESS)
                if Spinweight.winfo_name() in ["sbdfrom", "sbdto", "sbdrow", "sbdcol"]:
                    if Spinbox_SBD_to.get() != "" and Spinbox_SBD_from.get() != "":
                        if int(Spinbox_SBD_to.get()) < int(Spinbox_SBD_from.get()):
                            Spinweight.config(bootstyle=DANGER)
                            check = False
                        elif (int(Spinbox_SBD_to.get()) - int(Spinbox_SBD_from.get()) + 1) > (int(Spinbox_row.get()) * int(Spinbox_col.get())):
                            Spinweight.config(bootstyle=DANGER)
                            check = False
                        else:
                            Spinweight.config(bootstyle=SUCCESS)
                elif Spinweight.winfo_name() == "sbd":
                    if Spinweight.get() != "":
                        if int(Spinweight.get()) < int(Spinbox_SBD_from.get()) or int(Spinweight.get()) > int(Spinbox_SBD_to.get()):
                            Spinweight.config(bootstyle=DANGER)
                            check = False
                        else:
                            Spinweight.config(bootstyle=SUCCESS)
                elif Spinweight.winfo_name() == "distance":
                    if Spinweight.get() != "":
                        if int(Spinbox_col.get()) * int(Spinbox_row.get()) / (int(Spinweight.get()) + 1) < (int(Spinbox_SBD_to.get()) - int(Spinbox_SBD_from.get()) + 1):
                            Spinweight.config(bootstyle=DANGER)
                            check = False
                    else:
                        Spinweight.config(bootstyle=SUCCESS)
            else:
                Spinweight.config(bootstyle=DANGER)
                check = False
        return check
    def on_focus_out(event):
        if not on_press():
            Spinweight.delete(0, END)
            if Spinweight.winfo_name() == "sbd":
                Spinweight.insert(0, Spinbox_SBD_from.get())
        Spinweight.config(bootstyle=LIGHT)

    Spinweight.bind("<KeyRelease>", on_press)
    Spinweight.bind("<FocusOut>", on_focus_out)
def on_combobox_way_of_arrange(event) -> None:
    selected_way = Combobox_wayofarrange.get()
    if list_type_this_way[list_way_of_arrange[selected_way]]:
        Combobox_typethiswayarrange.config(values=list(list_type_this_way[list_way_of_arrange[selected_way]].keys()), state=READONLY)
        Combobox_typethiswayarrange.current(0)
    else:
        Combobox_typethiswayarrange.config(values=["Không có"], state=DISABLED)
        Combobox_typethiswayarrange.current(0)
    if list_way_of_arrange[selected_way] == "manual":
        Button_arrange_manual.grid()
    else:
        Button_arrange_manual.grid_remove()
def check_entry_empty(entry):
    if entry.get() in list_empty_string:
        return False
    return True
def calculator(event=None):
    global data
    match list_way_of_arrange[data.way_of_arrange]:
        case "even_odd":
            temp = data.table["data"][:]
            index = data.sbd_from
            for ir, row in enumerate(data.table["data"]):
                for ic, col in enumerate(row):
                    if index > data.sbd_to:
                        break
                    temp[ir][ic] = index
                    index += 1
            data.table["data"] = temp[:]
            data1d = []
            ldata1d = 0
            for i in data.table["data"]:
                for y in i:
                    if y != "Ô trống":
                        data1d += [y]
                        ldata1d += 1
            #print(ldata1d)
            evendata = list(filter(lambda x: x%2==0 or x==0, data1d))
            odddata = list(filter(lambda x: x%2!=0 and x!=0, data1d))
            match list_type_this_way["even_odd"][data.type_this_way]:
                case "even_first":
                    data1d = evendata + odddata + ["Ô trống" for _ in range(ldata1d - len(evendata + odddata))]
                    temp = data.table["data"][:]
                    index = 0
                    for ir, row in enumerate(data.table["data"]):
                        for ic, col in enumerate(row):
                            #print(index)
                            if index <= len(data1d) - 1:
                                temp[ir][ic] = data1d[index]
                            index += 1
                    data.table["data"] = temp[:]
                    del data1d
                case "odd_first":
                    data1d = odddata + evendata + ["Ô trống" for _ in range(ldata1d - len(odddata + evendata))]
                    temp = data.table["data"][:]
                    index = 0
                    for ir, row in enumerate(data.table["data"]):
                        for ic, col in enumerate(row):
                            #print(index)
                            if index <= len(data1d) - 1:
                                temp[ir][ic] = data1d[index]
                            index += 1
                    data.table["data"] = temp[:]
                    del data1d
def draw() -> None:
    global data
    Canvas_review.delete("all")
    canvas_width = Canvas_review.winfo_width()
    canvas_height = Canvas_review.winfo_height()
    Canvas_review.create_text(100, 15, text=f"{data.administrative}", font=("Arial", px_to_pt(12)), fill="#000000", anchor=CENTER)
    Canvas_review.create_text(100, 30, text=f"{data.school}", font=("Arial", px_to_pt(12), "bold"), fill="#000000", anchor=CENTER)
    Canvas_review.create_text(300, 15, text=f"CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", font=("Arial", px_to_pt(12), "bold"), fill="#000000", anchor=CENTER)
    Canvas_review.create_text(300, 30, text=f"Độc lập - Tự do - Hạnh phúc", font=("Arial", px_to_pt(12), "bold"), fill="#000000", anchor=CENTER)
    Canvas_review.create_text(canvas_width//2, 55, text=data.title_name, font=("Arial", px_to_pt(13), "bold"), fill="#000000", anchor=CENTER)
    Canvas_review.create_text(canvas_width//2, 70, text=f"NĂM HỌC: {data.school_year}", font=("Arial", px_to_pt(13), "bold"), fill="#000000", anchor=CENTER)
    Canvas_review.create_text(canvas_width//2, 85, text=f"NGÀY: {data.day}", font=("Arial", px_to_pt(13), "bold"), fill="#000000", anchor=CENTER)
    calculator()
    if data.table:
        margin = list(data.margin)
        num_rows = len(data.table["data"])
        num_cols = max(len(row) for row in data.table["data"])

        num_row_groups = (num_rows - 1) // data.table_group["size"][1] 
        num_col_groups = (num_cols - 1) // data.table_group["size"][0]

        height = (
            num_rows * data.size_of_box
            + (num_rows - 1 - num_row_groups) * data.margin[1]
            + num_row_groups * data.corridor_margin[1]
        )

        width = (
            num_cols * data.size_of_box
            + (num_cols - 1 - num_col_groups) * data.margin[0]
            + num_col_groups * data.corridor_margin[0]
        )
        data.table["position"][0] = canvas_width // 2 - width // 2
        position = data.table["position"]
        table_group = [1, 1]
        y = position[1]
        for ir, row in enumerate(data.table["data"]):
            if table_group[1] < data.table_group["size"][1]:
                margin_y = data.margin[1]
                table_group[1] += 1
            else:
                margin_y = data.corridor_margin[1]
                table_group[1] = 1
            x = position[0]
            for ic, col in enumerate(row):
                if table_group[0] < data.table_group["size"][0]:
                    margin_x = data.margin[0]
                    table_group[0] += 1
                else:
                    margin_x = data.corridor_margin[0]
                    table_group[0] = 1
                Canvas_review.create_rectangle(
                    x, y,
                    x + data.size_of_box, y + data.size_of_box
                )
                if col != "Ô trống":
                    Canvas_review.create_text(
                        x + data.size_of_box//2,
                        y + data.size_of_box//2,
                        text=f"{col}",
                        font=("Arial", px_to_pt(9)),
                        anchor=CENTER
                    )
                x += data.size_of_box + margin_x
            table_group[0] = 1
            y += data.size_of_box + margin_y
    data.table_teacher["position"][0] = position[0]
    Canvas_review.create_rectangle(
        data.table_teacher["position"][0],
        data.table_teacher["position"][1],
        data.table_teacher["position"][0] + data.table_teacher["position"][2],
        data.table_teacher["position"][1] + data.table_teacher["position"][3]
    )
    Canvas_review.create_text(
        data.table_teacher["position"][0] + data.table_teacher["position"][2]//2,
        data.table_teacher["position"][1] + data.table_teacher["position"][2]//3 - 6,
        text="BÀN GIÁO VIÊN", 
        font=("Arial", px_to_pt(12), "bold"),
        anchor=CENTER
    )
    data.entrance["position"][0] = position[0] + width
    Canvas_review.create_text(
        data.entrance["position"][0],
        data.entrance["position"][1],
        text=data.entrance["type"][0],
        font=("Arial", px_to_pt(data.entrance["size"])),
        anchor=data.entrance["anchor"][0]
    )
    Canvas_review.create_text(
        data.entrance["position"][0],
        data.entrance["position"][1] - 27,
        text="LỐI VÀO", 
        font=("Arial", px_to_pt(12), "bold"),
        anchor=data.entrance["anchor"][0]
    )

def on_check_all_have_type(event=None) -> None:
    check = True
    global canvas_width, canvas_height, data
    for widget in Label_frame_info.winfo_children() + Label_frame_title.winfo_children() + Label_frame_arrange.winfo_children():
        if isinstance(widget, (ttk.Spinbox, ttk.Entry, ttk.Combobox)) and check_entry_empty(widget):
            check = False
    data.school = Entry_school.get() if check_entry_empty(Entry_school) else "Trường không tên"
    data.administrative = Entry_administrative.get() if check_entry_empty(Entry_administrative) else "Không tên"
    data.title_name = Entry_title.get() if check_entry_empty(Entry_title) else "Không tiêu đề"
    data.school_year = Entry_school_year.get() if check_entry_empty(Entry_school_year) else "? - ?"
    data.day = Entry_day.entry.get() if check_entry_empty(Entry_day.entry) else "??/??/????"
    data.way_of_arrange = Combobox_wayofarrange.get()
    data.type_this_way = Combobox_typethiswayarrange.get()
    if check_spinbox(Spinbox_SBD_from) and check_spinbox(Spinbox_SBD_to) and check_spinbox(Spinbox_row) and check_spinbox(Spinbox_col) and check_spinbox(Spinbox_distance):
        data.table["data"] = [["Ô trống" for _ in range(int(Spinbox_col.get()))] for _ in range(int(Spinbox_row.get()))]
        data.sbd_from = int(Spinbox_SBD_from.get())
        data.sbd_to = int(Spinbox_SBD_to.get())
        data.distance = int(Spinbox_distance.get())
        #print(DataToCreate.table)
    if check:
        Button_run.config(state=NORMAL, bootstyle=SUCCESS)
    else:
        Button_run.config(state=DISABLED, bootstyle=DANGER)
    draw()
def on_combobox_type_this_way(event=None) -> None:
    data.type_this_way = Combobox_typethiswayarrange.get()
    draw()
class Commands:
    def List() -> None:
        def close_window():
            Window_list.destroy()
            Button_SBDwithname.config(bootstyle=LIGHT, state=NORMAL)
            Spinbox_SBD_from.config(bootstyle=LIGHT, state=NORMAL)
            Spinbox_SBD_to.config(bootstyle=LIGHT, state=NORMAL)
       
        def add_SBD_with_name():
            nonlocal sbd
            if Entry_name.get() == "":
                Messagebox.show_error("Vui lòng nhập tên học sinh...", "Lỗi")
                return
            if Entry_name.get() in DataToCreate.sbdwithname.values():
                Messagebox.show_error("Tên học sinh đã tồn tại...", "Lỗi")
                return
            TreeView_list.insert("", "end", values=(Spinbox_SBD.get(), Entry_name.get()))
            Entry_name.delete(0, END)
            sbd += 1 if sbd < int(Spinbox_SBD_to.get()) else 0
            Spinbox_SBD.set(sbd)

        if Spinbox_SBD_from.get() == "" or Spinbox_SBD_to.get() == "":
            Messagebox.show_error("Vui lòng nhập SBD từ.. và đến...", "Lỗi")
            return
        sbd = int(Spinbox_SBD_from.get())
        Spinbox_SBD_from.config(bootstyle=LIGHT, state=DISABLED)
        Spinbox_SBD_to.config(bootstyle=LIGHT, state=DISABLED)
        Button_SBDwithname.config(bootstyle=WARNING, state=DISABLED)

        Window_list = ttk.Toplevel(Window_main)
        Window_list.title("Danh sách SBD với tên")
        Window_list.geometry("600x400")

        Label_list_title = ttk.Label(Window_list, text="Danh sách SBD với tên", font=("Arial", 18), bootstyle=INFO)
        Label_list_title.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky=W)

        Labelframe_enter_directly = ttk.Labelframe(Window_list, text="Nhập trực tiếp", bootstyle=INFO)

        TreeView_list = ttk.Treeview(Labelframe_enter_directly, columns=("SBD", "Tên"), show="headings", bootstyle=LIGHT)
        TreeView_list.heading("SBD", text="SBD")
        TreeView_list.heading("Tên", text="Tên")
        TreeView_list.column("SBD", width=70, anchor=CENTER)
        TreeView_list.column("Tên", width=300, anchor=W)
        TreeView_list.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky=W)

        Label_SBD = ttk.Label(Labelframe_enter_directly, text=f"SBD: ", bootstyle=INFO)
        Label_SBD.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        Spinbox_SBD = ttk.Spinbox(Labelframe_enter_directly, name="sbd", from_=sbd, to=sbd + 1000, width=5, bootstyle=LIGHT)
        Spinbox_SBD.set(sbd)
        Spinbox_SBD.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        type_only_numbers(Spinbox_SBD)

        Label_name = ttk.Label(Labelframe_enter_directly, text="Tên: ", bootstyle=INFO)
        Label_name.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        Entry_name = ttk.Entry(Labelframe_enter_directly, width=30, bootstyle=LIGHT)
        Entry_name.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        placeholder(Entry_name, "Nhập tên của học sinh")

        Button_add = ttk.Button(Labelframe_enter_directly, text="Thêm", bootstyle=SUCCESS)
        Button_add.config(command=lambda: add_SBD_with_name())
        Button_add.grid(row=1, column=4, padx=5, pady=5, sticky=W)

        Labelframe_enter_directly.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        Window_list.protocol("WM_DELETE_WINDOW", close_window)
    def Run_to_create() -> None:
        global tab_list
        for widget in Label_frame_info.winfo_children() + Label_frame_title.winfo_children() + Label_frame_arrange.winfo_children():
            widget.config(state=DISABLED)
        Button_run.config(state=DISABLED)
        data.school = Entry_school.get()
        data.administrative = Entry_administrative.get()
        data.sbdwithname = {} #Temp
        data.table = [[True for _ in range(int(Spinbox_col.get()))] for _ in range(int(Spinbox_row.get()))]
        tab_list += [ttk.Frame(Notebook_preview, bootstyle=DARK)]
        tab_list[-1].pack(fill=BOTH, expand=True)
        Notebook_preview.add(tab_list[-1], text=f"{data.school} - {data.administrative}")

data = DataToCreate()
list_empty_string = [""]
Menubar = tk.Menu(Window_main)
Menubar.add_cascade(label="File", menu=ttk.Menu(Menubar, tearoff=0))
Menubar.add_cascade(label="Edit", menu=ttk.Menu(Menubar, tearoff=0))
Menubar.add_cascade(label="View", menu=ttk.Menu(Menubar, tearoff=0))
Menubar.add_cascade(label="Help", menu=ttk.Menu(Menubar, tearoff=0))
Window_main.config(menu=Menubar)

Sidebar = ScrolledFrame(Window_main, width=500, bootstyle=DARK)



Label_frame_title = ttk.Labelframe(Sidebar, text="Tiêu đề: ", bootstyle=INFO)

Label_administrative = ttk.Label(Label_frame_title, text="CQHC:", bootstyle=INFO)
Label_administrative.grid(row=0, column=0, padx=2, pady=2, sticky=W)

Entry_administrative = ttk.Entry(Label_frame_title, width=27, bootstyle=LIGHT)
Entry_administrative.grid(row=0, column=1, padx=2, pady=2, sticky=W)
placeholder(Entry_administrative, "Nhập tên cơ quan hành chính")

Label_school = ttk.Label(Label_frame_title, text="Tên trường:", bootstyle=INFO)
Label_school.grid(row=1, column=0, padx=2, pady=2, sticky=W)

Entry_school = ttk.Entry(Label_frame_title, width=27, bootstyle=LIGHT)
Entry_school.grid(row=1, column=1, padx=2, pady=2, sticky=W)
placeholder(Entry_school, "Nhập tên trường của bạn")

Label_title = ttk.Label(Label_frame_title, text="Tiêu đề:", bootstyle=INFO)
Label_title.grid(row=2, column=0, padx=2, pady=2, sticky=W)

Entry_title = ttk.Entry(Label_frame_title, width=27, bootstyle=LIGHT)
Entry_title.grid(row=2, column=1, padx=2, pady=2, sticky=W)
Entry_title.insert(0, data.title_name)
placeholder(Entry_title, "Nhập tiêu đề của bạn")

Label_school_year = ttk.Label(Label_frame_title, text="Năm học:", bootstyle=INFO)
Label_school_year.grid(row=3, column=0, padx=2, pady=2, sticky=W)

Entry_school_year = ttk.Entry(Label_frame_title, width=27, bootstyle=LIGHT)
Entry_school_year.grid(row=3, column=1, padx=2, pady=2, sticky=W)
Entry_school_year.insert(0, data.school_year)
placeholder(Entry_school_year, "Nhập năm học")

Label_day = ttk.Label(Label_frame_title, text="Ngày:", bootstyle=INFO)
Label_day.grid(row=4, column=0, padx=2, pady=2, sticky=W)

Entry_day = ttk.DateEntry(Label_frame_title, width=27, bootstyle=LIGHT)
Entry_day.grid(row=4, column=1, padx=2, pady=2, sticky=W)
placeholder(Entry_day.entry, "Nhập ngày")

Label_frame_title.grid(row=0, column=0, padx=2, pady=2, sticky=W) 

Label_frame_info = ttk.Labelframe(Sidebar, text="Thông tin: ", bootstyle=INFO)

Label_SBD_from = ttk.Label(Label_frame_info, text="SBD từ:", bootstyle=INFO)
Label_SBD_from.grid(row=0, column=0, padx=2, pady=2, sticky=W)

Spinbox_SBD_from = ttk.Spinbox(Label_frame_info, name="sbdfrom", from_=1, to=1000, width=5, bootstyle=LIGHT)
Spinbox_SBD_from.set(1)
Spinbox_SBD_from.grid(row=0, column=1, padx=2, pady=2, sticky=W)
type_only_numbers(Spinbox_SBD_from)

Label_SBD_to = ttk.Label(Label_frame_info, text="đến:", bootstyle=INFO)
Label_SBD_to.grid(row=0, column=2, padx=2, pady=2, sticky=W)

Spinbox_SBD_to = ttk.Spinbox(Label_frame_info, name="sbdto", from_=1, to=1000, width=5, bootstyle=LIGHT)
Spinbox_SBD_to.set(40)
Spinbox_SBD_to.grid(row=0, column=3, padx=2, pady=2, sticky=W)
type_only_numbers(Spinbox_SBD_to)

Label_SBDwithname = ttk.Label(Label_frame_info, text="SBD với tên (nếu có):", bootstyle=INFO)
Label_SBDwithname.grid(row=1, column=0, padx=2, pady=2, sticky=W)

Button_SBDwithname = ttk.Button(Label_frame_info, text="Danh sách", bootstyle=LIGHT)
Button_SBDwithname.config(command=Commands.List)
Button_SBDwithname.grid(row=1, column=1, columnspan = 3, padx=2, pady=2, sticky=W)

Label_row = ttk.Label(Label_frame_info, text="Số hàng:", bootstyle=INFO)
Label_row.grid(row=2, column=0, padx=2, pady=2, sticky=W)

Spinbox_row = ttk.Spinbox(Label_frame_info, name="sbdrow", from_=1, to=1000, width=5, bootstyle=LIGHT)
Spinbox_row.set(5)
Spinbox_row.grid(row=2, column=1, padx=2, pady=2, sticky=W)
type_only_numbers(Spinbox_row)

Label_col = ttk.Label(Label_frame_info, text="Số cột:", bootstyle=INFO)
Label_col.grid(row=3, column=0, padx=2, pady=2, sticky=W)

Spinbox_col = ttk.Spinbox(Label_frame_info, name="sbdcol", from_=1, to=1000, width=5, bootstyle=LIGHT)
Spinbox_col.set(8)
Spinbox_col.grid(row=3, column=1, padx=2, pady=2, sticky=W)
type_only_numbers(Spinbox_col)

Label_frame_info.grid(row=1, column=0, padx=2, pady=2, sticky=W)

Label_frame_arrange = ttk.Labelframe(Sidebar, text="Sắp xếp: ", bootstyle=INFO)

Label_wayofarrange = ttk.Label(Label_frame_arrange, text="Cách sắp xếp:", bootstyle=INFO)
Label_wayofarrange.grid(row=0, column=0, padx=2, pady=2, sticky=W)

list_way_of_arrange = {
    "Chẳn lẻ": "even_odd",
    "Ngẫu nhiên": "random",
    "Đầu Cuối": "start_end",
    "Xoắn ốc": "spiral",
    "Zigzag": "zigzag",
    "Thủ công": "manual",
}
list_type_this_way = {
    "even_odd": {
        "Chẳn trước": "even_first",
        "Lẻ trước": "odd_first",
    },
    "random": None,
    "start_end": {
        "SBD nhỏ trước": "sbd_small_first",
        "SBD lớn trước": "sbd_large_first",
    },
    "spiral": {
        "Trong ra ngoài": "inside_out",
        "Ngoài vào trong": "outside_in",
    },
    "zigzag": {
        "Từ trái sang phải": "left_to_right",
        "Từ phải sang trái": "right_to_left",
        "Từ trên xuống dưới": "top_to_bottom",
        "Từ dưới lên trên": "bottom_to_top",
    },
    "manual": None,
}
Combobox_wayofarrange = ttk.Combobox(Label_frame_arrange, values=list(list_way_of_arrange.keys()), state="readonly", bootstyle=LIGHT)
Combobox_wayofarrange.current(0)
Combobox_wayofarrange.grid(row=0, column=1, padx=2, pady=2, sticky=W)
Combobox_wayofarrange.bind("<<ComboboxSelected>>", on_combobox_way_of_arrange)
Combobox_wayofarrange.bind("<<ComboboxSelected>>", on_combobox_type_this_way, add="+")

Label_typethiswayarrange = ttk.Label(Label_frame_arrange, text="Kiểu sắp xếp:", bootstyle=INFO)
Label_typethiswayarrange.grid(row=1, column=0, padx=2, pady=2, sticky=W)

Combobox_typethiswayarrange = ttk.Combobox(Label_frame_arrange, values=[], state="readonly", bootstyle=LIGHT)
Combobox_typethiswayarrange.grid(row=1, column=1, padx=2, pady=2, sticky=W)
Combobox_typethiswayarrange.bind("<<ComboboxSelected>>", on_combobox_type_this_way)

Button_arrange_manual = ttk.Button(Label_frame_arrange, text="Thủ công >>", bootstyle=SUCCESS)
Button_arrange_manual.grid(row=999, column=0, padx=2, pady=2, sticky=W)
Button_arrange_manual.grid_remove()
on_combobox_way_of_arrange(None)

Label_distance = ttk.Label(Label_frame_arrange, text="Khoảng cách:", bootstyle=INFO)
Label_distance.grid(row=2, column=0, padx=2, pady=2, sticky=W)

Spinbox_distance = ttk.Spinbox(Label_frame_arrange, name="distance", from_=0, to=10, width=5, bootstyle=LIGHT)
Spinbox_distance.set(0)
Spinbox_distance.grid(row=2, column=1, padx=2, pady=2, sticky=W)
type_only_numbers(Spinbox_distance)

Label_frame_arrange.grid(row=2, column=0, padx=2, pady=2, sticky=W)

Frame_run = ttk.Frame(Sidebar, bootstyle=DARK)

Button_run = ttk.Button(Frame_run, text="Tạo sơ đồ!", bootstyle=DANGER, state=DISABLED)
Button_run.config(command=Commands.Run_to_create)
Button_run.grid(row=0, column=0, padx=2, pady=2, sticky=W)

Frame_run.grid(row=3, column=0, padx=2, pady=2, sticky=W)

#sizegrip = ttk.Sizegrip(Sidebar)
#sizegrip.grid(row=None, column=None, sticky="se")
Sidebar.pack(side=LEFT, fill=Y)

tab_list = []
Notebook_preview = ttk.Notebook(Window_main)

Frame_review_tab = ttk.Frame(Notebook_preview, bootstyle=DARK)

ScrolledFrame_review = ScrolledFrame(Frame_review_tab, bootstyle=DARK)

Frame_canvas_review = ttk.Frame(ScrolledFrame_review, bootstyle=DARK)

Canvas_review = tk.Canvas(Frame_canvas_review, width=420, height=594)
canvas_width = Canvas_review.winfo_width()
canvas_height = Canvas_review.winfo_height()
Canvas_review.config(background="#f3f3f3")
Canvas_review.grid(row=0, column=0, rowspan=15, padx=5, pady=5, sticky=NSEW)

Frame_canvas_review.pack(anchor=SW, expand=True)
Frame_review_tab.pack_propagate(False)

ScrolledFrame_review.pack(fill=BOTH, expand=True)

Frame_review_tab.pack(fill=BOTH, expand=True)

Notebook_preview.add(Frame_review_tab, text=" --- Preview --- ")
Notebook_preview.pack(side=LEFT, fill=BOTH, expand=True)

Window_main.bind("<Button-1>", on_check_all_have_type)
Window_main.bind("<KeyPress>", on_check_all_have_type)
on_check_all_have_type(None)
Window_main.mainloop()