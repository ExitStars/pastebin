#-*- coding:utf-8-*-

from json import dumps, loads
from pyperclip import copy
from ttk import Treeview
from Tkinter import *
from os import system

class Panel():
    """Pastebin Codeshare GUI Code"""

    def __init__(self):
        try:
            self.jData = loads(open("json/ayar.json", "r").read())
        except:
            print "[!] Ayar Dosyasi Bulunamadı!"
            self.jData = [{"name": "CodeSH", "poster": "esw0rmer"}]

        try:
            self.lData = loads(open("json/pasteList.json", "r").read())
        except:
            print "[!] Ayar Dosyasi Bulunamadı!"
            self.lData = [{"kid": "none", "baslik": "none", "poster": "none", "tarih": "none"}]

    def savaFile(self):
        self.jData[0]["name"] = self.isim.get()
        self.jData[0]["poster"] = self.poster.get()

        file = open("json/ayar.json", "w")
        file.write(dumps(self.jData))
        file.close()

    def OnDoubleClick(self, event):
        item = self.treeview.selection()[0]
        kid = self.treeview.item(item,"text")
        link = "http://pastebin.yeg/code.php?kid="+str(kid)
        copy(link)
        system("clear")
        print "Copy To Dashboard!\n"+str(link)


    def panel(self):
        anapen = Tk()
        anapen.geometry("450x340")
        anapen.resizable(False, False)
        anapen.title("Codeshare Kod Paylasim Betigi")

        karsila = Label(text="Pastebin Codeshare Panel\nCODERLAB Bilişim Hizmetleri")
        karsila.place(x=125, y=10)

        altCizgi = Label(text="-"*111)
        altCizgi.place(x=0, y=40)

        isimLabel = Label(text="Varsayılan Program Adı: ")
        isimLabel.place(x=0, y=60)

        self.isim = Entry()
        self.isim.insert(END, str(self.jData[0]["name"]))
        self.isim.place(x=150, y=60)

        posterLabel = Label(text="Varsayılan Kullanıcı Adı: ")
        posterLabel.place(x=0, y=80)

        self.poster = Entry()
        self.poster.insert(END, str(self.jData[0]["poster"]))
        self.poster.place(x=150, y=80)

        kaydet = Button(text="Kaydet", command=self.savaFile)
        kaydet.place(x=325, y=75)

        """tv = ttk.Treeview(anapen, height =10,columns=('c0','c1','c2'))
        for i in range(1000):
            tv.insert('',i,values=('a'+str(i),'b'+str(i),'c'+str(i)))
        tv.pack()

        vbar = ttk.Scrollbar(anapen,orient=VERTICAL,command=tv.yview)
        tv.configure(yscrollcommand=vbar.set)
        tv.grid(row=0,column=0,sticky=NSEW)
        vbar.grid(row=0,column=1,sticky=NS)"""

        tv = Treeview(anapen)
        tv['columns'] = ('baslik', 'poster', 'tarih')
        tv.heading("#0", text='KID', anchor='w')
        tv.column("#0", anchor="w", width=100)
        tv.heading('baslik', text='Başlık')
        tv.column('baslik', anchor='sw', width=100)
        tv.heading('poster', text='Poster')
        tv.column('poster', anchor='sw', width=100)
        tv.heading('tarih', text='Tarih')
        tv.column('tarih', anchor='sw', width=150)
        tv.place(x=0, y=110)
        self.treeview = tv

        for data in list(reversed(self.lData)):
            self.treeview.insert('', 'end', text= data["kid"], values=(data["baslik"], data["poster"], data["tarih"]))

        self.treeview.bind("<Double-1>", self.OnDoubleClick)



        mainloop()
