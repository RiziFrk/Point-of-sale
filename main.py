from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox


class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("Point of Sale")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='cadetblue')

        Change_Input = StringVar()
        Cash_Input = StringVar()
        Tax_Input = StringVar()
        SubTotal_Input = StringVar()
        Total_Input = StringVar()
        Item = StringVar()
        Qty = StringVar()
        Amount = StringVar()
        Choice = StringVar()
        #===========================================================Functions========================================================================================================#

        def delete():
            ItemCost=0
            Tax = 2.5
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
            SubTotal_Input.set(str('£%.2f' % (ItemCost)))
            Tax_Input.set(str('£%.2f'%(((ItemCost-2.3)*Tax)/100)))
            Total_Input.set(str('£%.2f'%((ItemCost-2.3) + ((ItemCost-2.3) * Tax) /100)))
            selected_item = (self.POS_records.selection()[0])
            self.POS_records.delete(selected_item)

        def giveChange():
            ItemCost = 0
            Tax = 2.5
            CashInput = float(Cash_Input.get())
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
            Change_Input.set(str('£%.2f' % (CashInput - ((ItemCost) + ((ItemCost * Tax)/100)))))
            if (Cash_Input.get() == "0"):
                Change_Input.set(" ")
                Method_of_Pay()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Point of Sale", "Do you want to quit?")
            if iExit > 0:
                root.destroy()
                return

        def Method_of_Pay():
            if (Choice.get() == "Cash"):
                self.txtCost.focus()
                Cash_Input.set("")
            elif (Choice.get() == ""):
                Cash_Input.set("0")
                Change_Input.set("")

        def Reset():
            Reset = tkinter.messagebox.askyesno("Point of sale", "Do you want to clear all data?")
            if Reset == YES:
                Cash_Input.set ("")
                Change_Input.set("")
                Tax_Input.set("")
                SubTotal_Input.set("")
                Total_Input.set("")


                return
        #============================================================================================================================================================================#
        MainFrame = Frame(self.root, bg='cadetblue')
        MainFrame.grid(padx=8, pady=5)

        ButtonFrame = Frame(MainFrame, bg='cadetblue', bd=5, width=1348, height=160, padx=4, pady=4, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bg='cadetblue', bd=5, width=800, height=300, padx=4, pady=4, relief=RIDGE)
        DataFrame.pack(side=LEFT)

        DataFrameLEFTCOVER = LabelFrame(DataFrame, bg='cadetblue', bd=5, width=800, height=300, padx=4, pady=4, font=('arial', 12, 'bold'), text="Point of Sale", relief=RIDGE)

        DataFrameLEFTCOVER.pack(side=LEFT)

        ChangeButtonFrame = Frame(DataFrameLEFTCOVER, bd=5, width=300, height=460, pady=4, relief=RIDGE)
        ChangeButtonFrame.pack(side=LEFT, padx=4)

        ReceiptFrame = Frame(DataFrameLEFTCOVER, bd=5, width=200, height=400, pady=5, padx=1, relief=RIDGE)
        ReceiptFrame.pack(side=RIGHT, padx=4)

        FoodItemFrame = LabelFrame(DataFrame, bd=5, width=450, height=600, padx=5, pady=2, relief=RIDGE, bg='cadetblue', font=('arial', 12, 'bold'), text="Items")
        FoodItemFrame.pack(side=RIGHT)

        CalFrame = Frame(ButtonFrame, bd=5, width=432, height=140, relief=RIDGE)
        CalFrame.grid(row=0, column=0, padx=5)

        ChangeFrame = Frame(ButtonFrame, bd=5, width=400, height=140, pady=2, relief=RIDGE)
        ChangeFrame.grid(row=0, column=1, padx=5)

        RemoveFrame = Frame(ButtonFrame, bd=5, width=400, height=140, pady=4, relief=RIDGE)
        RemoveFrame.grid(row=0, column=2, padx=5)
        # =============================================================Entry & Label Widget========================================================================================#
        self.lblSubTotal = Label(CalFrame, font=('arial', 14, 'bold'), text="Sub Total", bd=5)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5)
        self.txtSubTotal = Entry(CalFrame, font=('arial', 14, 'bold'), textvariable = SubTotal_Input, bd=2, width=24)
        self.txtSubTotal.grid(row=0, column=1, sticky=W, padx=5)

        self.lblTax = Label(CalFrame, font=('arial', 14, 'bold'), text="Tax", bd=5)
        self.lblTax.grid(row=1, column=0, sticky=W, padx=5)
        self.txtTax = Entry(CalFrame, font=('arial', 14, 'bold'), textvariable=Tax_Input, bd=2, width=24)
        self.txtTax.grid(row=1, column=1, sticky=W, padx=5)

        self.lblTotal = Label(CalFrame, font=('arial', 14, 'bold'), text="Total", bd=5)
        self.lblTotal.grid(row=2, column=0, sticky=W, padx=5)
        self.txtTotal = Entry(CalFrame, font=('arial', 14, 'bold'), textvariable=Total_Input, bd=2, width=24)
        self.txtTotal.grid(row=2, column=1, sticky=W, padx=5)
        # =============================================================Entry & Label Widget========================================================================================#
        self.lblMoP = Label(ChangeFrame, font=('arial', 14, 'bold'), text="Method of Payment", bd=5)
        self.lblMoP.grid(row=0, column=0, sticky=W, padx=5)
        self.cboMoP = ttk.Combobox(ChangeFrame, font=('arial', 14, 'bold'), width=34, state='readonly', textvariable=Choice, justify=RIGHT)

        self.cboMoP['values'] = ('Bitcoin','Cash','Ethereum', 'Master Card', 'Visa Card')
        self.cboMoP.current(0)
        self.cboMoP.grid(row=0, column=1)

        self.lblCost = Label(ChangeFrame, font=('arial', 14, 'bold'), text="Cash", bd=5)
        self.lblCost.grid(row=1, column=0, sticky=W, padx=5)
        self.txtCost = Entry(ChangeFrame, font=('arial', 14, 'bold'), textvariable=Cash_Input, bd=2, width=36,justify=RIGHT)
        self.txtCost.insert(0, "0")
        self.txtCost.grid(row=1, column=1, sticky=W, padx=2)

        self.lblChange = Label(ChangeFrame, font=('arial', 14, 'bold'), text="Change", bd=5)
        self.lblChange.grid(row=2, column=0, sticky=W, padx=5)
        self.txtChange = Entry(ChangeFrame, font=('arial', 14, 'bold'), textvariable=Change_Input, bd=2, width=34, justify=RIGHT)
        self.txtChange.grid(row=2, column=1, sticky=W, padx=5)
        # =============================================================Button Widget========================================================================================#
        self.btnPay = Button(RemoveFrame, padx=2, font=('arial', 15, 'bold'), text="Pay", width=10, height=1, bd=2, command=giveChange)
        self.btnPay.grid(row=0, column=0, pady=2, padx=7)

        self.btnExit = Button(RemoveFrame, padx=2, font=('arial', 15, 'bold'), text="Exit", width=10, height=1, bd=2, command=iExit)
        self.btnExit.grid(row=0, column=1, pady=2, padx=7)

        self.btnReset = Button(RemoveFrame, padx=2, font=('arial', 15, 'bold'), text="Reset", width=10, height=1, bd=2, command = Reset)
        self.btnReset.grid(row=1, column=0, pady=2, padx=7)

        self.btnRemove_Item = Button(RemoveFrame, padx=2, font=('arial', 15, 'bold'), text="Remove Item", width=10, height=1, bd=2, command=delete)
        self.btnRemove_Item.grid(row=1, column=1, pady=2, padx=7)
        # =============================================================Function===============================================================================================#

        def Item1():
            ItemCost = 2.30
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 1", 1, 2.30))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-2.3)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-2.3) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 2.3) + ((ItemCost - 2.3) * Tax) / 100)))

        def Item2():
            ItemCost = 1.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 2", 1, 1.90))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-1.9)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-1.9) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.9) + ((ItemCost - 1.9) * Tax) / 100)))

        def Item3():
            ItemCost = 3.20
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 3", 1, 3.20))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-3.2)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-3.2) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 3.2) + ((ItemCost - 3.2) * Tax) / 100)))

        def Item4():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 4", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-1.1)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-1.1) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item5():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 5", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item6():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 6", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item7():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 7", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item8():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 8", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item9():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 9", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item10():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 10", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-1.1)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-1.1) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item11():
            ItemCost = 2.30
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 11", 1, 2.30))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-2.3)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-2.3) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 2.3) + ((ItemCost - 2.3) * Tax) / 100)))

        def Item12():
            ItemCost = 1.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 12", 1, 1.90))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-1.9)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-1.9) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.9) + ((ItemCost - 1.9) * Tax) / 100)))

        def Item13():
            ItemCost = 3.20
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 13", 1, 3.20))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-3.2)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-3.2) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 3.2) + ((ItemCost - 3.2) * Tax) / 100)))

        def Item14():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 14", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-1.1)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-1.1) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item15():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 15", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item16():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 16", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item17():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 17", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item18():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 18", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item19():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 19", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item20():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 20", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-1.1)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-1.1) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item21():
            ItemCost = 2.30
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 21", 1, 2.30))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-2.3)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-2.3) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 2.3) + ((ItemCost - 2.3) * Tax) / 100)))

        def Item22():
            ItemCost = 1.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 22", 1, 1.90))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-1.9)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-1.9) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.9) + ((ItemCost - 1.9) * Tax) / 100)))

        def Item23():
            ItemCost = 3.20
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 23", 1, 3.20))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-3.2)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-3.2) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 3.2) + ((ItemCost - 3.2) * Tax) / 100)))

        def Item24():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 24", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-1.1)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-1.1) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item25():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 25", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item26():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 26", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item27():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 27", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item28():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 28", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item29():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values=("Item 29", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2])
                SubTotal_Input.set(str('£%.2f' % (ItemCost - 1.1)))
                Tax_Input.set(str('£%.2f' % (((ItemCost - 1.1) * Tax) / 100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item30():
            ItemCost = 1.1
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 30", 1, 1.1))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-1.1)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-1.1) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.1) + ((ItemCost - 1.1) * Tax) / 100)))

        def Item31():
            ItemCost = 2.30
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 31", 1, 2.30))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-2.3)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-2.3) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 2.3) + ((ItemCost - 2.3) * Tax) / 100)))

        def Item32():
            ItemCost = 1.90
            Tax = 2.5
            self.POS_records.insert("", tk.END, values = ("Item 32", 1, 1.90))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item (child, "values") [2])
                SubTotal_Input.set(str('£%.2f'%(ItemCost-1.9)))
                Tax_Input.set(str('£%.2f'%(((ItemCost-1.9) *Tax) /100)))
                Total_Input.set(str('£%.2f' % ((ItemCost - 1.9) + ((ItemCost - 1.9) * Tax) / 100)))

        # =============================================================Treeview Widget========================================================================================#
        scroll_x = Scrollbar(ReceiptFrame, orient = HORIZONTAL)
        scroll_y = Scrollbar(ReceiptFrame, orient = VERTICAL)

        self.POS_records=ttk.Treeview(ReceiptFrame, height=25, columns= ("Item", "Qty", "Amount"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.POS_records.heading("Item", text="Item")
        self.POS_records.heading("Qty", text="Qty")
        self.POS_records.heading("Amount", text="Amount")

        self.POS_records ['show'] = 'headings'

        self.POS_records.column("Item", width=110)
        self.POS_records.column("Qty", width=80)
        self.POS_records.column("Amount", width=81)

        self.POS_records.pack(fill=BOTH, expand=1)
        self.POS_records.bind("<ButtonRelease-1>")

        # =============================================================Button Widget========================================================================================#
        self.btnItem1 = Button(ChangeButtonFrame, text=("Item1"), padx=2, width=15, height=8, bd=2, command= Item1)
        self.btnItem1.grid(row=0, column=0, pady=2, padx=4)

        self.btnItem2 = Button(ChangeButtonFrame, text=("Item2"), padx=2, width=15, height=8, bd=2, command=Item2)
        self.btnItem2.grid(row=0, column=1, pady=2, padx=4)

        self.btnItem3 = Button(ChangeButtonFrame, text=("Item3"), padx=2, width=15, height=8, bd=2, command=Item3)
        self.btnItem3.grid(row=1, column=0, pady=2, padx=4)

        self.btnItem4 = Button(ChangeButtonFrame, text=("Item4"), padx=2, width=15, height=8, bd=2, command=Item4)
        self.btnItem4.grid(row=1, column=1, pady=2, padx=4)

        self.btnItem5 = Button(ChangeButtonFrame, text=("Item5"), padx=2, width=15, height=8, bd=2, command=Item5)
        self.btnItem5.grid(row=2, column=0, pady=2, padx=4)

        self.btnItem6 = Button(ChangeButtonFrame, text=("Item6"), padx=2, width=15, height=8, bd=2, command=Item6)
        self.btnItem6.grid(row=2, column=1, pady=2, padx=4)

        self.btnItem7 = Button(ChangeButtonFrame, text=("Item7"), padx=2, width=15, height=8, bd=2, command=Item7)
        self.btnItem7.grid(row=3, column=0, pady=2, padx=4)

        self.btnItem8 = Button(ChangeButtonFrame, text=("Item8"), padx=2, width=15, height=8, bd=2, command=Item8)
        self.btnItem8.grid(row=3, column=1, pady=2, padx=4)
        # =============================================================Entry & Label Widget========================================================================================#
        self.btnItem9 = Button(FoodItemFrame, text=("Item9"), padx=2, width=15, height=8, bd=2, command=Item9)
        self.btnItem9.grid(row=0, column=0, pady=2, padx=4)

        self.btnItem10 = Button(FoodItemFrame, text=("Item10"), padx=2, width=15, height=8, bd=2, command=Item10)
        self.btnItem10.grid(row=0, column=1, pady=2, padx=4)

        self.btnItem11 = Button(FoodItemFrame, text=("Item11"), padx=2, width=15, height=8, bd=2, command=Item11)
        self.btnItem11.grid(row=0, column=2, pady=2, padx=4)

        self.btnItem12 = Button(FoodItemFrame, text=("Item12"), padx=2, width=15, height=8, bd=2, command=Item12)
        self.btnItem12.grid(row=0, column=3, pady=2, padx=4)

        self.btnItem13 = Button(FoodItemFrame, text=("Item13"), padx=2, width=15, height=8, bd=2, command=Item13)
        self.btnItem13.grid(row=0, column=4, pady=2, padx=4)

        self.btnItem14 = Button(FoodItemFrame, text=("Item14"), padx=2, width=15, height=8, bd=2, command=Item14)
        self.btnItem14.grid(row=0, column=5, pady=2, padx=4)
        # =============================================================Entry & Label Widget========================================================================================#
        self.btnItem15 = Button(FoodItemFrame, text=("Item15"), padx=2, width=15, height=8, bd=2, command=Item15)
        self.btnItem15.grid(row=1, column=0, pady=2, padx=4)

        self.btnItem16 = Button(FoodItemFrame, text=("Item16"), padx=2, width=15, height=8, bd=2, command=Item16)
        self.btnItem16.grid(row=1, column=1, pady=2, padx=4)

        self.btnItem17 = Button(FoodItemFrame, text=("Item17"), padx=2, width=15, height=8, bd=2, command=Item17)
        self.btnItem17.grid(row=1, column=2, pady=2, padx=4)

        self.btnItem18 = Button(FoodItemFrame, text=("Item18"), padx=2, width=15, height=8, bd=2, command=Item18)
        self.btnItem18.grid(row=1, column=3, pady=2, padx=4)

        self.btnItem19 = Button(FoodItemFrame, text=("Item19"), padx=2, width=15, height=8, bd=2, command=Item19)
        self.btnItem19.grid(row=1, column=4, pady=2, padx=4)

        self.btnItem20 = Button(FoodItemFrame, text=("Item20"), padx=2, width=15, height=8, bd=2, command=Item20)
        self.btnItem20.grid(row=1, column=5, pady=2, padx=4)
        # =============================================================Entry & Label Widget========================================================================================#
        self.btnItem21 = Button(FoodItemFrame, text=("Item21"), padx=2, width=15, height=8, bd=2, command=Item21)
        self.btnItem21.grid(row=2, column=0, pady=2, padx=4)

        self.btnItem22 = Button(FoodItemFrame, text=("Item22"), padx=2, width=15, height=8, bd=2, command=Item22)
        self.btnItem22.grid(row=2, column=1, pady=2, padx=4)

        self.btnItem23 = Button(FoodItemFrame, text=("Item23"), padx=2, width=15, height=8, bd=2, command=Item23)
        self.btnItem23.grid(row=2, column=2, pady=2, padx=4)

        self.btnItem24 = Button(FoodItemFrame, text=("Item24"), padx=2, width=15, height=8, bd=2, command=Item24)
        self.btnItem24.grid(row=2, column=3, pady=2, padx=4)

        self.btnItem25 = Button(FoodItemFrame, text=("Item25"), padx=2, width=15, height=8, bd=2, command=Item25)
        self.btnItem25.grid(row=2, column=4, pady=2, padx=4)

        self.btnItem26 = Button(FoodItemFrame, text=("Item26"), padx=2, width=15, height=8, bd=2, command=Item26)
        self.btnItem26.grid(row=2, column=5, pady=2, padx=4)
        # =============================================================Entry & Label Widget========================================================================================#
        self.btnItem27 = Button(FoodItemFrame, text=("Item27"), padx=2, width=15, height=8, bd=2, command=Item27)
        self.btnItem27.grid(row=3, column=0, pady=2, padx=4)

        self.btnItem28 = Button(FoodItemFrame, text=("Item28"), padx=2, width=15, height=8, bd=2, command=Item28)
        self.btnItem28.grid(row=3, column=1, pady=2, padx=4)

        self.btnItem29 = Button(FoodItemFrame, text=("Item29"), padx=2, width=15, height=8, bd=2, command=Item29)
        self.btnItem29.grid(row=3, column=2, pady=2, padx=4)

        self.btnItem30 = Button(FoodItemFrame, text=("Item30"), padx=2, width=15, height=8, bd=2, command=Item30)
        self.btnItem30.grid(row=3, column=3, pady=2, padx=4)

        self.btnItem31 = Button(FoodItemFrame, text=("Item31"), padx=2, width=15, height=8, bd=2, command=Item31)
        self.btnItem31.grid(row=3, column=4, pady=2, padx=4)

        self.btnItem32 = Button(FoodItemFrame, text=("Item32"), padx=2, width=15, height=8, bd=2, command=Item32)
        self.btnItem32.grid(row=3, column=5, pady=2, padx=4)


if __name__ == '__main__':
    root = Tk()
    application = POS(root)
    root.mainloop()





# auto adjust to the correct size when opening
# alignment of Main.Frame and alignment of all inner frames
# size of cash and change boxes ????
# look at a new colourway because 'cadetblue' is stinking
# add code for images. keep it simple so anybody without coding experience is able to change the photos
# need to clear receipt frame without deleting it
#         self.POS_records.column("Item", width=110) size irrelevant for clearing
#         self.POS_records.column("Qty", width=80) size irrelevant for clearing
#         self.POS_records.column("Amount", width=81) size irrelevant for clearing