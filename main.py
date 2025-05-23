#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QListWidget, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QFileDialog
import os
from PIL import Image, ImageOps, ImageFilter
from PyQt5.QtGui import QPixmap
workdir = ''

class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.image = None
        self.dir = None
        self.save_dir = 'Modified/'
    def loadImage(self, filename):
        self.filename = filename
        self.dir = workdir
        image_path = os.path.join(self.dir, self.filename)
        self.image = Image.open(image_path)
    def showImage(self, path):
        pixmapimage = QPixmap(path)
        label_width, label_height = image.width(), image.height()
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.KeepAspectRatio)
        image.setPixmap(scaled_pixmap)
        image.setVisible(True)
    def save_image(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_bw(self):
        if file_list.selectedItems():
            self.image = ImageOps.grayscale(self.image)
            self.save_image()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Картинку выбери пожалуйста')
            error_win.exec()
    def do_sharpen(self):
        if file_list.selectedItems():
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.save_image()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Картинку выбери пожалуйста')
            error_win.exec()
    def do_rotate_left(self):
        if file_list.selectedItems():
            self.image = self.image.rotate(90)
            self.save_image()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Картинку выбери пожалуйста')
            error_win.exec()
    def do_rotate_right(self):
        if file_list.selectedItems():
            self.image = self.image.rotate(270)
            self.save_image()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Картинку выбери пожалуйста')
            error_win.exec()
    def do_mirror(self):
        if file_list.selectedItems():
            self.image = ImageOps.mirror(self.image)
            self.save_image()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Картинку выбери пожалуйста')
            error_win.exec()


workimage = ImageProcessor()

def showChosenImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, filename)
        workimage.showImage(image_path)

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = []
    for filname in files:
        for ext in extensions:
            if filname.endswith(ext):
                result.append(filname)
                break
    return result

def showFilenamesList():
    chooseWorkdir()
    extensions = ['.png', 'jpg', 'jpeg', 'gif', 'bmp']
    files = os.listdir(workdir)
    files = filter(files, extensions)
    file_list.clear()
    file_list.addItems(files)











app = QApplication([])
window = QWidget()
window.resize(700, 500)
window.setWindowTitle('Фоторедактор')

button = QPushButton('Папка')

file_list = QListWidget()

button2 = QPushButton('Лево')
button3 = QPushButton('Право')
button4 = QPushButton('Зеркало')
button5 = QPushButton('Резкость')
button6 = QPushButton('Ч/Б')

image = QLabel('Картинка')

v_line = QVBoxLayout()
v_line1 = QVBoxLayout()
h_line = QHBoxLayout()
h_line1 = QHBoxLayout()
v_line.addWidget(button)
v_line.addWidget(file_list)
h_line1.addWidget(button2)
h_line1.addWidget(button3)
h_line1.addWidget(button4)
h_line1.addWidget(button5)
h_line1.addWidget(button6)
h_line.addLayout(v_line)
h_line.addLayout(v_line1)
v_line1.addWidget(image)
v_line1.addLayout(h_line1)
window.setLayout(h_line)






button.clicked.connect(showFilenamesList)
file_list.currentRowChanged.connect(showChosenImage)
button2.clicked.connect(workimage.do_rotate_left)
button3.clicked.connect(workimage.do_rotate_right)
button4.clicked.connect(workimage.do_mirror)
button5.clicked.connect(workimage.do_sharpen)
button6.clicked.connect(workimage.do_bw)
window.show()
app.exec_()