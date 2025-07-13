Cliper is a cli tool to manage your clipboard history by saving only important things to you rather than having to
dig through your entire clipboard history

It contains features like:
- fuzzy searching your labels
- date filtering

and of course the basic features of saving, removing, listing and accessing your clipboard contents

---

## table of contents:
- [general use](#general-use)
- [commands](#commands)
  - [save command](#save-command)
  - [list-contents command](#list-contents-command)
  - [access command](#access-command)
  - [remove command](#remove-command)
  - [search command](#search-command)
- [installation and setting up](#installation-and-setting-up)
  - [install.sh](#install.sh)
  - [manual installation](#manual-installation)
- [notes](#notes)

## general use
the main way to use this application is to save the last thing in your clipboard history and add a label to it
the label will be used to take the actions and you can't repeat the same label twice in the list or the same 
copied text

you could also save them with a priority which may help in you listing them sorted by priority it takes in a
number between 1 (lowest) to 3 (highest)

the text will be saved automatically with a creation date Y-M-D that could also be used to sort by date when listing
or to filter the fuzzy search results

the rest of the commands like `search`, `remove`, `access` and `list-contents` are all used after adding something to the
clipboard

to access what you have copied you would use the `access` command which by default will put the last thing you entered 
back to your clipboard you could override this action by providing a label with the `--label` option

## commands
### save command:
  you use this command to save the last thing in your clipboard to the clipboard of cliper it takes in a required label
  with the `--label` option and an optional priority with the `--priority` option
  
  the label will be used for all the actions of the application like searching, accessing or removing 
  so its encouraged to add short labels for ease of use
  
  the pirority will allow you to sort the listing based on it and it takes only from 1 (lowest) to 3 (highest)
  1 is the default piroity in case the user doesn't add anything
  
  the program also automatically saves a creation_date which will allow you to sort the listing or to filter
  the search results by providing it
  
  the program doesn't accept duplicate text or labels
  
  an example on how it could be used:

  `>>> cliper save --label <label> --priority <priority>`

### list-contents command:
  you use this command to list all the contents of the application by default it lists the contents at the order
  they are saved at in the clipboard
  
  you could override this action by providing a way to sort them you have two options for that the
  
  - `--date` option to sort by date it takes in only oldest or newest
  - `--priority` option to sort by priority it takes in only highest or lowest
  
  you can't enter both if you do enter both the one that was entered first will be the one to execute
  
  the data will be printed in a table format
  
  an example on how it could be used:
  
  `>>> cliper list-contents --priority highest`

### access command:
  you use this command to access something you saved in your clipboard, by default it will put the last thing you added
  to the clipboard back to your actual clipboard, but you could override this action by providing it a label with the
  `--label` option and providing the exact name of the label
  
  if the label provided doesn't exist no output will be given
  
  an example on how it could be used:
  
  `>>> cliper access --label <label>`

### remove command:
  you use this command to remove something from your clipboard it takes in one of the three
  
  - `--all` option to remove everything at once
  - `--label` option to remove an item on the given label
  - `--remove-priority` to remove all items that have the same priority level you give
  
  you can't use all of these options at once 
  
  if you enter a label or piroity that doesn't exist the command will give no output 
  
  the same could be said if you enter something incorrectly
  
  an example on how it could be used:
  
  `>>> cliper remove --all`

### search command:
  you use this command to fuzzy search the labels in your clipboard you could enter a part of the
  label and it will give you the most close takes
  
  it takes in a required query argument which it will search with if it doesn't find anything with the accuracy
  higher or equal to 80% it will give no output
  
  the lowest accuracy it could provide is 80% it doesn't provide any other metadata on what this label
  has saved or its creation date just the label itself
  
  it takes in an optional `--filter` option it allows you to filter the results on a certain date
  the date that will be given will be the creation date which you could see when listing your clipboard
  you have to provide it exactly how it is and in the same format **Y-M-D** if it doesn't find anything with
  that creation date it will give no output
  
  an example on how it could be used:
  
  `>>> cliper search gee --filter Y-M-D`

## installation and setting up
### install.sh
  this program provides an easy way of installation with the install.sh script
  
