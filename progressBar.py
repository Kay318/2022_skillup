import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QProgressBar, QMessageBox
from PyQt5.QtCore import QBasicTimer, QEventLoop, QTimer

class ProgressApp(QDialog):

    def __init__(self, time, new_set_difference, save_path, wb:object):
        super().__init__()
        self.difference = new_set_difference
        self.path = save_path
        self.wb = wb
        self.save_Bool = False

        loop = QEventLoop()
        QTimer.singleShot(1000, loop.quit)

        self.numberVar = time

        self.setWindowTitle('진행도')
        self.setFixedSize(230, 150)
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
    
        self.btn = QPushButton('Stop', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0
        self.show()
        self.timer.start(self.numberVar, self)
        loop.exec_()

    def timerEvent(self, e):
        if self.step == 99 and self.difference:
            self.timer.stop()

            idx = 1
            while(os.path.isfile(self.path)):
                self.path = str(os.path.dirname(self.path))
                self.path = f"{self.path}\\다국어평가결과({idx}).xlsx"
                idx = idx + 1
            else:
                self.wb.save(self.path)
                QApplication.processEvents()
                self.timer.start(self.numberVar, self)
            
        elif self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return 

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        elif self.btn.text() == "Finished":
            self.save_Bool = True
            self.close()
        else:
            reply = QMessageBox.question(self, '알림', '현재 엑셀 작업을 취소하시겠습니까?',
                                        QMessageBox.Ok | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                self.close()
            else:
                self.timer.start(self.numberVar, self)
                self.btn.setText('Stop')
        QApplication.processEvents()

    def closeEvent(self, a0) -> None:
        
        path = str(os.path.dirname(self.path))
        os.startfile(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProgressApp(time=500)
    ex.show()
    sys.exit(app.exec_())