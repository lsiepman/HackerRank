while read item
do
    cut -f2- <<< $item
done
