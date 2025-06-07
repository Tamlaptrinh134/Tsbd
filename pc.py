from tkinter import * 
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.dialogs import Messagebox
Window_main = ttk.Window(themename="darkly")
Window_main.title("Tsbd")
Window_main.geometry("1000x800")
class DataToCreate:
    def __init__(self):
        self.sbdwithname = {}
        self.table = []
        self.school = ""
        self.class_name = ""
        self.title_name = "SƠ ĐỒ ĐÁNH SỐ BÁO DANH"
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
        DataToCreate.school = Entry_school.get()
        DataToCreate.class_name = Entry_class.get()
        DataToCreate.sbdwithname = {} #Temp
        DataToCreate.table = [[True for _ in range(int(Spinbox_col.get()))] for _ in range(int(Spinbox_row.get()))]
        tab_list += [ttk.Frame(Notebook_preview, bootstyle=DARK)]
        tab_list[-1].pack(fill=BOTH, expand=True)
        Notebook_preview.add(tab_list[-1], text=f"{DataToCreate.school} - {DataToCreate.class_name}")

def placeholder(Entry, text) -> None:
    def on_focus_in(event):
        if Entry.get() == text:
            Entry.delete(0, END)
            Entry.config(foreground="white")
    def on_focus_out(event):
        if Entry.get() == "":
            Entry.insert(0, text)
            Entry.config(foreground="grey")

    Entry.config(foreground="grey")
    Entry.insert(0, text)
    Entry.bind("<FocusIn>", on_focus_in)
    Entry.bind("<FocusOut>", on_focus_out)
def check_spinbox(Spinweight):
    check = True
    if not Spinweight.get().isdigit():
        check = False
    else:
        if Spinweight.cget("from") <= int(Spinweight.get()) <= Spinweight.cget("to"):
            if Spinweight.winfo_name() in ["sbdfrom", "sbdto"]:
                if Spinbox_SBD_to.get() != "" and Spinbox_SBD_from.get() != "":
                    if int(Spinbox_SBD_to.get()) < int(Spinbox_SBD_from.get()):
                        check = False
                    elif (int(Spinbox_SBD_to.get()) - int(Spinbox_SBD_from.get()) + 1) > (int(Spinbox_row.get()) * int(Spinbox_col.get())):
                        check = False
            elif Spinweight.winfo_name() == "sbd":
                if Spinweight.get() != "":
                    if int(Spinweight.get()) < int(Spinbox_SBD_from.get()) or int(Spinweight.get()) > int(Spinbox_SBD_to.get()):
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
                if Spinweight.winfo_name() in ["sbdfrom", "sbdto"]:
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

def on_combobox_type_thi_way(event) -> None:
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
def check_entry_empty(Entry):
    if Entry.get() in ["", "Nhập lớp của bạn", "Nhập tên trường của bạn"]:
        return False
    return True
