Cliper is a CLI tool to manage your clipboard history by saving only important things to you rather than having to dig through your entire clipboard history.

It contains features like:
- fuzzy searching your labels
- date filtering

And of course the basic features of saving, removing, listing, and accessing your clipboard contents.

## table of contents:
- [general use](#general-use)
- [commands](#commands)
  - [save command](#save-command)
  - [list-contents command](#list-contents-command)
  - [access command](#access-command)
  - [remove command](#remove-command)
  - [search command](#search-command)
- [installation and setting up](#installation-and-setting-up)
  - [pip and pipx](#pip-and-pipx)
- [notes](#notes)

## general use
The main way to use this application is to save the last thing in your clipboard history and add a label to it.  
The label will be used to take the actions and you can't repeat the same label twice in the list or the same copied text.

You could also save them with a priority which may help in listing them sorted by priority. It takes in a number between 1 (lowest) to 3 (highest).

The text will be saved automatically with a creation date Y-M-D that could also be used to sort by date when listing or to filter the fuzzy search results.

The rest of the commands like `search`, `remove`, `access`, and `list-contents` are all used after adding something to the clipboard.

To access what you have copied you would use the `access` command which by default will put the last thing you entered back to your clipboard. You could override this action by providing a label with the `--label` option.

## commands

### save command:
You use this command to save the last thing in your clipboard to the clipboard of cliper. It takes in a required label with the `--label` option and an optional priority with the `--priority` option.

The label will be used for all the actions of the application like searching, accessing, or removing, so it's encouraged to add short labels for ease of use.

The priority will allow you to sort the listing based on it and it takes only from 1 (lowest) to 3 (highest).  
1 is the default priority in case the user doesn't add anything.

The program also automatically saves a creation_date which will allow you to sort the listing or filter the search results by providing it.

The program doesn't accept duplicate text or labels.

Example:  
`>>> cliper save --label <label> --priority <priority>`

### list-contents command:
You use this command to list all the contents of the application. By default it lists the contents in the order they were saved in the clipboard.

You could override this action by providing a way to sort them. You have two options:
- `--date` option to sort by date. It takes in only `oldest` or `newest`
- `--priority` option to sort by priority. It takes in only `highest` or `lowest`

You can't enter both. If you do, the one that was entered first will be the one to execute.

The data will be printed in a table format.

Example:  
`>>> cliper list-contents --priority highest`

### access command:
You use this command to access something you saved in your clipboard. By default, it will put the last thing you added back into your actual clipboard.  
You can override this action by providing a label with the `--label` option and the exact name of the label.

If the label provided doesn't exist, no output will be given.

Example:  
`>>> cliper access --label <label>`

### remove command:
You use this command to remove something from your clipboard. It takes in one of the three:
- `--all` option to remove everything at once
- `--label` option to remove an item by the given label
- `--remove-priority` to remove all items that have the same priority level you give

You can't use all of these options at once.

If you enter a label or priority that doesn't exist, the command will give no output.  
The same applies if you enter something incorrectly.

Example:  
`>>> cliper remove --all`

### search command:
You use this command to fuzzy search the labels in your clipboard. You can enter part of the label and it will give you the closest matches.

It takes in a required query argument to search with. If it doesn't find anything with accuracy ≥ 80%, it will give no output.

The lowest accuracy it could provide is 80%. It doesn't provide any other metadata—just the label itself.

It takes an optional `--filter` option to filter the results by a certain date.  
The date must be the exact creation date shown when listing your clipboard, in this format: **Y-M-D**.

If nothing is found with that date, it will give no output.

Example:  
`>>> cliper search <query> --filter <Y-M-D>`

## installation and setting up:
### pip and pipx:
  this application is available on pip and pipx, recommended use pipx
  
  `>>> pipx install cliper`

  you are ready to go!

## notes:

All the options given have shorthand versions. To view them, run -h or --help after any command.

Please, if you encounter any bugs or issues, create a GitHub issue with as much context as possible.

Thanks for downloading this tool. I hope you enjoy it!