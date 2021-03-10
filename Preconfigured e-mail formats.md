# Preconfigured e-mail formats table
Below is a table containing all preconfigured e-mail formats by the script (will be searched even if user doesn't specify any formats).
- {first} means first name (e.g. john) and can be replicated by the user in the script by typing first!!
- {last} means last name (e.g. smith) and can be replicated by the user in the script by typing last!!
- {f} means first character of first name (e.g. j for john) and can be replicated by the user in the script by typing f!!
- {l} means first character of last name (e.g. s for smith) and can be replicated by the user in the script by typing l!!
- 1963 means full birth year of target (1963 is used as an example)
- 63 means the last two digits of birth year of the target (1963 is used as an example)
- {username} means (known) username input given by the user

Each element contained in a cell will be followed by the domain(s) selected by the user at the beggining of the script as input e.g. {f}{last}@domain

The **first column** contains all formats that will be tested for the name and surname inputs of the user <br/>
The **second column** contains all formats that will be tested if user inputs also a birth year for the target <br/>
The **third column** contains all formats that will be tested if user inputs also a known username for the target <br/>

| **Name/Surname**        | **Birth year input (e.g. 1963)**           | **Username**       |
| -------------       | :-------------:                        | -----:          |
| {f}{last}	          | {last}{first}1963	                     | {username}|
| {f}.{last}	        | {first}{last}1963	                     | {username}1963   |
| {f}_{last}	        | {f}{last}1963	                         | {username}63     |
| {last}{f}	          | {f}.{last}1963	                         | {username}.1963  |
| {last}.{f}	        | {f}_{last}1963	                         | {username}_1963  |
| {last}_{f}	        | {first}.{l}1963	                       | {username}.63    |
| {l}{first}	        | {first}_{l}1963	                       | {username}_63    |
| {l}.{first}	        | {last}.{first}1963                     |                 |
| {l}_{first}	        | {first}.{last}1963                     |                 |
| {first}{l}	          | {last}_{first}1963                     |                 |
| {first}.{l}	          | {first}_{last}1963                     |                 |
| {first}_{l}	          | {last}{first}63                     |                 |
| {last}{first}	        | {first}{last}63                     |                 |
| {last}.{first}	      | {f}{last}63                     |                 |
| {last}_{first}	      | {f}.{last}63                     |                 |
| {first}{last}	        | {f}_{last}63                     |                 |
| {first}.{last}	      | {first}.{l}63                     |                 |
| {first}_{last}	      | {first}_{l}63                     |                 |
| {first}{last}1	      | {last}.{first}63                     |                 |
| {first}{last}.1	      | {first}.{last}63                     |                 |
| {f}{last}1	          | {last}_{first}63                     |                 |
| {f}{last}.1	          | {first}_{last}63                     |                 |
| {first}.{last}1	      | {last}{first}.1963                     |                 |
| {first}.{last}.1	    | {first}{last}.1963                     |                 |
|                       | {f}{last}.1963                     |                 |
|                       | {f}.{last}.1963                     |                 |
|                       | {f}_{last}.1963                     |                 |
|                       | {first}.{l}.1963                     |                 |
|                       | {first}_{l}.1963                     |                 |
|                       | {last}.{first}.1963                     |                 |
|                       | {first}.{last}.1963                     |                 |
|                       | {last}_{first}.1963                     |                 |
|                       | {first}_{last}.1963                     |                 |
|                       | {last}{first}_1963                     |                 |
|                       | {first}{last}_1963                     |                 |
|                       | {f}{last}_1963                     |                 |
|                       | {f}.{last}_1963                     |                 |
|                       | {f}_{last}_1963                     |                 |
|                       | {first}.{l}_1963                     |                 |
|                       | {first}_{l}_1963                     |                 |
|                       | {last}.{first}_1963                     |                 |
|                       | {first}.{last}_1963                     |                 |
|                       | {last}_{first}_1963                     |                 |
|                       | {first}_{last}_1963                     |                 |
