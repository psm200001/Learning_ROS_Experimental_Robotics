#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from python_qt_binding.QtWidgets import QWidget, QVBoxLayout, QSlider
from python_qt_binding.QtCore import Qt
from rqt_gui_py.plugin import Plugin

class PanTiltWidget(QWidget):
    def __init__(self):
        super(PanTiltWidget, self).__init__()
        layout = QVBoxLayout()

        self.pan_slider = QSlider(Qt.Horizontal)
        self.pan_slider.setMinimum(-90)
        self.pan_slider.setMaximum(90)
        self.pan_slider.setValue(0)
        self.pan_slider.valueChanged.connect(self.update_pan)

        self.tilt_slider = QSlider(Qt.Horizontal)
        self.tilt_slider.setMinimum(-45)
        self.tilt_slider.setMaximum(45)
        self.tilt_slider.setValue(0)
        self.tilt_slider.valueChanged.connect(self.update_tilt)

        layout.addWidget(self.pan_slider)
        layout.addWidget(self.tilt_slider)
        self.setLayout(layout)

        self.pan_pub = rospy.Publisher('/pan_controller/command', Float64, queue_size=10)
        self.tilt_pub = rospy.Publisher('/tilt_controller/command', Float64, queue_size=10)

    def update_pan(self, value):
        self.pan_pub.publish(value * 3.14 / 180)

    def update_tilt(self, value):
        self.tilt_pub.publish(value * 3.14 / 180)

class PanTiltPlugin(Plugin):
    def __init__(self, context):
        super(PanTiltPlugin, self).__init__(context)
        self.setObjectName('PanTiltPlugin')
        self._widget = PanTiltWidget()
        context.add_widget(self._widget)
