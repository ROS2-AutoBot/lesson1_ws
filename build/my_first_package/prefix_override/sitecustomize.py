import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vudinhso/RMIT_Bot/lesson1_ws/install/my_first_package'
