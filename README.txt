Introduction:

Do you not trust the password lookup at https://haveibeenpwned.com/Passwords for some reason?
Well good news, now you can trust my coding abilities instead!
And because I am way too lazy to set up a server or whatever, I don't even know how I would collect passwords that someone enters into this software, it's basically magic!
And if you don't trust me for some (probably good) reason, just read the source code to convince yourself of the fact that there is no networking code in there whatsoever!
Amazing!


Actual Readme:

Download the latest list of SHA-1 hashed Passwords (ordered by hash) from:
https://haveibeenpwned.com/Passwords (Yes it's really that big)
Extract it to the directory the .py files are in and rename it to "pw_hashes.txt".
Create an empty folder called "Lookup_Files" in the same directory as the .py files

CAREFUL: Running the following file will write ~24GB in txt files to this drive, please make sure you have enough space, I haven't tested what happens if there isn't enough space.
Run SplitFileAsDicts.py.
This constructs 4096 xyz_hashes.txt files, where xyz represents the first 3 chars of all hashes contained in the file.
This will take a while (~12 minutes on a Ryzen 3700x), but only needs to be done once.
When this is done, password lookups will take a fraction of a second.

Once it has finished running, you can delete the "pw_hashes.txt" file to save some space if you'd like.

Run hashingUI.py and enter any string that you'd like to check against the latest pwned passwords list.
It will then show you if it has been pwned and if so how often.
