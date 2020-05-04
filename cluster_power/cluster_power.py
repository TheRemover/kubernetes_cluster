#!/usr/bin/python3

import serial
import json

class Cluster:

  def __init__(self):
    self.nodes = None
    with open('nodes.json') as f:
      self.nodes = json.load(f)
    self.ser = serial.Serial('/dev/ttyACM0')
    self.ser.baudrate = 9600

  def power_off(self, type=None, name=None):
    for node in self.nodes:
      if (node['type']==type or node['node'] in name) or (type is None and name is None):
        self.ser(b"{} {}".format(node['relay'], 1))

  def power_on(self,type=None, name=None):
    for node in self.nodes:
      if node['type']==type or node['node']==name or (not type and not node):
        self.ser.write("{} {}".format(node['relay'], 0).encode())

  def get_state(self):
    for node in self.nodes:
      if GPIO.input(node['gpio']):
        print('{} - ON'.format(node['node']))
      else:
        print('{} - OFF'.format(node['node']))

def main():
  cluster = Cluster()
  cluster.power_off()
#  cluster.power_on(name="TK1C")
#  cluster.power_on(name="N1L")
#  cluster.power_on(name="N3R")
#  cluster.get_state()

if __name__ == "__main__":
    main()
