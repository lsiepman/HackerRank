while read item
do
    cut -f1-3 -d " "  <<< $item
done
