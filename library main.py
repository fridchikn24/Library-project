#Library project
#Look up borrower's dvds and books checked out
#See if any overdue
#Bar any borrowing if overdue and total late fees
#Make new customer if not in the base
#How to do book/dvd names?

	
class Borrower(object):
	name = "String"
	books = []
	dvds = []
	due_dates = []#books first then dvds

shelf = {
	"The Best in the World(at what I have no idea)": "Chris Jericho": 3,
	"For Whom the Bells Toll":"Ernest Hemmingway": 2,
	"The Sun Also Rises": "Ernest Hemmingway": 1,
	"The Origin of Species": "Charles Darwin": 1,
	"The Republic": "Plato": 2
}


def library(lib):
	consumers = [Borrower]
	print "Welcome to the Library. Are you her to borrow, return, or donate? /n"
	answer = raw_input
	if answer == "Borrow":
		processBorrow(consumers)
	if answer == "Return":
		processReturn(consumers)
	if answer == "Donate":
		processDonate()
	else:
		print "I'm sorry, could you say that again? /n"

def processBorrow():
	print "What would you like to borrow? /n"
	book = raw_input
	if book in shelf:
		checkquantity(book)
		if True:
			checkfees(consumers)
			if False:
				#dock a book from the shelf
				return
			else: 
				print "You have some outstanding fines, please pay these fines or return the items you borrowed /n"
				return
	else:
		print "We're sorry, that book is not currently in stock /n" 
		print "Would you like to look for another book?(Y/N) /n"	
		if raw_input = "Y":
			processBorrow()
			return
		else:
			return

def processReturn():
	print "What would you like to return? /n"
	book = raw_input
	#put book back in shelf
	if checkfees(consumers) is True:
		#remove fees
	else: return

def processDonate():
