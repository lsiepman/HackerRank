while read item
do
    cut -f1-3  <<< $item
done
