Structure of GUI
============================================

This page summarises the code structure of a GUI (class).


.. code-block:: python

	class Ui_MainWindow(QtWidgets.QMainWindow):

inside you need to define the innit fuction::

	def __init__(self,n_db_loaded):
		# define window
		super(Ui_MainWindow,self).__init__()
		#define variables needed
		self.var_x=""
		#define closing window false
		self.finish_window=False

and ::
    
    	def closeEvent(self, event):
		#define close window
        	self.finish_window=True
        	self.close()

and the main fuction defining the window an its functions::
        
    	def setupUi(self):
		#define main characteristic window
       		self.setObjectName("MainWindow") #name
        	self.resize(558, 300) #size
        	self.centralwidget = QtWidgets.QWidget(self) #Widget
        	self.centralwidget.setObjectName("centralwidget")

		#Also define all the labels, buttons and others

		def retranslateUi(self):
			#define the name of the labals, buttons and others

		def example(self):
			#define what you want the window to do
			self.var_x="testing"
		


