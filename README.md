# cliper
this project is a cli clipboard history manager, but rather than taking anything you copy you manually tell it to 
put the latest thing in your clipboard history with a label and an optional priority for searching and removing or 
any action that you will do with the text like accessing it to your clipboard history you will use the label

you could search for labels with a fuzzy search algorithm implemented from fuzzywuzzy package you could also
list them remove from them and you could access them with the access command by default this will put the latest
thing you added into your clipboard history you could use its label to access another one manually

another important thing is in the save command (the one where you add the copied text) you can't have duplicate text or labels
and the priority you add has to be at least 1 and at most 3

note that in any of the commands if there was no output except for the search command there was an issue that happend or you 
entered something wrong so it got no output to give as for the search command it just didn't find anything from your query

note that this app saves your list in a hidden json file created when you use this program at path ~/.clipboard_contents.json 

I hope you like from this project and have fun and even a bit of usefullness when using it and learn from it as
much as I did thanks for copying, downloading the tool or even checking this repo!

---

## table of contents:
- [save command](#save)
- [remove command](#remove)
- [list command](#list)
- [search command](#search)
- [access command](#access)
- [setting up](#setting_up)

---

## save command
with the save command you can save the last thing in your clipboard history so the last thing you copied will be saved
it takes a required '--label' option to set its label its neccessary because you search, access, remove with the label 
I recommend using short labels to remember them if needed 

it also takes in an optional '--priority' option or '-p' for short it takes in a number to represent its importance 
from 1 min to 3 max anything lower or higher won't be accepted if you don't enter a priority it will opt to 1 by default

#### example:

`./cliper.pyz save --label <label-name> -p <priority-level>`

notice that we don't specify the text that will be saved itself just the label and the optional priority that is because the 
last thing in the clipboard will be the thing that is saved 

---

## remove command
with this command you could remove one of the copied snippets that you have of course you will use it with the 
'--label' option or '-l' for short and enter that label 

#### example: 

`./cliper.pyz remove --label <label-name>`

note that the label is case sensitive and expects you to type it exactly the same as you saved it so its recommended
to save the snippets with short labels to them

this command also takes two options '--all' or '-a' for short which will remove all the snippets at once 
and '--remove-priority' or '-rp' for short with this you provide a priority and it will remove all occurances of that 
priority in a snippet you saved 

#### example on remove all:

`./cliper.pyz remove --all`

#### example on remove-priority:

`./cliper.pyz remove --remove-priority 3`

keep in mind that if you enter a priority that is either not in the list or a label that isn't in the list both will give no output
same for if you enter an invalid priority

---

## list command
with this command you will get a table-like format with all the data it will start with the label text 
and then the priority by default it will print them with the order at which they are saved at in the json file
you could use the '--sort-by-heighest-priority' option or '-shp' for short to sort them by the priorities value
the highest first of course

#### example:
`./cliper.pyz list`

#### example with sort-by-heighest-priority option:
`./cliper.pyz list --sort-by-heighest-priority`

---

## search command
with this command you could search all of your labels, but you don't need to enter their names exactly
since this is a fuzzy search basically you could enter a part of the label and it will give you the best matches

#### example:
`./cliper.pyz search cl`
1) **cl**ock
2) **cl**ack 

of course that just means that in the list you have there is a clock and a clack and maybe more, but they just didn't get
included because they didn't pass the 80% accuracy limit set you could then access them or remove them with using the label
that matched the label in mind

note that if you eneter a snippet that doesn't have any matches above the 80% accuracy that is set there will be no output

---

## access command
the access command will by default access the latest item that you have added by copying them to your clipboard,
you could overwrite that action by selecting a label for yourself use the '--label' option or '-l' for short to 
provide the label yourself

#### example (access the last added one):
`./cliper.pyz access`

#### example (access a one at a given label):
`./cliper.pyz access --label <label-name>`

note that the label here and in any other command other than search is case sensitive and expects you to add
it fully and correctly so its recommended to add short labels you could always search for them with 'search' or
list all of them with the 'list' command

in case there is no output you probably entered something wrong like a label name that doesn't exist