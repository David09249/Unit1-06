# Created by: David Wang
# Created on: 28-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit1-06
# This program shows the difference between local and global variables 

import ui

variableX = 25

def local_button_touch_up_inside(sender):
    
    variableX = 10
    variableY = 30
    variableZ = variableX + variableY
    
    view['local_answer_label'].text = str(variableZ)
        
def global_button_touch_up_inside(sender):
    
    variableY = 30
    variableZ = variableX + variableY
    
    view['global_answer_label'].text = str(variableZ)

view = ui.load_view()
view.present('full_screen')
