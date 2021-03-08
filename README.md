# emailGuesser
You 've heard of brute-force attacks to find a password. How about brute-force guessing a target's email address?

Introducing emailGuesser!
emailGuesser is an Open Source Intelligence (OSINT) project which helps users "guess" their target's email address based on multiple inputs and preferences.

This tool is for research purposes only.
Use this tool responsibly and ethically! You will be reliable for any abuse or harm, you may cause using it.

It is highly advisable to run the script using a VPN to enhance your privacy protection! It will also ensure your IP will not get banned due to continuous requests to the sites used.

Installation
To install this project run: 
$ git clone https://github.com/WhiteHatInspector/emailGuesser --> 
cd emailGuesser --> 
python3 emailGuesser.py

Usage
The script will search for potential e-mail addresses of a target according to inputs given by the user. It will try "guessing" potential e-mail addresses of the target by using the most common formats used in e-mail addresses (e.g. jsmith@gmail.com).

The script asks for the following user inputs:
Name: Insert the first name of your target (mandatory)
Surname: Insert the last name of your target (mandatory)
Birth year: Insert birth year in its full form (e.g. 1984), otherwise the script will assume you don't know the exact birth year. You can also input "no" if you don't know the year of birth - Optional field
Username: Insert any known username of the target (only one) - Optional field
Add extra e-mail formats: Use static or dynamic formats for the username of the e-mail (part of e-mail before the @ symbol). If you want to add static formats just input them (e.g. josmi94) but if you want to use dynamic formats then use any structure containing the following: f!! -for first char of the target's first name-, first!! -for the target's first name-, l!! -for first char of the target's last name- and last!! -for the target's last name-.
Add domains: Input all domains that you wish to contact a search to, separated by a single comma (e.g. yahoo.com,gmail.com)

The script will check the structure of the e-mail addresses and will query the valid ones to:
1. Skype (using the skypli.com site)
2. Breached databases (using the haveibeenpwned.com site)

All e-mail addresses that are found in any of these sites, will return to the user at the end of the script, containing further info.
The script also provides a "results.txt" at the end, that is saved to the same folder as the .py file, that the user can use for any further investigation.

The script runs continuously so after each search, it will restart from the beggining asking for the next inputs.

For any feedback or questions please contact me on https://twitter.com/whinspector or theinspector32@protonmail.com
