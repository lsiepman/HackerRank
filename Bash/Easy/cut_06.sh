while read item
do
    cut -c 13-  <<< $item
done
