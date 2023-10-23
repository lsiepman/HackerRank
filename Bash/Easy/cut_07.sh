while read item
do
    cut -f4 -d " "  <<< $item
done
