import time
#This splits the text file such that all hashes starting with 000 are one one file, 001 in another and so on
print("PLEASE READ CAREFULLY and use at own risk.")
print("If you've already run this once and Lookup_Files is created you don't need to run this.")
print("If pw_hashes.txt doesn't exist this this code will error out.")
print("Running this will write txt files with a total size roughly equal to pw_hashes.txt, not sure how this handles a lack of storage space")
print("Running this a second time without deleting the existing LookupFiles may add to existing ones, causing bigger files and slower operation")
print("If you are sure you want to proceed please enter \"Yes this is my first time\" with correct capitalization")
proceed = input()
if proceed != "Yes this is my first time":
    exit()

fullFile = open("pw_hashes.txt", "r")
chars = ("0", "1", "2", "3", "4", "5", "6", "7",
         "8", "9", "A", "B", "C", "D", "E", "F")  # potential chars in hash
found_a_hash = False  # innermost loop exits once a matching hash was found before but current line doesn't match
t0 = time.time()
start_time = time.time()

for curr_char_0 in chars:
    for curr_char_1 in chars:
        for curr_char_2 in chars:
            curr_chars = curr_char_0 + curr_char_1 + curr_char_2
            file = open("Lookup_Files/" + curr_chars + "_hashes.txt", "a+")
            for line in fullFile:
                if line[0:3] == curr_chars:
                    file.write(line)  # line break is already in the line
                    found_a_hash = True
                elif found_a_hash:
                    found_a_hash = False
                    break  # all hashes starting with curr_chars found, goto next chars
            print(curr_chars + " Done, took " + str(time.time()-start_time) + " sec")
            start_time = time.time()
print("All done, took " + str(time.time()-t0) + "sec total")
