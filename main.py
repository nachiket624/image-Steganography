from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from mainwindow import Ui_MainWindow
import sys
from PySide6.QtGui import QPixmap
from program_utility.imageencode import ImgEncode
from program_utility.imagedecode import ImgDecode
from program_utility.imgimgencode import imgImgencode
from program_utility.imgimgdecode import imgImgDecode
from program_utility.exeencode import encodeExe
from program_utility.exedecode import decodeExe

imgexe = []
decodeimgexe = []
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.w = None
        self.w1 = None
        self.setupUi(self)
        self.Options.itemClicked.connect(self.onItemClicked)
        self.open_encode_img.clicked.connect(self.showOpenFileDialogEncode)
        self.img_decode_open.clicked.connect(self.imgDecode)
        self.primary_img.clicked.connect(self.getPrimaryImage)
        self.seconday_img.clicked.connect(self.getSecondayImage)
        self.open_encode_img_2.clicked.connect(self.openMergeImage)
        self.img_img_export.clicked.connect(self.getImages)
        self.pushButton.clicked.connect(self.cleandata)
        self.uploadexe_btn.clicked.connect(self.uploadexe)
        self.uploadexe_btn.clicked.connect(self.uploadimag)
        self.processimgexe.clicked.connect(self.filepaths)
        self.decodeexe_btn.clicked.connect(self.decodeexe)
        self.processdecodeexe.clicked.connect(self.decodeImgExe)


    def onItemClicked(self):
        item = self.Options.currentItem()
        item = (item.text(0))
        self.changepage(item)

    def changepage(self,page):
        """This function change the stackwigest page """
        if page == "Image Encode":
            self.stackedWidget.setCurrentWidget(self.page_0)
        if page == "Image to Image Encode":
            self.stackedWidget.setCurrentWidget(self.page_1)
        if page == "Image exe Encode":
            self.stackedWidget.setCurrentWidget(self.page_2)


    def showOpenFileDialogEncode(self):
        options = QFileDialog.Options()
        image_file, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                    "Images (*.png *.jpg *.jpeg *.bmp *.gif *.tiff);;All Files (*)",
                                                    options=options)
        if image_file:
            pixmap = QPixmap(image_file)
            if not pixmap.isNull():
                self.img_enode_holder.setPixmap(pixmap)
                text = self.path_encode_img.text()
                print("text is ", text)
                self.pushButton.clicked.connect(ImgEncode(image_file, text))
            else:
                self.img_enode_holder.setText("Invalid Image File")
    def imgDecode(self):
        file = self.showOpenFile()
    def showOpenFile(self):
        options = QFileDialog.Options()
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setViewMode(QFileDialog.List)
        selected_file, _ = file_dialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)",
                                                       options=options)
        if selected_file:
            pixmap = QPixmap(selected_file)
            if not pixmap.isNull():
                self.img_decode_holder.setPixmap(pixmap)
                self.decode_img_text.setText(str(ImgDecode(selected_file)))

    def cleandata(self):
        self.img_enode_holder.clear()

# ##########################################################################
#                       Encode Image Inside Image
# ##########################################################################

    def openimage(self):
        options = QFileDialog.Options()
        image_file, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                    "Images (*.png *.jpg *.jpeg *.bmp *.gif *.tiff);;All Files (*)", options=options)

        return image_file

    def showSaveFileDialog(self):
        options = QFileDialog.Options()
        file_dialog = QFileDialog()
        selected_file, _ = file_dialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)",
                                                       options=options)

        if selected_file:
            text_to_save = self.text_edit.toPlainText()
            with open(selected_file, 'w') as file:
                file.write(text_to_save)
            print(f"File saved to: {selected_file}")


    def getImages(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a question dialog")

        imgImgencode(primaryImg,secondry)


    def getPrimaryImage(self):
        global primaryImg
        primaryImg = self.openimage()
        if primaryImg:
            pixmap = QPixmap(primaryImg)
            if not pixmap.isNull():
                self.img_img_primary.setPixmap(pixmap)


    def getSecondayImage(self):
        global secondry
        secondry = self.openimage()
        if secondry:
            pixmap = QPixmap(secondry)
            if not pixmap.isNull():
                self.img_img_secondary.setPixmap(pixmap)


# ##########################################################################
#                       Decode Image Inside Image
# ##########################################################################

    def openMergeImage(self):
        # todo: 1) open merge image 2) decode and display
        image_path1 = self.openimage()
        imgImgDecode(image_path1)
        hiddinimg = "/home/laptop420/PycharmProjects/steg/new_image.png"
        if hiddinimg:
            pixmap = QPixmap(hiddinimg)
            if not pixmap.isNull():
                self.img_img_decode.setPixmap(pixmap)


# ##########################################################################
#                       Encode Image executable
# ##########################################################################
    def file_path_for_exe(self,type):
        options = QFileDialog.Options()
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setViewMode(QFileDialog.List)
        image_file, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                    type,
                                                    options=options)

        return image_file

    def uploadexe(self):
        uploadexe = (self.file_path_for_exe('Executable Files (*.exe);;All Files (*)'))
        self.uploadexe_line.setText(str(uploadexe))
        imgexe.append(uploadexe)


    def uploadimag(self):
        uploadeimg = (self.file_path_for_exe('Images (*.jpg *.jpeg );;All Files (*)'))
        self.uploadimage_line.setText(str(uploadeimg))
        imgexe.append(uploadeimg)

    # def meargeexe(self):
    #     self.uploadexe_btn.clicked.connect(self.uploadexe)
    #     self.uploadexe_btn.clicked.connect(self.uploadimag)

    def filepaths(self):
        # print(imgexe)
        exefile = imgexe[0]
        imgfile = imgexe[1]
        print("exefile {} image file {}",exefile,imgfile)
        encodeExe(imgfile,exefile)

# ##########################################################################
#                       Decode Image executable
# ##########################################################################

    def decodeexe(self):
        uploadexe = (self.file_path_for_exe('Images (*.jpg *.jpeg );;All Files (*)'))
        print("Decode image path ",uploadexe)
        self.decodeexex_line.setText(uploadexe)
    def decodeImgExe(self):
        img = self.decodeexex_line.text()
        print("image path is ",img)
        decodeExe(img)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()