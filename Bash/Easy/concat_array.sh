my_array=($(cat))
my_array=("${my_array[@]}" "${my_array[@]}" "${my_array[@]}")

echo ${my_array[@]}

