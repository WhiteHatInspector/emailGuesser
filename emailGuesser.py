# imports
import re
import requests
from bs4 import BeautifulSoup
import time
import random
import csv

# Colours to be added in text output to make it more readable and user-friendly
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
reset = "\033[39m"

# Initial screen
print("Welcome to " + green + "emailGuesser" + reset + "!\nDeveloped by " + blue + "White Hat Inspector (@WHInspector)" + reset + ".\nFor feedback and/or questions send me a private message on " + blue + "https://twitter.com/whinspector" + reset)
print("")

# User inputs
while True:
	name_input = input(yellow + 'Please enter name: ' + reset)
	last_name_input = input(yellow + "Please enter surname: " + reset)
	birth_input = input(yellow + "Please enter birth year (or no): " + reset)
	username_input = input(yellow + "Please enter username (or no): " + reset)
	skype_input = "blank"
	while skype_input != "y" and skype_input != "n":
		skype_input = input(yellow + "Would you like to automatically add to the pool Skype usernames from people using this name in Skype? (y/n) " + reset)
		if skype_input != "y" and skype_input != "n":
			print(red + "Please input 'y' or 'n'!" + reset)

	# Check if birth year is 4 digits long
	if len(birth_input) != 4:
		birth_input = "no"

	# Ask user if he wants to add more e-mail formats than the ones already preconfigured
	extra_formats_input = input(yellow + "Would you like to add more e-mail formats apart from the preconfigured ones? (y/n) " + reset)
	while extra_formats_input != "y" and extra_formats_input != "n":
		print(red + "Please select a valid input." + reset)
		extra_formats_input = input(yellow + "Would you like to add more combinations than the preconfigured ones? (y/n) " + reset)

	extra_formats = []
	if extra_formats_input == "y":
		extra_formats = input(yellow + "Provide all extra formats you wish to examine, separated by commas: " + reset).split(",")

	# User input about all domains to be searched
	domain = []
	while domain == [] or domain == ['']:
		domain = input(yellow + "Please enter domains separated by a single comma: " + reset).split(",")
		if domain == ['']:
			print(red + "You must input at least one domain to be searched!" + reset)

	# Lists with which we will work during the script
	emails = []
	emails_for_verification = []
	final_emails = []
	final_emails_text = []

	startSearching = time.perf_counter()

	# for every domain specified by user, make combinations and add them to the list
	for dom in domain:
		structure = ["f!!last!!", "f!!.last!!", "f!!_last!!", "last!!f!!", "last!!.f!!", "last!!_f!!", "l!!first!!", "l!!.first!!", "l!!_first!!", "first!!l!!", "first!!.l!!", "first!!_l!!", "last!!first!!", "last!!.first!!", "last!!_first!!", "first!!last!!", "first!!.last!!", "first!!_last!!", "first!!last!!1", "first!!last!!.1", "f!!last!!1", "f!!last!!.1", "first!!.last!!1", "first!!.last!!.1"]

		# Add extra formats if specified by user
		if extra_formats_input == "y":
			for inputs in extra_formats:
				structure.append(inputs)

		# Add formats using birth year if specified by the user
		if birth_input != "no":
			structure.append("last!!first!!" + birth_input)
			structure.append("first!!last!!" + birth_input)
			structure.append("f!!last!!" + birth_input)
			structure.append("f!!.last!!" + birth_input)
			structure.append("f!!_last!!" + birth_input)
			structure.append("first!!.l!!" + birth_input)
			structure.append("first!!_l!!" + birth_input)
			structure.append("last!!.first!!" + birth_input)
			structure.append("first!!.last!!" + birth_input)
			structure.append("last!!_first!!" + birth_input)
			structure.append("first!!_last!!" + birth_input)
			structure.append("last!!first!!" + birth_input[2:])
			structure.append("first!!last!!" + birth_input[2:])
			structure.append("f!!last!!" + birth_input[2:])
			structure.append("f!!.last!!" + birth_input[2:])
			structure.append("f!!_last!!" + birth_input[2:])
			structure.append("first!!.l!!" + birth_input[2:])
			structure.append("first!!_l!!" + birth_input[2:])
			structure.append("last!!.first!!" + birth_input[2:])
			structure.append("first!!.last!!" + birth_input[2:])
			structure.append("last!!_first!!" + birth_input[2:])
			structure.append("first!!_last!!" + birth_input[2:])
			structure.append("last!!first!!." + birth_input)
			structure.append("first!!last!!." + birth_input)
			structure.append("f!!last!!." + birth_input)
			structure.append("f!!.last!!." + birth_input)
			structure.append("f!!_last!!." + birth_input)
			structure.append("first!!.l!!." + birth_input)
			structure.append("first!!_l!!." + birth_input)
			structure.append("last!!.first!!." + birth_input)
			structure.append("first!!.last!!." + birth_input)
			structure.append("last!!_first!!." + birth_input)
			structure.append("first!!_last!!." + birth_input)
			structure.append("last!!first!!_" + birth_input)
			structure.append("first!!last!!_" + birth_input)
			structure.append("f!!last!!_" + birth_input)
			structure.append("f!!.last!!_" + birth_input)
			structure.append("f!!_last!!_" + birth_input)
			structure.append("first!!.l!!_" + birth_input)
			structure.append("first!!_l!!_" + birth_input)
			structure.append("last!!.first!!_" + birth_input)
			structure.append("first!!.last!!_" + birth_input)
			structure.append("last!!_first!!_" + birth_input)
			structure.append("first!!_last!!_" + birth_input)
			structure.append("last!!first!!." + birth_input[2:])
			structure.append("first!!last!!." + birth_input[2:])
			structure.append("f!!last!!." + birth_input[2:])
			structure.append("f!!.last!!." + birth_input[2:])
			structure.append("f!!_last!!." + birth_input[2:])
			structure.append("first!!.l!!." + birth_input[2:])
			structure.append("first!!_l!!." + birth_input[2:])
			structure.append("last!!.first!!." + birth_input[2:])
			structure.append("first!!.last!!." + birth_input[2:])
			structure.append("last!!_first!!." + birth_input[2:])
			structure.append("first!!_last!!." + birth_input[2:])
			structure.append("last!!first!!_" + birth_input[2:])
			structure.append("first!!last!!_" + birth_input[2:])
			structure.append("f!!last!!_" + birth_input[2:])
			structure.append("f!!.last!!_" + birth_input[2:])
			structure.append("f!!_last!!_" + birth_input[2:])
			structure.append("first!!.l!!_" + birth_input[2:])
			structure.append("first!!_l!!_" + birth_input[2:])
			structure.append("last!!.first!!_" + birth_input[2:])
			structure.append("first!!.last!!_" + birth_input[2:])
			structure.append("last!!_first!!_" + birth_input[2:])
			structure.append("first!!_last!!_" + birth_input[2:])

		# Add username format if specified by the user
		if username_input != "no":
			structure.append(username_input)

			# add birth date to usernames only if specified by user
			if birth_input != "no":
				structure.append(username_input + birth_input)
				structure.append(username_input + birth_input[2:])
				structure.append(username_input + "." + birth_input)
				structure.append(username_input + "_" + birth_input)
				structure.append(username_input + "." + birth_input[2:])
				structure.append(username_input + "_" + birth_input[2:])

		# Search Skype based on name and surname input to find hidden e-mail addresses
		if skype_input == "y":
			print("")
			print("Searching Skype users...")
			url = "https://www.skypli.com/search/" + name_input + "%20" + last_name_input
			page = requests.get(url)
			soup = BeautifulSoup(page.content, "html.parser")
			results = soup.find(class_="search-results__title")
			if results.text.strip() != "0 results for " + name_input + " " + last_name_input:
				print(results.text.strip() + ". Autocompleting list of e-mail usernames...")
				results = soup.find_all(class_="search-results__block-info-username")
				for n in results:
					test_text = n.text.strip()
					if test_text.find(".cid.") == -1:
						if test_text.find("live:") != -1:
							if len(test_text) != 21:
								structure.append(test_text[5:])

								# find account using same e-mail username as someone else in skype (only look for underscore followed by last 1 or 2 chars being digits)
								# then add them also to the pool (original string is also added before reduced in size)
								if test_text[-1].isdigit() == True and test_text[-2] == "_":
									structure.append(test_text[5:-2])
								if test_text[-1].isdigit() == True and test_text[-2].isdigit() == True and test_text[-3] == "_":
									structure.append(test_text[5:-3])
						else:
							structure.append(test_text)
			else:
				print("No results on Skype for this name!")



		# Switch f!! with first letter of name, l!! with first letter of surname, first!! with first name and last!! with surname
		found_first = False
		found_last = False
		for x in structure:
			if x.find("first!!") != -1:
				x = x.replace("first!!", name_input)
				found_first = True
			if x.find("last!!") != -1:
				x = x.replace("last!!", last_name_input)
				found_last = True
			if x.find("f!!") != -1:
				x = x.replace("f!!", name_input[0])
			if x.find("l!!") != -1:
				x = x.replace("l!!", last_name_input[0])
			emails.append(x + "@" + dom)


	# Simple Regex for syntax checking
	regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

	# Email addresses verification (Bulk syntax checking)
	for n in emails:

		addressToVerify = n

		# Syntax check
		match = re.match(regex, addressToVerify)
		if match == None:
			print("verifying " + red + n + reset + "... Bad Syntax")
		else:
			print("verifying " + green + n + reset + "... Good Syntax")
			# if good syntax, add to e-mail addresses to be checked
			emails_for_verification.append(n)

	# If there are valid syntaxed e-mail, check them. Otherwise return an error message to the user.
	if len(emails_for_verification) != 0:
		print("Checking e-mails with good syntax...")
	else:
		print("There is no e-mail with valid syntax to check.")

	# check Skypli for speed then check haveibeenpwned if not found on skype
	if len(emails_for_verification) != 0:

		# Initialize request timer for first iteration of beenPwned
		requestPwnedStartTimer = 0

		for mailcheck in emails_for_verification:

			url = "https://www.skypli.com/search/" + mailcheck
			page = requests.get(url)
			soup = BeautifulSoup(page.content, "html.parser")
			results = soup.find_all(class_="search-results__title")

			# If an e-mail was found registered to only one user in Skype, print his details
			# Else if found registered to multiple users, show link to the tool user to decide if he wants to see more info
			# Else if found on breached database, return that the e-mail address is found to be Pwned
			# Else, return that the e-mail was not found to be pwned (does not exist)
			for n in results:
				if n.text.strip() == "1 results for " + mailcheck:
					final_emails_text.insert(0, mailcheck)
					print(blue + mailcheck + reset + " was found in Skype")
					result = soup.find(class_="search-results__block-info-username")
					url_new = "https://www.skypli.com/profile/" + result.text.strip()
					page_new = requests.get(url_new)
					soup_new = BeautifulSoup(page_new.content, "html.parser")
					mailcheck = blue + mailcheck + reset
					result_new = soup_new.find_all(class_="profile-box__table-value")
					for r in result_new:
						mailcheck = mailcheck + "\n" + r.text.strip()
					final_emails.insert(0, mailcheck + "\nMore info: " + url_new + "\n") # Add it to the top of the list in order to be shown first as Skype account
				elif n.text.strip() != "0 results for " + mailcheck:
					final_emails_text.insert(0, mailcheck)
					print(blue + mailcheck + reset + " was found in multiple Skype accounts")
					final_emails.insert(0, blue + mailcheck + reset + " Multiple skype accounts found: " + url + "\n") # Add it to the top of the list in order to be shown first as Skype account
				else:
					# Count time elapsed since last haveIbeenPwned iteration/check
					requestPwnedEndTimer = time.perf_counter()
					requestPwnedTimePassed = requestPwnedEndTimer - requestPwnedStartTimer

					# Add a random delay between 7 and 11 seconds to not let your IP get banned
					randomTimePassed = random.randint(7, 11)
					if requestPwnedTimePassed < randomTimePassed:
						time.sleep(randomTimePassed - requestPwnedTimePassed)

					url = "https://haveibeenpwned.com/account/" + mailcheck
					page = requests.get(url)
					soup = BeautifulSoup(page.content, 'html.parser')
					results = soup.find_all(id="pwnCount")  # class_='pwnTitle'
					# print(results)
					for n in results:
						if n.text.strip() == "Not pwned in any data breaches and found no pastes (subscribe to search sensitive breaches)":
							print(green + mailcheck + reset + " not found in breached database.")
						else:
							print(red + mailcheck + reset + " was found to be " + red + "Pwned!" + reset)
							final_emails_text.append(mailcheck)
							final_emails.append(red + mailcheck + reset + "\n") # Add it to the bottom of the list as breached with no additional details

					# Restart timer
					requestPwnedStartTimer = time.perf_counter()

	# Show user all e-mails that were found on skype or pwned
	print("")
	print("-------------------------------------")
	print("")
	print("Emails found:\n")
	for finalEmail in final_emails:
		print(finalEmail)

	endSearching = time.perf_counter()

	if len(final_emails) != 0:
		# Ask user if he wants output in txt or csv format
		print("")
		outputs = "0"
		while outputs != "1" and outputs != "2" and outputs != "3" and outputs != "4":
			outputs = input(yellow + "Would you like any outputs?\n[1] No\n[2] .txt file\n[3] .csv file\n[4] Both\nYour choice: " + reset)
			if outputs != "1" and outputs != "2" and outputs != "3" and outputs != "4":
				print(red + "Please select 1,2,3 or 4!" + reset)

		# Write results.txt file with all emails found in clear form
		if outputs == "2" or outputs == "4":
			print("")
			print("Creating txt file...")
			f = open("results.txt", "w")
			for finalEmail in final_emails_text:
				f.write(finalEmail + "\n")
			print(f.name + " created!")
			f.close()  # close file after writing

		# Write resultscsv.csv file with all emails found in clear form
		if outputs == "3" or outputs == "4":
			print("")
			print("Creating csv file...")
			with open('resultscsv.csv', 'w', newline='') as resultscsv:
				resultswriter = csv.writer(resultscsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
				for finalEmail in final_emails_text:
					resultswriter.writerow([finalEmail])
			print("resultscsv.csv created!")
	else:
		print(red + "No e-mails found! :(" + reset)

	print("")
	if len(emails_for_verification) != 0:
		print(f"Your search lasted for {endSearching - startSearching:0.4f} seconds.\nEmails queried where {len(emails_for_verification)} in total.\nAverage verification time per e-mail address was {(endSearching - startSearching)/len(emails_for_verification):0.2f}.")
	else:
		print(f"Your search lasted for {endSearching - startSearching:0.4f} seconds.\nEmails queried where {len(emails_for_verification)} in total.")
	print("")