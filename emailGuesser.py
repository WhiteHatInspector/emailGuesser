import re
import requests
from bs4 import BeautifulSoup
import time
import random

# Colours to be added in text output to make it more readable and user-friendly
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
reset = "\033[39m"

print("Welcome to " + green + "emailGuesser" + reset + "!\nDeveloped by " + blue + "White Hat Inspector (@WHInspector)" + reset + ".\nFor feedback and/or questions send me a private message on " + blue + "https://twitter.com/whinspector" + reset)

# User inputs
while True == True:
	input1 = input('Please enter name: ')
	input2 = input("Please enter surname: ")
	input3 = input("Please enter birth year (or no): ")
	input4 = input("Please enter username (or no): ")

	if len(input3) != 4:
		input3 = "no"

	input5 = input("Would you like to add more e-mail formats apart from the preconfigured ones? (y/n) ")
	while input5 != "y" and input5 != "n":
		print(red + "Please select a valid input." + reset)
		input5 = input("Would you like to add more combinations than the preconfigured ones? (y/n) ")

	input6 = []
	if input5 == "y":
		input6 = input("Provide all extra formats you wish to examine, separated by commas: ").split(",")

	domain = input("Please enter domains separated by a single comma: ").split(",")

	# Lists with which we will work
	emails = []
	emails_for_verification = []
	final_emails = []
	final_emails_text = []

	# for every domain specified by user, make combinations and add them to the list
	for dom in domain:
		structure = ["f!!last!!", "f!!.last!!", "f!!_last!!", "last!!f!!", "last!!.f!!", "last!!_f!!", "l!!first!!", "l!!.first!!", "l!!_first!!", "first!!l!!", "first!!.l!!", "first!!_l!!", "last!!first!!", "last!!.first!!", "last!!_first!!", "first!!last!!", "first!!.last!!", "first!!_last!!", "first!!last!!1", "first!!last!!.1", "f!!last!!1", "f!!last!!.1", "first!!.last!!1", "first!!.last!!.1"]

		if input5 == "y":
			for inputs in input6:
				structure.append(inputs)

		if input3 != "no":
			structure.append("last!!first!!" + input3)
			structure.append("first!!last!!" + input3)
			structure.append("f!!last!!" + input3)
			structure.append("f!!.last!!" + input3)
			structure.append("f!!_last!!" + input3)
			structure.append("first!!.l!!" + input3)
			structure.append("first!!_l!!" + input3)
			structure.append("last!!.first!!" + input3)
			structure.append("first!!.last!!" + input3)
			structure.append("last!!_first!!" + input3)
			structure.append("first!!_last!!" + input3)
			structure.append("last!!first!!" + input3[2:])
			structure.append("first!!last!!" + input3[2:])
			structure.append("f!!last!!" + input3[2:])
			structure.append("f!!.last!!" + input3[2:])
			structure.append("f!!_last!!" + input3[2:])
			structure.append("first!!.l!!" + input3[2:])
			structure.append("first!!_l!!" + input3[2:])
			structure.append("last!!.first!!" + input3[2:])
			structure.append("first!!.last!!" + input3[2:])
			structure.append("last!!_first!!" + input3[2:])
			structure.append("first!!_last!!" + input3[2:])
			structure.append("last!!first!!." + input3)
			structure.append("first!!last!!." + input3)
			structure.append("f!!last!!." + input3)
			structure.append("f!!.last!!." + input3)
			structure.append("f!!_last!!." + input3)
			structure.append("first!!.l!!." + input3)
			structure.append("first!!_l!!." + input3)
			structure.append("last!!.first!!." + input3)
			structure.append("first!!.last!!." + input3)
			structure.append("last!!_first!!." + input3)
			structure.append("first!!_last!!." + input3)
			structure.append("last!!first!!_" + input3)
			structure.append("first!!last!!_" + input3)
			structure.append("f!!last!!_" + input3)
			structure.append("f!!.last!!_" + input3)
			structure.append("f!!_last!!_" + input3)
			structure.append("first!!.l!!_" + input3)
			structure.append("first!!_l!!_" + input3)
			structure.append("last!!.first!!_" + input3)
			structure.append("first!!.last!!_" + input3)
			structure.append("last!!_first!!_" + input3)
			structure.append("first!!_last!!_" + input3)
			structure.append("last!!first!!." + input3[2:])
			structure.append("first!!last!!." + input3[2:])
			structure.append("f!!last!!." + input3[2:])
			structure.append("f!!.last!!." + input3[2:])
			structure.append("f!!_last!!." + input3[2:])
			structure.append("first!!.l!!." + input3[2:])
			structure.append("first!!_l!!." + input3[2:])
			structure.append("last!!.first!!." + input3[2:])
			structure.append("first!!.last!!." + input3[2:])
			structure.append("last!!_first!!." + input3[2:])
			structure.append("first!!_last!!." + input3[2:])
			structure.append("last!!first!!_" + input3[2:])
			structure.append("first!!last!!_" + input3[2:])
			structure.append("f!!last!!_" + input3[2:])
			structure.append("f!!.last!!_" + input3[2:])
			structure.append("f!!_last!!_" + input3[2:])
			structure.append("first!!.l!!_" + input3[2:])
			structure.append("first!!_l!!_" + input3[2:])
			structure.append("last!!.first!!_" + input3[2:])
			structure.append("first!!.last!!_" + input3[2:])
			structure.append("last!!_first!!_" + input3[2:])
			structure.append("first!!_last!!_" + input3[2:])

		if input4 != "no":
			structure.append(input4)

			# add birth date to usernames only if specified by user
			if input3 != "no":
				structure.append(input4 + input3)
				structure.append(input4 + input3[2:])
				structure.append(input4 + "." + input3)
				structure.append(input4 + "_" + input3)
				structure.append(input4 + "." + input3[2:])
				structure.append(input4 + "_" + input3[2:])

		# Switch f!! with first letter of name, l!! with first letter of surname, first!! with first name and last!! with surname
		found_first = False
		found_last = False
		for x in structure:
			if x.find("first!!") != -1:
				x = x.replace("first!!", input1)
				found_first = True
			if x.find("last!!") != -1:
				x = x.replace("last!!", input2)
				found_last = True
			if x.find("f!!") != -1:
				x = x.replace("f!!", input1[0])
			if x.find("l!!") != -1:
				x = x.replace("l!!", input2[0])
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
			# raise ValueError('Bad Syntax')
		else:
			print("verifying " + green + n + reset + "... Good Syntax")
			emails_for_verification.append(n)

	if len(emails_for_verification) != 0:
		print("Checking e-mails with good syntax...")
		# print("Checking following emails: ")
		# for email in emails_for_verification:
			# print(email)  # Verify addresses
	else:
		print("There is no e-mail with valid syntax to check.")

	# check Skypli for speed then check haveibeenpwned if not found on skype
	if len(emails_for_verification) != 0:
		for mailcheck in emails_for_verification:

			# print("https://www.skypli.com/search/" + mailcheck)
			url = "https://www.skypli.com/search/" + mailcheck
			page = requests.get(url)
			soup = BeautifulSoup(page.content, "html.parser")
			results = soup.find_all(class_="search-results__title")

			for n in results:
				# print("Skype")
				# print(n)
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
					# print("https://haveibeenpwned.com/account/" + mailcheck)
					url = "https://haveibeenpwned.com/account/" + mailcheck
					page = requests.get(url)
					soup = BeautifulSoup(page.content, 'html.parser')
					results = soup.find_all(id="pwnCount")  # class_='pwnTitle'
					# print(results)
					for n in results:
						# print("HaveIBeenPwned")
						if n.text.strip() == "Not pwned in any data breaches and found no pastes (subscribe to search sensitive breaches)":
							print(green + mailcheck + reset + " not found in breached database.")
						else:
							print(red + mailcheck + reset + " was found to be " + red + "Pwned!" + reset)
							final_emails_text.append(mailcheck)
							final_emails.append(red + mailcheck + reset + "\n") # Add it to the bottom of the list as breached with no additional details
					time.sleep(random.randint(5, 8)) # Add a random delay between 5 and 8 to not let your IP get banned

	# emails that were found on skype or pwned
	print("")
	print("-------------------------------------")
	print("")
	print("Emails found:\n")
	for finalEmail in final_emails:
		print(finalEmail)

	# Write txt file with all emails found
	print("")
	print("Creating txt file...")
	f = open("results.txt", "w")
	for finalEmail in final_emails_text:
		f.write(finalEmail + "\n")
	print(f.name + " created!")
	f.close()