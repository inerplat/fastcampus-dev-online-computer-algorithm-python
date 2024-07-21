#!/bin/bash

package_name=$1

# 프로젝트 루트 디렉토리 설정 (필요에 따라 수정하세요)
project_root="./"
package_dir="$project_root/$(echo $package_name | tr '.' '/')"

code_file_java="$package_dir/Main.java"
code_file_python="$package_dir/main.py"
input_dir="$package_dir/test_inputs"
output_dir="$package_dir/test_outputs"

if [ -f "$code_file_java" ]; then
    javac "$code_file_java"
    if [ $? -ne 0 ]; then
        echo "Error: Compilation failed for $package_name."
        exit 1
    fi
    class_name="$package_name.Main"
    program="java -cp $project_root $class_name"
elif [ -f "$code_file_python" ]; then
    program="python $code_file_python"
else
    echo "Error: Main.java or main.py not found in the specified package directory $package_name."
    exit 1
fi

num_cases=$(ls $input_dir/input_*.txt | wc -l)

total_cases=0
passed_cases=0

for i in $(seq 1 $num_cases); do
    input_file="$input_dir/input_$i.txt"
    expected_output_file="$output_dir/output_$i.txt"

    start_time=$(date +%s%3N)
    actual_output=$(eval "$program < $input_file")
    end_time=$(date +%s%3N)
    elapsed_time=$((end_time - start_time))

    IFS=$'\n' read -d '' -r -a actual_output_lines <<< "$actual_output"
    mapfile -t expected_output_lines < $expected_output_file

    matched=true
    for j in "${!actual_output_lines[@]}"; do
        actual_output_line=$(echo "${actual_output_lines[j]}" | xargs)
        expected_output_line=$(echo "${expected_output_lines[j]}" | xargs)
        if [ "$actual_output_line" != "$expected_output_line" ]; then
            matched=false
            break
        fi
    done

    if [ "$matched" = true ]; then
        echo "Test case $i : Passed (Time: ${elapsed_time}ms)"
        passed_cases=$((passed_cases+1))
    else
        echo "Test case $i : Failed (Time: ${elapsed_time}ms)"
        echo "Expected Output:"
        for line in "${expected_output_lines[@]}"; do
            echo "$line"
        done
        echo "Actual Output:"
        for line in "${actual_output_lines[@]}"; do
            echo "$line"
        done
    fi

    total_cases=$((total_cases+1))
done

echo "Passed $passed_cases out of $total_cases test cases for $package_name."
