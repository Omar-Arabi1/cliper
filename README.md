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
- [installation and setting up]
  - [install.sh](#install.sh)
  - [manual installation](#manual-installation)

## general use
the main way to use this application is to save the last thing in your clipboard history and add a label to it
the label will be used to take the actions and you can't repeat the same label twice in the list or the same 
copied text

you could also save them with a priority which may help in you listing them sorted by priority it takes in a
number between 1 (lowest) to 3 (highest)

the text will be saved automatically with a creation date Y-M-D that could also be used to sort by date when listing
or to filter the fuzzy searc results

the rest of the commands like `search`, `remove`, `access` and `list-contents` are all used after adding something to the
clipboard

to access what you have copied you would use the access command which by default will put the last thing you entered 
back to your clipboard you could override this action by providing a label with the `--label` option

## commands
### save command:
    you use this command to save the last thing in your clipboard to the list it takes in a required label
    with the `--label` option and an optional priority with the `--priority` option
    
    the label will be used for all the actions of the application like searching, accessing or removing 
    so its encouraged to add short labels for ease of use
    
    the pirority will allow you to sort the listing based on it and it takes only from 1 (lowest) to 3 (highest)
    1 is the default piroity in case the user doesn't add anything
    
    the program also automatically saves a creation_date which will allow you to sort the listing or to filter
    the search results by providing it
    
    the program doesn't accept duplicate text or label

### list-contents command:
    