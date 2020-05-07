import serial
import json
import time

class Cluster:

  def __init__(self, node_list='nodes.json', serial_port='/dev/ttyACM0', baud_rate=9600):
    self.nodes = None
    with open(node_list) as f:
      self.nodes = json.load(f)
    self.ser = serial.Serial(serial_port)
    self.ser.baudrate = baud_rate

  def power_off(self, type=None, name=None):
    for node in self.nodes:
      print(node)
      if type is None and name is None:
        self.ser.write("{} {}".format(node['relay'], 1).encode())
      elif type is not None:
        if node['type']==type:
          print("{} {}".format(node['node'],node['relay']))
          time.sleep(10)
          self.ser.write("{} {}".format(node['relay'], 1).encode())
      elif name is not None:
        if node['node'] in name:
          print("{} {}".format(node['node'],node['relay']))
          time.sleep(10)
          self.ser.write("{} {}".format(node['relay'], 1).encode())

  def power_on(self,type=None, name=None):
    print(name)
    for node in self.nodes:
      if type is None and name is None:
        self.ser.write("{} {}".format(node['relay'], 0).encode())
      elif type is not None:
        if node['type']==type:
          print("{} {}".format(node['node'],node['relay']))
          time.sleep(10)
          self.ser.write("{} {}".format(node['relay'], 0).encode())
      elif name is not None:
        if node['node'] in name:
          print("{} {}".format(node['node'],node['relay']))
          time.sleep(10)
          self.ser.write("{} {}".format(node['relay'], 0).encode())

  def get_state(self):
    for node in self.nodes:
      if GPIO.input(node['gpio']):
        print('{} - ON'.format(node['node']))
      else:
        print('{} - OFF'.format(node['node']))
