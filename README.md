### deplicate file cleanser

This script first finds all PNG files (edit the code for any file type as you wish) in the current directory and its subdirectories, calculates their hashes, and stores them in a dictionary. If a hash already exists in the dictionary, it means there's a duplicate file. Finally, it deletes the duplicate files found. Make sure to run this script in the directory where you want to detect and delete duplicate PNG files.

#### execute the cleanser by:
```
python cleanser.py
```
