from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QRadioButton,QCheckBox,QVBoxLayout,QHBoxLayout,QTextEdit,QLineEdit,QAction,QMenu,QMenuBar,QLabel,QProgressBar,qApp,QTextEdit
from PyQt5.QtGui import QPixmap,QIcon
import sys,os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import Image

mesaj = MIMEMultipart()
access = None

image1 = Image.open("gmail.png")
image1.crop((80,125,430,393)).save("gmail1.png")

image2 = Image.open("lockpage.png")
image2.crop((134,140,562,593)).save("locpage1.png")


class Login_Window(QWidget):
    def __init__(self,fromm=None):
        super().__init__()
        
        self.setStyleSheet("background-color: #3B3B3B;")
        self.setGeometry(1200,200,300,300)
        
        self.setWindowIcon(QIcon("simge.jpg"))

        self.setWindowTitle("Login Window")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()

        if fromm != None:
            self.line1.setText(fromm)

        self.warning = QLabel()
        self.warning.setStyleSheet("QLabel"
                      "{"
                      "color : red;"
                      "}")

        self.text1 = QLabel()
        self.text1.setText("Username:  ")
        self.text2 = QLabel()
        self.text2.setText("Password:  ")
        self.text3 = QLabel()

        self.button = QPushButton("Enter")

        image = QLabel()
        image.setPixmap(QPixmap("locpage1.png"))

        h_box = QHBoxLayout()        
        h_box.addStretch()
        h_box.addWidget(self.text1)
        h_box.addWidget(self.line1)
        h_box.addStretch()

        h_box1 = QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.text2)
        h_box1.addWidget(self.line2)
        h_box1.addStretch()

        h_box2 = QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(image)
        h_box2.addStretch()
        
        h_box3 = QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.button)
        h_box3.addWidget(self.warning)
        h_box3.addStretch()

        v_box = QVBoxLayout()
        
        v_box.addLayout(h_box2)
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box1)
        v_box.addStretch()
        v_box.addLayout(h_box3)
        v_box.addStretch()

        self.setLayout(v_box)
        self.button.clicked.connect(self.click)


    def click(self):
        global access
        if len(self.line1.text()) and len(self.line2.text()) != 0:
            try:
                mail = smtplib.SMTP("smtp.gmail.com",587)
                self.warning.setText("Checking...")     
                mail.starttls()
                mail.ehlo()
                mail.login(str(self.line1.text()),str(self.line2.text()))
                self.close()
                access = True
            except smtplib.SMTPAuthenticationError:
                self.warning.setText("The account not found, try again!")
                pass
        else:
            self.warning.setText("Please enter your password and username in these boxes.")


