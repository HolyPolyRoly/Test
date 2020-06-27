#!/usr/bin/python
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def main():
  indicator = appindicator.Indicator.new("customtray", "system-shutdown-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  gtk.main()

def menu():
  menu = gtk.Menu()
  
  #Performance Button
  perfbtn = gtk.MenuItem('Performance')
  perfbtn.connect('activate', perfcmd)
  menu.append(perfbtn)
  
  #Balanced Button
  balbtn = gtk.MenuItem('Balanced')
  balbtn.connect('activate', balcmd)
  menu.append(balbtn)
  
  #Battery Button
  batbtn = gtk.MenuItem('Battery')
  batbtn.connect('activate', batcmd)
  menu.append(batbtn) 
  menu.show_all()
  return menu
  
def perfcmd(_):
  os.system("system76-power profile performance")

def balcmd(_):
  os.system("system76-power profile performance")

def batcmd(_):
  os.system("system76-power profile battery")

def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()
