import json
import time
import requests

class ClusterPower:

  def setPin(self,pin, value):
    if not pin:
      print("No pin specified");
      return -1
    if not value:
      print ("No value specified");
      return -1
    if self.debug:
          print("Setting pin {} to {}".format(pin,value))
    result = requests.get("http://{}/digital/{}/{}".format(self.controller, pin, value))
    if result.status_code != 200:
      print("Unable to reach controller {}".format(self.controller))
      return -1
    else:
      return

  def __init__(self, node_list='nodes.json', controller='172.16.0.2', debug=False):
    self.nodes = None
    with open(node_list) as f:
      self.nodes = json.load(f)
    self.controller=controller
    self.debug = debug

  def power_off(self, type=None, name=None):
    if self.debug:
      print("Type: {}, Name: {}".format(type, name))
    for node in self.nodes:
      if self.debug:
        print("Node: {}".format(node.get('node')))
      if type is None and name is None:
        self.setPin(node.get('gpio'), '0')
      elif type is not None:
        if node['type']==type:
          self.setPin(node.get('gpio'), '0')
      elif name is not None:
        if node['node'] in name:
          self.setPin(node.get('gpio'), '0')

  def power_on(self,type=None, name=None):
    if self.debug:
      print("Type: {}, Name: {}".format(type, name))
    for node in self.nodes:
      if self.debug:
        print("Node: {}".format(node.get('node')))
      if type is None and name is None:
        self.setPin(node.get('gpio'), '1')
      elif type is not None:
        if node['type']==type:
          self.setPin(node.get('gpio'), '1')
      elif name is not None:
        if node['node'] in name:
          self.setPin(node.get('gpio'), '1')

  def getPin(self,pin):
    if not pin:
      print("No pin specified");
      return -1
    if self.debug:
      print("Getting pin {} status".format(pin))
    result = requests.get("http://{}/digital/{}".format(self.controller, pin))
    if result.status_code != 200:
      print("Unable to reach controller {}".format(self.controller))
      return -1
    else:
      value = result.json()
      if self.debug:
        print("Pin {} is {}".format(pin,value.get("return_value")))
      return value.get("return_value")

  def status(self,type=None, name=None):
    if self.debug:
      print("Type: {}, Name: {}".format(type, name))
    for node in self.nodes:
      if self.debug:
        print("Node: {}".format(node.get('node')))
      if type is None and name is None:
        result = self.getPin(node.get('gpio'))
        print("Node: {} Status: {}".format(node.get('node'),result))
      elif type is not None:
        if node['type']==type:
          result = self.getPin(node.get('gpio'))
          print("Node: {} Status: {}".format(node.get('node'),result))
      elif name is not None:
        if node['node'] in name:
          result = self.getPin(node.get('gpio'))
          print("Node: {} Status: {}".format(node.get('node'),result))

  def hard_cycle(self,type=None, name=None):
    self.power_off(type=type,name=name)
    self.power_on(type=type,name=name)

#  def node_reset(self,os_name,type=None, name=None)
#     for node in self.nodes:
#      if type is None and name is None:
#        self.ser.write("{} {}".format(node['relay'], 1).encode())
#        hex_ip = ip_to_hex(node['ip']
#        os.symlink("{}/{}".format(self.tftp_dir,os_name),"{}/{}".format(self.tftp_dir,hex_ip)
#        time.sleep(1)
#      elif type is not None:
#        if node['type']==type:
#          self.ser.write("{} {}".format(node['relay'], 1).encode())
#          time.sleep(1)
#      elif name is not None:
#        if node['node'] in name:
#          self.ser.write("{} {}".format(node['relay'], 1).encode())
#          time.sleep(1)

  #def get_state(self):
    #for node in self.nodes:
      #if GPIO.input(node['gpio']):
        #print('{} - ON'.format(node['node']))
      #else:
        #print('{} - OFF'.format(node['node']))
