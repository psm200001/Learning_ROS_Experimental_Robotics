find_package(catkin REQUIRED COMPONENTS
  rqt_gui
  rqt_gui_py
  rospy
  std_msgs
)

catkin_package()

install(FILES
  plugin.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(PROGRAMS
  scripts/pan_tilt_rqt_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
