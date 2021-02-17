rm -rf */*/__pycache__
rm -rf */__pycache__
rm -rf __pycache__

# wc -l : Prints the number of lines in a file.
# wc -w : prints the number of words in a file.
# wc -c : Displays the count of bytes in a file.
# wc -m : prints the count of characters from a file.
# wc -L : prints only the length of the longest line in a file.

echo "\t===ALL DATA STATS==="
echo "Lines:\t\t"    $(wc -l README.md *.sh LICENSE .gitignore lms *.py */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")
echo "Words:\t\t"    $(wc -w README.md *.sh LICENSE .gitignore lms *.py */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")
echo "Characters:\t" $(wc -m README.md *.sh LICENSE .gitignore lms *.py */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")
echo "Bytes:\t\t"    $(wc -c README.md *.sh LICENSE .gitignore lms *.py */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")

echo "\n\n\t===PROGRAM FILES STATS==="
echo "Lines:\t\t"    $(wc -l lms *.py */*.py */*/*.py | grep -iEv ".py|lms")
echo "Words:\t\t"    $(wc -w lms *.py */*.py */*/*.py | grep -iEv ".py|lms")
echo "Characters:\t" $(wc -m lms *.py */*.py */*/*.py | grep -iEv ".py|lms")
echo "Bytes:\t\t"    $(wc -c lms *.py */*.py */*/*.py | grep -iEv ".py|lms")

echo "\n\n\t===SAVE DATA STATS==="
echo "Lines:\t\t"    $(wc -l .*/*/*.txt .*/*/.*.txt | grep -iEv ".txt")
echo "Words:\t\t"    $(wc -w .*/*/*.txt .*/*/.*.txt | grep -iEv ".txt")
echo "Characters:\t" $(wc -m .*/*/*.txt .*/*/.*.txt | grep -iEv ".txt")
echo "Bytes:\t\t"    $(wc -c .*/*/*.txt .*/*/.*.txt | grep -iEv ".txt")

# rm -rf .save_data
