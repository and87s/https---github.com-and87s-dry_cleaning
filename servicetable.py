from PyQt5.QtWidgets import QTableWidgetItem,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from dbtablewidget import dbTableWidget

class serviceTable(dbTableWidget):
    def __init__(self,cleaner,parent=None):
        header = [
            u'Клиент',
            u'Услуга',
            u'Количество',
            u'Цена',
            u'Сумма',
            u'Дата приема',
            u'Дата возврата'
        ]
        dbTableWidget.__init__(self,cleaner=cleaner,parent=parent,header=header)

    def setData(self):
        values = self.getCleaner().getServiceCodes()
        self.setRowCount(len(values))
        r=0
        for service in self.getCleaner().getServiceList():
            self.setItem(r,0,QTableWidgetItem(service.getClient().getDecription()))
            self.setItem(r,1,QTableWidgetItem(service.getKindService().getName()))
            self.setItem(r,2,QTableWidgetItem(str(service.getCount())))
            self.setItem(r,3,QTableWidgetItem(str(service.getPrice())))
            self.setItem(r,4,QTableWidgetItem(str(service.finalprice())))
            self.setItem(r,5,QTableWidgetItem(service.getDateReception().strftime("%d.%m.%Y") if service.getDateReception() else '' ))
            self.setItem(r,6,QTableWidgetItem(service.getDateReturn().strftime("%d.%m.%Y") if service.getDateReturn() else ''))
            self.appendRowCode(r,service.getCode())
            r+=1