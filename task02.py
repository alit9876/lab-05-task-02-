import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow


class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        loadUi('final_scroll.ui', self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.submit_button.clicked.connect(self.Add_data)
        self.reset_data()

    def reset_data(self):
        self.District_Box.setCurrentIndex(0)
        self.tehsil_box.setCurrentIndex(0)
        self.deed_number.setCurrentIndex(0)
        self.stamp_paper.setCurrentIndex(0)
        self.Agent_name.setText('Enter Agent Name')
        self.Agent_Contact.setText('Enter Agent Contact Number')
        self.Agent_CNIC.setText('Enter Agent CNIC')
        self.Agent_Email.setText('Enter Agent Email')
        self.party_name.setText('Enter 1st Party Name')
        self.party_Contact.setText('Enter 1st Party Contact')
        self.party_CNIC.setText('Enter 1st Party CNIC')
        self.party_EMAIL.setText('Enter 1st Party Email')

    def Add_data(self):
        district = self.District_Box.currentText()
        tehsil = self.tehsil_box.currentText()
        ded_number = self.deed_number.currentText()
        stamp_paper_type = self.stamp_paper.currentText()
        agn_name = self.Agent_name.text()
        agn_contact = self.Agent_Contact.text()
        agn_cnic = self.Agent_CNIC.text()
        agn_email = self.Agent_Email.text()
        f_party_name = self.party_name.text()
        f_party_contact = self.party_Contact.text()
        f_party_CNIC = self.party_CNIC.text()
        f_party_Email = self.party_EMAIL.text()
        #
        data = {
            'District': [district],
            'Tehsil': [tehsil],
            'Stamp Paper type': [stamp_paper_type],
            'Deed Number': [ded_number],
            'Agent Name': [agn_name],
            'Agent Contact': [agn_contact],
            'Agent CNIC': [agn_cnic],
            'Agnet Email': [agn_email],
            '1st Agent Name': [f_party_name],
            '1st Agent Contact': [f_party_contact],
            '1st Agent CNIC': [f_party_CNIC],
            '1st Agent Email': [f_party_Email]
        }
        df = pd.DataFrame(data)
        df.to_csv('data.csv', mode='a', header=True, index=False, encoding='utf-8')
        self.reset_data()
        print('Data have been stored')


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())
