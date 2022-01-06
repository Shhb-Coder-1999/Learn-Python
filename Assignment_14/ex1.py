from math import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtUiTools import  QUiLoader
from functools import partial

class Calculator(QMainWindow):
  def __init__(self):
      super().__init__()
      self.input_num = None
      self.result = 0
      self.last_op = None
      loader = QUiLoader()
      self.ui = loader.load("cal_design.ui")
      self.ui.show()

      self.ui.num_1.clicked.connect(partial(self.init, '1' ,'num'))
      self.ui.num_2.clicked.connect(partial(self.init, '2' ,'num'))
      self.ui.num_3.clicked.connect(partial(self.init, '3' ,'num'))
      self.ui.num_4.clicked.connect(partial(self.init, '4' ,'num'))
      self.ui.num_5.clicked.connect(partial(self.init, '5' ,'num'))
      self.ui.num_6.clicked.connect(partial(self.init, '6' ,'num'))
      self.ui.num_7.clicked.connect(partial(self.init, '7' ,'num'))
      self.ui.num_8.clicked.connect(partial(self.init, '8' ,'num'))
      self.ui.num_9.clicked.connect(partial(self.init, '9' ,'num'))
      self.ui.num_0.clicked.connect(partial(self.init, '0' ,'num'))
      self.ui.dot_btn.clicked.connect(partial(self.init, '.' ,'num'))
      self.ui.sum_btn.clicked.connect(partial(self.init, None ,'sum'))
      self.ui.sub_btn.clicked.connect(partial(self.init, None ,'sub'))
      self.ui.div_btn.clicked.connect(partial(self.init, None ,'div'))
      self.ui.mul_btn.clicked.connect(partial(self.init, None ,'mul'))
      self.ui.res_btn.clicked.connect(partial(self.init, None ,'res'))
      self.ui.sin_btn.clicked.connect(partial(self.init, None ,'sin'))
      self.ui.cos_btn.clicked.connect(partial(self.init, None ,'cos'))
      self.ui.tan_btn.clicked.connect(partial(self.init, None ,'tan'))
      self.ui.cot_btn.clicked.connect(partial(self.init, None ,'cot'))
      self.ui.sqrt_btn.clicked.connect(partial(self.init, None ,'sqrt'))
      self.ui.log_btn.clicked.connect(partial(self.init, None ,'log'))
      self.ui.symmetry_btn.clicked.connect(partial(self.init, None ,'symmetry'))
      self.ui.clear_btn.clicked.connect(partial(self.init, None ,'clear'))
      

  def init(self , num , type):
      if(type == 'num'):
        if self.input_num == None :
            self.input_num = num
            self.ui.lcdNumber.display(self.input_num)
        else:
            if num == '.' and "." not in self.input_num:
                self.input_num += num
                self.ui.lcdNumber.display(self.input_num)  
            elif num != '.':
                self.input_num += num
                self.ui.lcdNumber.display(self.input_num) 


      elif  type == 'sum':
         if self.last_op != 'equal' and self.last_op != 'sin' and self.last_op != 'cos' and self.last_op != 'tan' and self.last_op != 'cot' and self.last_op != 'log' and self.last_op != 'sqrt' and self.last_op != 'symmetry'  :
           self.sum()
         else :
                self.ui.lcdNumber.display("0") 
                self.input_num = None
                self.last_op = 'sum'     

      elif  type == 'sub' :
         if self.last_op != 'equal' and self.last_op != 'sin' and self.last_op != 'cos' and self.last_op != 'tan' and self.last_op != 'cot' and self.last_op != 'log' and self.last_op != 'sqrt' and self.last_op != 'symmetry' :
            self.sub()
         else :
                self.ui.lcdNumber.display("0") 
                self.input_num = None
                self.last_op = 'sub'   

      elif  type == 'mul' :
          if self.last_op != 'equal' and self.last_op != 'sin' and self.last_op != 'cos' and self.last_op != 'tan' and self.last_op != 'cot' and self.last_op != 'log' and self.last_op != 'sqrt' and self.last_op != 'symmetry' :
             self.mul()
          else :
                self.ui.lcdNumber.display("0") 
                self.input_num = None
                self.last_op = 'mul' 

      elif  type == 'div' :
          if self.last_op != 'equal' and self.last_op != 'sin' and self.last_op != 'cos' and self.last_op != 'tan' and self.last_op != 'cot' and self.last_op != 'log' and self.last_op != 'sqrt' and self.last_op != 'symmetry' :
             self.div()
          else :
                self.ui.lcdNumber.display("0") 
                self.input_num = None
                self.last_op = 'div' 

      elif  type == 'sin':
                self.sin()
                self.input_num = None
                self.last_op = 'sin' 

      elif  type == 'cos':
             self.cos()
             self.input_num = None
             self.last_op = 'sin' 

      elif  type == 'tan':

             self.tan()
             self.input_num = None
             self.last_op = 'tan'  

      elif  type == 'cot':
                self.cot()
                self.input_num = None
                self.last_op = 'cot'  

      elif  type == 'sqrt':
                self.sqrt()
                self.input_num = None
                self.last_op = 'sqrt'  

      elif  type == 'log':
                self.log()
                self.input_num = None
                self.last_op = 'log'        

      elif  type == 'symmetry':
                self.symmetry()
                self.last_op = 'symmetry'  

      elif  type == 'clear':
                self.clear()
                self.last_op = 'clear'                                     
                

      elif  type == 'res':
          self.equal()    
          self.ui.lcdNumber.display(self.result) 


  def sum(self):
       if self.result !=0:
        self.result = self.result + float(self.input_num)
       else :
        self.result = float(self.input_num)
       
       self.ui.lcdNumber.display("0") 
       self.input_num = None
       self.last_op = 'sum'

  def sub(self):
       if self.result !=0:
        self.result = self.result - float(self.input_num)
       else :
        self.result = float(self.input_num)
       
       self.ui.lcdNumber.display("0") 
       self.input_num = None
       self.last_op = 'sub'

  def mul(self):
       if self.result !=0 :
        self.result = self.result * float(self.input_num)
       else :
          self.result = float(self.input_num)
       self.ui.lcdNumber.display("0") 
       self.input_num = None
       self.last_op = 'mul'

  def div(self):
       if self.result !=0:
        self.result = self.result / float(self.input_num)
       else :
        self.result = float(self.input_num)
       
       self.ui.lcdNumber.display("0") 
       self.input_num = None
       self.last_op = 'div'

  def sin(self):
       if self.result == 0:
         self.result = sin(radians(float(self.input_num)))
       elif self.result != 0:
         self.result = sin(radians(float(self.result)))

       self.ui.lcdNumber.display(self.result) 
       self.input_num = None
       self.last_op = 'sin'

  def cos(self):
       if self.result == 0:
         self.result =  cos(radians(float(self.input_num)))
       elif self.result != 0:
         self.result = cos(radians(float(self.result)))

       self.ui.lcdNumber.display(self.result) 
       self.input_num = None
       self.last_op = 'cos'   

  def tan(self):
       if self.result == 0:
         self.result = tan(radians(float(self.input_num)))
       elif self.result != 0:
         self.result = tan(radians(float(self.result)))       

       self.ui.lcdNumber.display(self.result) 
       self.input_num = None
       self.last_op = 'tan'

  def cot(self):
       if self.result == 0:
         self.result = 1/tan(radians(float(self.input_num)))
       elif self.result != 0:
         self.result = 1/tan(radians(float(self.result)))      


       self.ui.lcdNumber.display(self.result) 
       self.input_num = None
       self.last_op = 'cot' 

  def log(self):
       if self.result == 0:
         self.result =log(float(self.input_num) , 10)
       elif self.result != 0:
         self.result = log(float(self.result)  , 10)        

       self.ui.lcdNumber.display(self.result) 
       self.input_num = None
       self.last_op = 'log'  

  def sqrt(self):
       if self.result == 0:
         self.result =sqrt(float(self.input_num))
       elif self.result != 0:
         self.result = sqrt(float(self.result)) 

       self.ui.lcdNumber.display(self.result) 
       self.input_num = None
       self.last_op = 'sqrt' 

  def symmetry(self):
       if self.result == 0:
          self.result = self.input_num       
      

       print("------------------")
       if  '-' in str(self.result):
            self.result = float(str(self.result)[1:])
            self.ui.lcdNumber.display(self.result) 
            self.last_op = 'symmetry' 
       else: 
           self.result =float("-" + self.input_num)
           self.ui.lcdNumber.display(self.result)
           self.last_op = 'symmetry' 

  def clear(self):
       self.input_num = None
       self.result = 0
       self.ui.lcdNumber.display(self.result) 
       self.last_op = 'symmetry' 



  def equal(self):
      if self.last_op == 'sum':
       self.result = self.result + float(self.input_num)
       self.last_op = 'equal'
      elif self.last_op == 'sub':
       self.result = self.result - (float(self.input_num))
       self.last_op = 'equal'
      elif self.last_op == 'mul':
       self.result = self.result * float(self.input_num) 
       self.last_op = 'equal'
      elif self.last_op == 'div':
       self.result = self.result / float(self.input_num) 
       self.last_op = 'equal'     
         



my_app = QApplication()
calculator = Calculator()
calculator.setFixedSize(200 , 300)
my_app.exec()
