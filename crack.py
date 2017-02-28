import sys
import win32com.client as win32
openedDoc = win32.gencache.EnsureDispatch('Word.Application')
filename= sys.argv[1]
dictionary_file = open ( 'dictionary.txt', 'r' )
passwords = dictionary_file.readlines()
dictionary_file.close()
passwords = [item.rstrip('\n') for item in passwords]
results = open('Password_result.txt', 'w')
password_found = 'false'
for password in passwords:
	if(password_found == 'false' ):
		print(password)
		try:
			wb = openedDoc.Documents.Open(filename, False, False, None, password)
			print("Password identified. Password is: "+password)
			results.write(password)
			results.close()
			password_found = 'true'
		except:
			print("Incorrect password")
			pass
	else:
		sys.exit(0)