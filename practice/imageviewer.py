#circlelinkedlist를 활용하여 자동으로 넘어가는 imageviewr 생성

from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
import os
import threading
import sys

class Node:
    def __init__(self, item = None, link=None):
        self.item = item
        self.link = link

class circleLinkedlist:
    def __init__(self):
        self.root = Node()
        self.tail = self.root
        self.current = self.root

    def append(self, item):
        newNode = Node(item)
        if self.root.item == None:
            self.root = newNode
            self.tail = newNode
            newNode.link = self.root
            self.current = self.root
        else:
            tmp = self.tail.link
            self.tail.link = newNode
            newNode.link = tmp
            self.tail = newNode

    def print(self):
        curNode= self.root
        print("image list:  " + curNode.item, end=", ")
        while curNode.link != self.root:
            curNode= curNode.link
            print(curNode.item, end=", ")

    def listsize(self):
        listSize = 1
        curNode=self.root
        while curNode.link !=self.root:
            curNode=curNode.link
            listSize+=1
        return listSize

    def setCurrent(self, item):
        curNode = self.root
        for num in range(self.listsize()):
            if curNode.item !=item:
                curNode = curNode.link
            else:
                self.current = curNode
                break


    def moveNext(self):
        self.current = self.current.link
        return self.current.item

    def insert(self, item):
        newNode = Node(item)
        tmp1 = self.current.link
        self.current.link = newNode
        newNode.link = tmp1
        if self.current == self.tail:
            self.tail = newNode


    def delete(self, item):
        curNode = self.root
        if self.root.item == item:
            self.root = self.root.link
            self.tail.link = self.root
        else:
            while curNode.link != self.root:
                preNode = curNode
                curNode = curNode.link
                if curNode.item == item:
                    preNode.link = curNode.link
                    if curNode == self.tail:
                        self.tail = preNode

    def getCurrent(self):
        return self.current.item

class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Image Viewer")
        self.window.geometry("640x480")
        self.window.resizable(False, False)

        menubar = tk.Menu(self.window)
        menu_1 = tk.Menu(menubar, tearoff=0)
        menu_2 = tk.Menu(menubar, tearoff=0)
        menu_1.bind('<<MenuSelect>>')
        menu_2.bind('<<MenuSelect>>')

        menu_1.add_command(label="Open", command=self.directoryselect)
        menu_1.add_command(label="Close", command=self.close)
        menu_2.add_command(label="Next", command=self.next)
        menubar.add_cascade(label="Directory", menu=menu_1)
        menubar.add_cascade(label="Next image", menu=menu_2)
        self.window.config(menu=menubar)

        self.imgLabel = tk.Label(self.window, width=400, height=400, relief='solid')
        self.imgLabel.pack()
        self.window.mainloop()

    def close(self):
        sys.exit()

    def directoryselect(self):
        global imagelist
        imagelist = circleLinkedlist()
        jpgfiles = []
        path = filedialog.askdirectory(initialdir="C:/Users", title="Choose directory")
        for x in os.listdir(path):
            if x.endswith(".jpg"):
                jpgfiles.append(x)
        for filename in jpgfiles:
            imagelist.append(path + "/" + filename)
        imagelist.print()
        selFile=imagelist.getCurrent()
        self.fileSelect(selFile)

    def fileSelect(self, selFile):
        self.image = Image.open(selFile)
        if self.image.size[1] > self.image.size[0]:
            hSize = int((400 * self.image.size[0] / self.image.size[1]))
            vSize = 400
        else:
            hSize = 400
            vSize = int((400 * self.image.size[1] / self.image.size[0]))
        self.image = self.image.resize((hSize,vSize), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.imgLabel.config(image = self.image)

    def next(self):
        nextFile = imagelist.moveNext()
        self.fileSelect(nextFile)
        threading.Timer(2, self.next).start()                #사진을 직접 넘기고 싶은 경우 이 부분을 주석처리합니다.

a = Window()