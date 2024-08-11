import sys
from PyQt5.QtCore import Qt, QTimer, QRect ,QRectF
from PyQt5.QtGui import QPainter, QColor ,QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication


class MusicVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(33)  # Update every 100 milliseconds

        self.rect_heights = [10 ,10 ,10 ,10 ,10 ,10]  # Initial heights of the rectangles
        self.max_heights = [21 ,25 ,30 ,20 ,24 ,29]
        self.direction = [1, 1, 1, 1, 1  ,1]  # Direction of movement for each rectangle

        self.setGeometry(350, 350, 200, 35)
        self.setWindowTitle('Music Visualizer')
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)

        rect_width = 15
        gap = 8
        radius = 6

        for i in range(len(self.rect_heights)):
            x = i * (rect_width + gap) + 20
            y = self.height() - self.rect_heights[i]
            rect = QRectF(x, y, rect_width, self.rect_heights[i])
            
            path = QPainterPath()
            path.moveTo(x, y + radius)
            path.arcTo(QRectF(x, y, radius * 2, radius * 2), 180, -90)  # Top-left corner
            path.lineTo(x + rect_width - radius, y)
            path.arcTo(QRectF(x + rect_width - radius * 2, y, radius * 2, radius * 2), 90, -90)  # Top-right corner
            path.lineTo(x + rect_width, y + self.rect_heights[i])
            path.lineTo(x, y + self.rect_heights[i])
            path.closeSubpath()
            
            painter.setBrush(QColor(173, 110, 224))  # Black color for the rectangles
            painter.drawPath(path)
        self.update_rect_heights()

    def update_rect_heights(self):
        for i in range(len(self.rect_heights)):
            self.rect_heights[i] += 5 * self.direction[i]
            if self.rect_heights[i] > self.max_heights[i] or self.rect_heights[i] < 5:
                self.direction[i] *= -1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MusicVisualizer()
    sys.exit(app.exec_())
