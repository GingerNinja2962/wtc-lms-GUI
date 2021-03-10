rm -rf */*/__pycache__
rm -rf */__pycache__
rm -rf __pycache__
rm -rf build/
# rm -rf .save_data # optional

# wc -l : Prints the number of lines in a file.
# wc -w : prints the number of words in a file.
# wc -c : Displays the count of bytes in a file.
# wc -m : prints the count of characters from a file.
# wc -L : prints only the length of the longest line in a file.


echo "\t=======ALL DATA STATS======"
if test -f "./dist/wtc-lms-GUI"; then
    echo "Lines:\t\t"    $(wc -l */wtc-lms-GUI lms */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")
    echo "Words:\t\t"    $(wc -w */wtc-lms-GUI lms */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")
    echo "Characters:\t" $(wc -m */wtc-lms-GUI lms */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")
    echo "Bytes:\t\t"    $(wc -c */wtc-lms-GUI lms */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")
else
    echo "Lines:\t\t"    $(wc -l lms */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")
    echo "Words:\t\t"    $(wc -w lms */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")
    echo "Characters:\t" $(wc -m lms */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")
    echo "Bytes:\t\t"    $(wc -c lms */*.py */*/*.py .*/*/*.txt .*/*/.*.txt | grep -iEv ".py|.txt|.md|.sh|lms|LICENSE|.gitignore")
fi

echo "\n\n\t====PROGRAM FILES STATS===="
echo "Lines:\t\t"    $(wc -l lms */*.py */*/*.py | grep -iEv ".py|lms")
echo "Words:\t\t"    $(wc -w lms */*.py */*/*.py | grep -iEv ".py|lms")
echo "Characters:\t" $(wc -m lms */*.py */*/*.py | grep -iEv ".py|lms")
echo "Bytes:\t\t"    $(wc -c lms */*.py */*/*.py | grep -iEv ".py|lms")

echo "\n\n\t===EXECUTABLE DATA STATS==="
if test -f "./dist/wtc-lms-GUI"; then
    echo "Lines:\t\t"    $(wc -l */wtc-lms-GUI)
    echo "Words:\t\t"    $(wc -w */wtc-lms-GUI)
    echo "Characters:\t" $(wc -m */wtc-lms-GUI)
    echo "Bytes:\t\t"    $(wc -c */wtc-lms-GUI)
else
    echo "\n\t       +-----------+"
    echo "\t       | NOT FOUND |"
    echo "\t       +-----------+"
fi

echo "\n\n\t======SAVE DATA STATS======"
if [ -d "./.save_data" ]; then
    echo "Lines:\t\t"    $(wc -l .*/*/*.txt .*/*/.*.txt | grep -iEv ".txt")
    echo "Words:\t\t"    $(wc -w .*/*/*.txt .*/*/.*.txt | grep -iEv ".txt")
    echo "Characters:\t" $(wc -m .*/*/*.txt .*/*/.*.txt | grep -iEv ".txt")
    echo "Bytes:\t\t"    $(wc -c .*/*/*.txt .*/*/.*.txt | grep -iEv ".txt")
else
    echo "\n\t       +-----------+"
    echo "\t       | NOT FOUND |"
    echo "\t       +-----------+\n\n"
fi
