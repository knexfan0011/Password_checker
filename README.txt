Download the latest list of SHA-1 hashed Passwords (ordered by hash) from
https://haveibeenpwned.com/Passwords
Extract it to the directory the .py files are in and rename it to "pw_hashes.txt".
If it doesn't already exist, create an empty folder called "Lookup_Files" in the same directory as the .py files

CAREFUL: Running the following file will write ~24GB in txt files to this drive, please make sure you have enough space, I haven't tested what happens if there isn't enough space.
Run SplitFileAsDicts.py.
This will take a while (~12 minutes on a Ryzen 3700x), but only needs to be done once, once it's all done password lookups will take a fraction of a second.
This constructs 4096 xyz_hashes.txt files, where xyz represents the first 3 chars of all hashes contained in the file.
You can now delete the "pw_hashes.txt" file to save some space if you'd like.

Run hashingUI.py and enter any string that you'd like to check against the latest pwned passwords list.
It will then show you if it has been pwned and if so how often.