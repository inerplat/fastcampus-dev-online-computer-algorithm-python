#!/bin/bash

package_name=$1

project_root="./"

package_dir="$project_root/$(echo $package_name | tr '.' '/')"

java_file="$package_dir/Main.java"
python_file="$package_dir/main.py"
input_dir="$package_dir/test_inputs"
output_dir="$package_dir/test_outputs"

if [ -f "$java_file" ]; then
    javac "$java_file"
    if [ $? -ne 0 ]; then
        echo "Error: Compilation failed."
        exit 1
    fi
    class_name="$package_name.Main"
    program="java -cp $project_root $class_name"
elif [ -f "$python_file" ]; then
    program="python $python_file"
else
    echo "Error: Neither Main.java nor main.py found in the specified package directory."
    exit 1
fi

num_cases=$(ls $input_dir/input_*.txt | wc -l)

total_cases=0
passed_cases=0

for i in $(seq 1 $num_cases); do
    input_file="$input_dir/input_$i.txt"
    expected_output_file="$output_dir/output_$i.txt"

    start_time=$(date +%s%3N)
    actual_output=$($program < $input_file)
    end_time=$(date +%s%3N)
    elapsed=$((end_time - start_time))

    actual_output_lines=($(echo "$actual_output" | xargs -L 1))
    expected_output_lines=($(cat $expected_output_file | xargs -L 1))

    if [ $elapsed -gt 2000 ]; then
        echo "Test case $i : Failed (Timeout) - Time taken: ${elapsed}ms"
    else
        matched=true
        for ((j=0; j<${#actual_output_lines[@]}; j++)); do
            if [ "${actual_output_lines[j]}" != "${expected_output_lines[j]}" ]; then
                matched=false
                break
            fi
        done

        if $matched; then
            echo "Test case $i : Passed - Time taken: ${elapsed}ms"
            passed_cases=$((passed_cases+1))
        else
            echo "Test case $i : Failed - Time taken: ${elapsed}ms"
            echo "Expected Output:"
            for line in "${expected_output_lines[@]}"; do
                echo "$line"
            done
            echo "Actual Output:"
            for line in "${actual_output_lines[@]}"; do
                echo "$line"
            done
        fi
    fi

    total_cases=$((total_cases+1))
done

echo "Passed $passed_cases out of $total_cases test cases."