def on_check_all_have_type(event) -> None:
    check = True
    global canvas_width, canvas_height, data
    for widget in Label_frame_info.winfo_children() + Label_frame_title.winfo_children() + Label_frame_arrange.winfo_children():
        if isinstance(widget, (ttk.Spinbox, ttk.Entry, ttk.Combobox)) and check_entry_empty(widget):
            check = False
    data.school = Entry_school.get() if check_entry_empty(Entry_school) else "Không tên"
    data.class_name = Entry_class.get() if check_entry_empty(Entry_class) else "Không tên"
    if check_spinbox(Spinbox_SBD_from) and check_spinbox(Spinbox_SBD_to):
        data.table = [[True for _ in range(int(Spinbox_col.get()))] for _ in range(int(Spinbox_row.get()))]
        #print(DataToCreate.table)
    if check:
        Button_run.config(state=NORMAL, bootstyle=SUCCESS)
    else:
        Button_run.config(state=DISABLED, bootstyle=DANGER)
    
    Canvas_review.delete("all")
    canvas_width = Canvas_review.winfo_width()
    canvas_height = Canvas_review.winfo_height()
    Canvas_review.create_text(canvas_width//2, 25, text=f"Trường: {data.school}", font=("Font", 17), fill="#000000", anchor=CENTER)
    Canvas_review.create_text(canvas_width//2, 50, text=f"Lớp: {data.class_name}", font=("Font", 15), fill="#000000", anchor=CENTER)
    Canvas_review.create_line(50, 70, canvas_width - 50, 70, fill="#000000", width=1)
    Canvas_review.create_text(canvas_width//2, 90, text=data.title_name, font=("Font", 12), fill="#000000", anchor=CENTER)

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
        data.class_name = Entry_class.get()
        data.sbdwithname = {} #Temp
        data.table = [[True for _ in range(int(Spinbox_col.get()))] for _ in range(int(Spinbox_row.get()))]
        tab_list += [ttk.Frame(Notebook_preview, bootstyle=DARK)]
        tab_list[-1].pack(fill=BOTH, expand=True)
        Notebook_preview.add(tab_list[-1], text=f"{data.school} - {data.class_name}")

        
Menubar = Menu(Window_main)
Menubar.add_cascade(label="File", menu=ttk.Menu(Menubar, tearoff=0))
Menubar.add_cascade(label="Edit", menu=ttk.Menu(Menubar, tearoff=0))
Menubar.add_cascade(label="View", menu=ttk.Menu(Menubar, tearoff=0))
Menubar.add_cascade(label="Help", menu=ttk.Menu(Menubar, tearoff=0))
Window_main.config(menu=Menubar)

Sidebar = ScrolledFrame(Window_main, width=320, bootstyle=DARK)

Label_frame_title = ttk.Labelframe(Sidebar, text="Tiêu đề: ", bootstyle=INFO)

Label_school = ttk.Label(Label_frame_title, text="Tên trường:", bootstyle=INFO)
Label_school.grid(row=0, column=0, padx=2, pady=2, sticky=W)

Entry_school = ttk.Entry(Label_frame_title, width=27, bootstyle=LIGHT)
Entry_school.grid(row=0, column=1, padx=2, pady=2, sticky=W)
placeholder(Entry_school, "Nhập tên trường của bạn")

Label_class = ttk.Label(Label_frame_title, text="Lớp:", bootstyle=INFO)
Label_class.grid(row=1, column=0, padx=2, pady=2, sticky=W)

Entry_class = ttk.Entry(Label_frame_title, width=27, bootstyle=LIGHT)
Entry_class.grid(row=1, column=1, padx=2, pady=2, sticky=W)
placeholder(Entry_class, "Nhập lớp của bạn")

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

Spinbox_row = ttk.Spinbox(Label_frame_info, from_=1, to=1000, width=5, bootstyle=LIGHT)
Spinbox_row.set(10)
Spinbox_row.grid(row=2, column=1, padx=2, pady=2, sticky=W)
type_only_numbers(Spinbox_row)

Label_col = ttk.Label(Label_frame_info, text="Số cột:", bootstyle=INFO)
Label_col.grid(row=3, column=0, padx=2, pady=2, sticky=W)

Spinbox_col = ttk.Spinbox(Label_frame_info, from_=1, to=1000, width=5, bootstyle=LIGHT)
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
data = DataToCreate()
Combobox_wayofarrange = ttk.Combobox(Label_frame_arrange, values=list(list_way_of_arrange.keys()), state="readonly", bootstyle=LIGHT)
Combobox_wayofarrange.current(0)
Combobox_wayofarrange.grid(row=0, column=1, padx=2, pady=2, sticky=W)
Combobox_wayofarrange.bind("<<ComboboxSelected>>", on_combobox_type_thi_way)

Label_typethiswayarrange = ttk.Label(Label_frame_arrange, text="Kiểu sắp xếp:", bootstyle=INFO)
Label_typethiswayarrange.grid(row=1, column=0, padx=2, pady=2, sticky=W)

Combobox_typethiswayarrange = ttk.Combobox(Label_frame_arrange, values=[], state="readonly", bootstyle=LIGHT)
Combobox_typethiswayarrange.grid(row=1, column=1, padx=2, pady=2, sticky=W)

Button_arrange_manual = ttk.Button(Label_frame_arrange, text="Thủ công >>", bootstyle=SUCCESS)
Button_arrange_manual.grid(row=None, column=0, padx=2, pady=2, sticky=W)
Button_arrange_manual.grid_remove()
on_combobox_type_thi_way(None)

Label_distance = ttk.Label(Label_frame_arrange, text="Khoảng cách:", bootstyle=INFO)
Label_distance.grid(row=2, column=0, padx=2, pady=2, sticky=W)

Spinbox_distance = ttk.Spinbox(Label_frame_arrange, from_=0, to=10, width=5, bootstyle=LIGHT)
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
Sidebar.pack_propagate(False)

tab_list = []
Notebook_preview = ttk.Notebook(Window_main)

Frame_review_tab = ttk.Frame(Notebook_preview, bootstyle=DARK)

ScrolledFrame_review = ScrolledFrame(Frame_review_tab, bootstyle=DARK)

Frame_canvas_review = ttk.Frame(ScrolledFrame_review, bootstyle=DARK)

Canvas_review = Canvas(Frame_canvas_review, width=420, height=594)
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