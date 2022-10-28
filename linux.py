'''
==============================
NSSECU2 - Hacking Tool Project
==============================
Members: Escalona, Fadrigo, Fortiz, Manzano, Sy
Topic: WiFi Hacking Tool

linux.py module
'''

import utils.utils as utils
import scanning.interfaces.interfaces as interfaces
import time

def get_wifi_devices():
    interf = interfaces.get_interface()
    if interf == None:
        return None
    return interf

def run():
    utils.confirm(utils.running_OS())
    invalid = True
    while invalid:
        int_choices = ["1","2","3","4","5","0"]
        str_choices = [  "WiFi Scan", "WiFi Cracking","WAP Admin Attack",
                        "Full Suite (1-3 in order)", "WiFi DOS", "Exit"]
        utils.header("Tools Menu")
        choice = utils.menu(int_choices, str_choices)
        if utils.valid_choice(choice, int_choices):
            if choice == "0":
                exit(0)
            elif choice == "1":
                print("Test: " + str_choices[int(choice)-1])
            elif choice == "2":
                print("Test: " + str_choices[int(choice)-1])
            elif choice == "3":
                print("Test: " + str_choices[int(choice)-1])
            elif choice == "4":
                print("Test: " + str_choices[int(choice)-1])
            elif choice == "5":
                print("Test: " + str_choices[int(choice)-1])
            print("Wait for 1sec")
            time.sleep(1) 
    exit(0)