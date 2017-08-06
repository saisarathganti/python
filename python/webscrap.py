#webscaper - it searches the result of entered keyword and displays it in terminal

import requests , pyperclip , bs4 , sys

#through request it is possible to get the entire code of the search page to the local terminal

#beautiful soup actually used to acess the data or code brought through request

if(len(sys.argv)>1):

	word = ' '.join(sys.argv[1:])
#takes the commandline argument and convert it to string

else:

	word = pyperclip.paste()

#brings the entire code of the  link to the local repository
 
r = requests.get('https://www.google.co.in/search?site=&source=hp&q=' + word)

soup = bs4.BeautifulSoup(r.text, "lxml")

#beautiful soup is used above which pulls the daa of the html file 

qp = (soup.findAll("div" , {"id" : "center_col"})) 

#the above code searches the div element with id center-col

#the below loop basically print the all the links of the search results

for div  in qp:

	link = div.findAll('a')

	for x in link:

		print x['href']