class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.init_ui()
    def init_ui(self):
        

        self.write1 = QLabel()
        self.write1.setText("Who will send the mail?")
        self.write2 = QLabel()
        self.write2.setText("Who will the mail be sent to?")
        self.write3 = QLabel()
        self.write3.setText("Title")
        self.write4 = QLabel()
        self.write4.setText("Write content")
        self.write5 = QLabel()
        self.write5.setText("")
        self.write6 = QLabel()
        self.write6.setText("")
        self.write7 = QLabel()
        self.write7.setText("")
        self.write8 = QLabel()
        self.write8.setText("")
        self.write_space = QLabel()
        self.write_space.setText("Not Sent")
        self.image1 = QLabel()
        self.image1.setPixmap(QPixmap("gmail1.png"))

        self.write1.setStyleSheet("color: #6F30EE;")
        self.write2.setStyleSheet("color: #6F30EE;")
        self.write3.setStyleSheet("color: #6F30EE;")
        self.write4.setStyleSheet("color: #6F30EE;")
        self.write_space.setStyleSheet("color: red;")

        self.progressbar = QProgressBar()

        self.progressbar.setGeometry(30, 40, 200, 25)



        self.button1 = QPushButton("Send")
        self.button2 = QPushButton("Login")
        self.button1.setStyleSheet("QPushButton"
                             "{"
                             "color : white;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "color : red;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : green;"
                             "}"
                             )
        self.button2.setStyleSheet("QPushButton"
                     "{"
                     "background-color : grey;"
                     "}"
                     "QPushButton::pressed"
                     "{"
                     "background-color : black;"
                     "}"
                     "QPushButton::hover"
                     "{"
                     "background-color : black;"
                     "}"
                     "QPushButton::hover"
                    "{"
                    "color : white;"
                    "}"
                     )
        

        self.R_button= QRadioButton()

        self.line1 = QLineEdit()
        self.line1.setStyleSheet("color: white;")
        self.line2 = QLineEdit() 
        self.line2.setStyleSheet("color: white;")
        self.line3 = QLineEdit() 
        self.line3.setStyleSheet("color: white;")
        self.line4 = QTextEdit()
        self.line4.setStyleSheet("color: white;")

        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        h_box3 = QHBoxLayout()
        h_box4 = QHBoxLayout()
        h_box5 = QHBoxLayout()
        h_box6 = QHBoxLayout()
        h_box7 = QHBoxLayout()

        h_box1.addStretch()
        h_box1.addWidget(self.write1)
        h_box1.addWidget(self.line1)
        h_box1.addWidget(self.write5)
        h_box1.addStretch()

        h_box2.addStretch()
        h_box2.addWidget(self.write2)
        h_box2.addWidget(self.line2)
        h_box2.addWidget(self.write6)
        h_box2.addStretch()
        
        
        h_box3.addStretch()
        h_box3.addWidget(self.write3)
        h_box3.addWidget(self.line3)
        h_box3.addWidget(self.write7)
        h_box3.addStretch()
        
        h_box4.addStretch()
        h_box4.addWidget(self.write4)
        h_box4.addWidget(self.line4)
        h_box4.addWidget(self.write8)
        h_box4.addStretch()
        
        h_box5.addStretch()
        h_box5.addWidget(self.write_space)
        h_box5.addWidget(self.progressbar)
        h_box5.addStretch()

        h_box6.addStretch()
        h_box6.addWidget(self.button2)
        h_box6.addWidget(self.button1)
        h_box6.addStretch()

        h_box7.addStretch()
        h_box7.addWidget(self.image1)
        h_box7.addStretch()

        h_box8 =QHBoxLayout()
        self.label1 = QLabel()
        self.r_button1 = QRadioButton("28")
        self.r_button1.setStyleSheet("color:white;")
        self.r_button2 = QRadioButton("465")
        self.r_button2.setStyleSheet("color:white;")
        self.r_button3 = QRadioButton("587")
        self.r_button3.setStyleSheet("color:white;")
        self.label1.setText("Port: ")
        self.label1.setStyleSheet("color:Blue;")

        h_box8.addStretch()
        h_box8.addWidget(self.label1)
        h_box8.addWidget(self.r_button1)
        h_box8.addWidget(self.r_button2)
        h_box8.addWidget(self.r_button3)
        h_box8.addStretch()

        v_box1 = QVBoxLayout()
        
        v_box1.addLayout(h_box7)
        v_box1.addStretch()
        v_box1.addLayout(h_box1)
        v_box1.addLayout(h_box2)
        v_box1.addLayout(h_box3)
        v_box1.addLayout(h_box4)
        v_box1.addLayout(h_box6)
        v_box1.addStretch()
        v_box1.addLayout(h_box8)
        v_box1.addStretch()
        v_box1.addLayout(h_box5)
        v_box1.addStretch()

        self.setLayout(v_box1)
        
        self.button2.clicked.connect(self.login)
        self.button1.clicked.connect(lambda : self.send_message(self.r_button1.isChecked(),self.r_button2.isChecked(),self.r_button3.isChecked()))
        
         
    def login(self):
        
        
        mesaj["From"] = self.line1.text()
        
        if self.w is None:
            self.w =  Login_Window(mesaj["From"])
        self.w.show()




    def send_message(self,sayi1,sayi2,sayi3):
        self.progressbar.setValue(0)
        if access == True and (sayi1 or sayi2 or sayi3) :
            try:                    
                if sayi1:
                    mail = smtplib.SMTP("smtp.gmail.com",28)
                elif sayi2:
                    mail = smtplib.SMTP("smtp.gmail.com",465)
                else:
                    mail = smtplib.SMTP("smtp.gmail.com",587)
                mesaj["To"] = self.line2.text()
                mesaj["subject"] = self.line3.text()
                self.yazi = self.line4.text()
                mesaj_govdesi = MIMEText(self.yazi,"plain")
                mesaj.attach(mesaj_govdesi)  
                
    
                    
                #quwhiahhykflxqrf
                #kerembkik@gmail.com
                mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
                self.progressbar.setValue(100)
                
                mail.close()

                self.write_space.setText("Email sent successfully")
            except:
                self.progressbar.setValue(0)
                self.write_space.setText("An error occurred, check your connect...")
        elif not(sayi1 or sayi2 or sayi3):
            self.write_space.setText("Please select one port.")
        else:
            self.write_space.setText("Please login first.")

class main_window(QMainWindow):
    def __init__(self): 
        
        super().__init__()

        self.setStyleSheet("background-color: black;")

        self.setGeometry(550,100,800,800)

        self.setWindowIcon(QIcon("gmail3.jpg"))

        self.widget = widget()

        self.setCentralWidget(self.widget)

        
        self.setWindowTitle("Mail Sender")

        self.show()

        menubar = self.menuBar()
        
        menubar.setStyleSheet("background-color: orange;")

        menu1 = menubar.addMenu("File")
        menu_1_1 = menu1.addMenu("Delete")
        action1 = QAction("Delete 1st line",self)
        action1.setShortcut("CTRl+1")
        action2 = QAction("Delete 2nd line",self)
        action2.setShortcut("CTRl+2")
        action3 = QAction("Delete 3rd line",self)
        action3.setShortcut("CTRl+3")
        action4 = QAction("Delete 4th line",self)
        action4.setShortcut("CTRl+4")
        action5 = QAction("Quit",self)
        action5.setShortcut("CTRL+Q")

        menu_1_1.addActions((action1,action2,action3,action4,action5))
    
        menu_1_1.triggered.connect(self.trigger)

    def trigger(self,action):
        if action.text() == "Delete 1st line":
            self.widget.line1.clear()
        elif action.text() == "Delete 2nd line":
            self.widget.line2.clear()
        elif action.text() == "Delete 3rd line":
            self.widget.line3.clear()
        elif action.text() == "Delete 4th line":
            self.widget.line4.clear()
        elif action.text() == "Quit":
            qApp.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ana_pencere1 = main_window()

    sys.exit(app.exec_())
