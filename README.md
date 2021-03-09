# emailGuesser
You 've probably heard of brute-force attacks to find a password. How about brute-force "guessing" a target's email address?

Introducing emailGuesser!

**emailGuesser** is an Open Source Intelligence (OSINT) tool which helps users "guess" their target's email address based on multiple inputs and preferences.

**DISCLAIMER**: This tool is for research purposes only.
Use this tool responsibly and ethically! You will be reliable for any abuse or harm, you may cause using it.

It is highly advisable to run the script using a VPN to enhance your privacy protection! It will also ensure your IP will not get banned due to continuous requests to the sites used.

## Installation
To install this project run: 

```bash
# clone the repo
$ git clone https://github.com/WhiteHatInspector/emailGuesser

# change the working directory to emailGuesser
$ cd emailGuesser

# run the script
$ python3 emailGuesser.py
```

## Usage
The script will search for potential e-mail addresses of a target according to inputs given by the user. It will try "guessing" potential e-mail addresses of the target by using the most common formats used in e-mail addresses (e.g. jsmith@domain or j.smith@domain).

The script asks for the following user inputs (mandatory inputs are marked with asterisk):
```
Name*: Insert the first name of your target (e.g. john)

Surname*: Insert the last name of your target (e.g. smith)

Birth year: Insert birth year in its full form (e.g. 1984), otherwise the script will assume you don't know the exact birth year. 
You can also input "no" if you don't know the year of birth

Username: Insert any known username of the target (only one). You can also input "no" if you don't know any username.

Add extra e-mail formats: Use static or dynamic formats for the username of the e-mail (part of e-mail before the @ symbol).
This option will add usernames to an already pre-configured list in the script (see table below for pre-configured usernames)
If you want to add static formats just input them (e.g. josmi94) but if you want to use dynamic formats then use any structure 
containing the following: 
- f!! (first char of the target's first name), 
- first!! (target's first name), 
- l!! (first char of the target's last name) and 
- last!! (target's last name).
Example: f!!+last!!

Add domains: Input all domains that you wish to contact a search to, separated by a single comma (e.g. yahoo.com,gmail.com)
```
The script will check the structure of the e-mail addresses that were automatically created and will query the valid ones to:
1. Skype (using the skypli.com site)
2. Breached databases (using the haveibeenpwned.com site)

Below is a list of preconfigured e-mail formats that the site will search, even if not specified otherwise by user:



All e-mail addresses that are found in any of these sites, will return to the user at the end of the script, containing further info.

The script also provides a "results.txt" at the end, that is saved to the same folder as the .py file, that the user can use for any further investigation.

The script runs continuously so after each search, it will restart from the beggining asking for the next inputs.

## Contributing
If you would like to contribute to this project, you are welcome to do so. Each and every contribution is greatly valued! Keep in mind that this tool must remain
free to use for everyone, so don't use paid APIs (like Dehashed) but try finding a work around.

Right now I am working on the following TODO list:
- [ ] Find more or alternative sites to search-query that yield immediate results about the identity of the owner of an e-mail address (like Skype)
- [ ] Find more or alternative sites to search-query in order to validate e-mail addresses (not breached data)
- [ ] Find a way to query haveIbeenPwned (or similar) site faster without having to wait for 5-8 random time duration and not getting IP banned
- [ ] Add more username formats that people use often before the @ symbol on e-mails and add them to the tool

## Feedback and Questions
For any feedback or questions please contact me on https://twitter.com/whinspector or theinspector32@protonmail.com

## License
MIT © emailGuesser
created by White Hat Inspector
