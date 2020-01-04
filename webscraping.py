import webbrowser
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
def amazon_mode():
	print("\nWelcome to Amazon Coupon");
	print("This program will list coupons currently on Amazon with Most Savings")
	print("\nConnecting to Amazon...")
	my_url = 'https://www.amazon.ca/b?node=12218500011'
	uClient = uReq(my_url)
	print("Reading Items...")
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html,"html5lib")
	section_a = page_soup.findAll("div",{"class":"a-box-inner"})
	savings = {}
	for i in range(len(section_a)):
		try:
			cost = section_a[i].find("div",{"class":"a-section coupon-item-title"}).span.text.strip().replace('Save $','')
			name_list = section_a[i].find("div",{"class":"a-section coupon-title"}).text.strip().split(' on ')
			name = name_list[1]
			savings[name] = cost
		except IndexError:
			name = name_list[0]
			cost = section_a[i].find("div",{"class":"a-section coupon-item-title"}).span.text.strip().replace('Save $','')
			savings[name] = cost
		except AttributeError:
			pass

	key = list(savings.keys())
	final_ranking = [key[0]]
	for i in range(0,len(key)):
		inserted = False
		test_name = key[i]
		for j in range(len(final_ranking)):	
			if (int(savings[test_name]) >= int(savings[final_ranking[j]])):
				final_ranking.insert(j,test_name)
				inserted = True
				break
			elif j == len(final_ranking)-1 and inserted == False:
				final_ranking.insert(j,test_name)

	print('           Items','                          |                            ','Savings ($)')
	for p in range(0,len(final_ranking)-1): 
		item_name = final_ranking[p].ljust(70,'.')
		print(' {0:<3.0f}. {1:<70}'.format(p+1,item_name), end='')
		print('${0:<02.2f}'.format(float(savings[final_ranking[p]])))

	go_to_webpage = input("\nDo You Wish to go to Amazon Coupons Webpage? [y/n]").lower()
	if (go_to_webpage == 'y'):
		webbrowser.open('https://www.amazon.ca/b?node=12218500011')

def netflix_mode():
	print("\nWelcome to Netflix Movie Ranker")
	print("note: this is will take ~1 minute to run")
	print("Select a Category to Rank:")
	my_url = 'https://www.netflix.com/ca/browse/genre/34399'
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html,"html.parser")
	category_dict = {}
	list_num = 0

	container = page_soup.find("div",{"class":"nm-collections-container"})
	categories = container.findAll("section",{"class":"nm-collections-row"})
	# find all the categories
	for cat_names in categories:
		# finds the category name
		try:
			category_dict[list_num] = cat_names.h1.a.span.text.strip()
			print('({0:^4.0f}) {1:<}'.format(list_num,category_dict[list_num])); 
			list_num+=1
		except AttributeError:
			# use a different path
			category_dict[list_num] = cat_names.h1.text.strip()
			print('({0:^4.0f}) {1:<}'.format(list_num,category_dict[list_num])); 
			list_num+=1
	try:
		category_input = int(input("  "))
		if (str(category_input).isnumeric() == False):
			raise
		print("\nRanking: ", end='')
		print(category_dict[category_input],end='\n\n')
	except:
		while (category_input <0 ) or (category_input >len(categories)) or (str(category_input).isnumeric()==False):
			print("Input Error")
			try:
				category_input = int(input("Enter Valid Input: "))
			except: print("Not a Number");


	# now rank that category
	rank_category_html = categories[category_input]
	movies = rank_category_html.div.ul.findAll("span",{"class":"nm-collections-title-name"})
	# grab ratings from google:
	movie_rankings = {}
	for category_movies in movies:
		try:
			normal_title = category_movies.text.strip()
			title = '+'.join(category_movies.text.strip().split(' '))
			google_url= 'https://www.google.com/search?q='
			final_url = google_url+title+'+movie'
			headers={
			'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
			}
			r=requests.get(final_url,headers=headers)
			google_soup=soup(r.text,'xml')
			rating = google_soup.find("div",{"class":"srBp4 Vrkhme"}).text.strip()
			rating = int(rating.split('%')[0])
			movie_rankings[normal_title] = rating
			print(normal_title+'.....'+str(rating)+'%');
		except:
			pass
	print("Ranking Movies...", end='\n\n')

	# RANK RATINGS
	key = list(movie_rankings.keys())

	final_ranking = [key[0]]
	for i in range(0,len(key)):
		if i != None:
			inserted = False
			movie_name = key[i]
			for j in range(len(final_ranking)):	
				if (int(movie_rankings[movie_name]) >= int(movie_rankings[final_ranking[j]])):
					final_ranking.insert(j,movie_name)
					inserted = True
					break
				elif j == len(final_ranking)-1 and inserted == False:
					final_ranking.insert(j,movie_name)

	print('\n            Movie','                     |             ','Rating (%)')
	for p in range(0,len(final_ranking)-1):
		print(' {0:<3.0f}. {1:<50}  '.format(p+1,final_ranking[p]), end='')
		print('{0:<3.0f}'.format(float(movie_rankings[final_ranking[p]])))

	go_to_webpage = input("\nGo To Netfilx Webpage? [y/n]").lower()
	if (go_to_webpage == 'y'):
		webbrowser.open('https://www.netflix.com/ca/browse/genre/34399')


if __name__ == '__main__':
	print("Welcome to WebScraping\n")
	print("Select a Mode:")
	print("( 1 ) Netflix - Rank Netflix Movies According to Ratings")
	print("( 2 ) Amazon  - Rank Amazon Coupons Accordings to Saving Amount")
	mode = input("  ")
	if (mode == '1'):
		netflix_mode()
	elif (mode == '2'):
		amazon_mode()