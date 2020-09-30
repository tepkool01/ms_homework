# ms_homework
A homework submission for Microsoft contract role. There are 2 different files for the hyper parameter naming. One is by using the OS library in python to find a common prefix to build the unique string, and the other uses no libraries / Trie algorithm to find a unique prefix. In practice, I would probably use the OS library unless there is a need to roll-my-own.

# Running
Simply modify the last line in either file to run the function with whatever payload you want to test with. These files could be easily modified to accept command line arguments as an alternative execution approach.


# CONCERNS / THOUGHTS
- What about non-ascii characters?
- What about 'None' or blank values?
- What about really long keys or valuess
- 0 and negative prefix lengths? should just equal original string?
- Might be better to collect all of the duplicates and then process their duplicate prefixes rather than by 2 at a time
- In get unique prefix (os library), there could be an array out of bounds issue if picking from a character beyond the string length
- Added space by using keys dictionary, but could probably do this (if needed) within the existing dict
