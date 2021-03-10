# Preconfigured e-mail formats table
Below is a table containing all preconfigured e-mail formats by the script (will be searched even if user doesn't specify any formats).
- {first} means first name (e.g. john) and can be replicated by the user in the script by typing first!!
- {last} means last name (e.g. smith) and can be replicated by the user in the script by typing last!!
- {f} means first character of first name (e.g. j for john) and can be replicated by the user in the script by typing f!!
- {l} means first character of last name (e.g. s for smith) and can be replicated by the user in the script by typing l!!
- 1963 means full birth year of target (1963 is used as an example)
- 63 means the last two digits of birth year of the target (1963 is used as an example)
- {username} means (known) username input given by the user
- @domain means the part of the e-mail address following the @ symbol and will be generated according to input given by the user

The **first column** contains all formats that will be tested for the name and surname inputs of the user <br/>
The **second column** contains all formats that will be tested if user inputs also a birth year for the target <br/>
The **third column** contains all formats that will be tested if user inputs also a known username for the target <br/>

| **Name/Surname**        | **Birth year input (e.g. 1963)**           | **Username**       |
| -------------       | :-------------:                        | -----:          |
| {f}{last}@domain	          | {last}{first}1963@domain	                     | {username}@domain|
| {f}.{last}@domain	        | {first}{last}1963@domain	                     | {username}1963@domain   |
| {f}_{last}@domain	        | {f}{last}1963@domain	                         | {username}63@domain     |
| {last}{f}@domain	          | {f}.{last}1963@domain	                         | {username}.1963@domain  |
| {last}.{f}@domain	        | {f}_{last}1963@domain	                         | {username}_1963@domain  |
| {last}_{f}@domain	        | {first}.{l}1963@domain	                       | {username}.63@domain    |
| {l}{first}@domain	        | {first}_{l}1963@domain	                       | {username}_63@domain    |
| {l}.{first}@domain	        | {last}.{first}1963@domain                     |                 |
| {l}_{first}@domain	        | {first}.{last}1963@domain                     |                 |
| {first}{l}@domain	          | {last}_{first}1963@domain                     |                 |
| {first}.{l}@domain	          | {first}_{last}1963@domain                     |                 |
| {first}_{l}@domain	          | {last}{first}63@domain                     |                 |
| {last}{first}@domain	        | {first}{last}63@domain                     |                 |
| {last}.{first}@domain	      | {f}{last}63@domain                     |                 |
| {last}_{first}@domain	      | {f}.{last}63@domain                     |                 |
| {first}{last}@domain	        | {f}_{last}63@domain                     |                 |
| {first}.{last}@domain	      | {first}.{l}63@domain                     |                 |
| {first}_{last}@domain	      | {first}_{l}63@domain                     |                 |
| {first}{last}1@domain	      | {last}.{first}63@domain                     |                 |
| {first}{last}.1@domain	      | {first}.{last}63@domain                     |                 |
| {f}{last}1@domain	          | {last}_{first}63@domain                     |                 |
| {f}{last}.1@domain	          | {first}_{last}63@domain                     |                 |
| {first}.{last}1@domain	      | {last}{first}.1963@domain                     |                 |
| {first}.{last}.1@domain	    | {first}{last}.1963@domain                     |                 |
|                       | {f}{last}.1963@domain                     |                 |
|                       | {f}.{last}.1963@domain                     |                 |
|                       | {f}_{last}.1963@domain                     |                 |
|                       | {first}.{l}.1963@domain                     |                 |
|                       | {first}_{l}.1963@domain                     |                 |
|                       | {last}.{first}.1963@domain                     |                 |
|                       | {first}.{last}.1963@domain                     |                 |
|                       | {last}_{first}.1963@domain                     |                 |
|                       | {first}_{last}.1963@domain                     |                 |
|                       | {last}{first}_1963@domain                     |                 |
|                       | {first}{last}_1963@domain                     |                 |
|                       | {f}{last}_1963@domain                     |                 |
|                       | {f}.{last}_1963@domain                     |                 |
|                       | {f}_{last}_1963@domain                     |                 |
|                       | {first}.{l}_1963@domain                     |                 |
|                       | {first}_{l}_1963@domain                     |                 |
|                       | {last}.{first}_1963@domain                     |                 |
|                       | {first}.{last}_1963@domain                     |                 |
|                       | {last}_{first}_1963@domain                     |                 |
|                       | {first}_{last}_1963@domain                     |                 |
