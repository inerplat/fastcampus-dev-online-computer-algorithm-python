param (
    [string]$package_name
)

$project_root = ".\"

$package_dir = Join-Path -Path $project_root -ChildPath $package_name.Replace('.', '\')
$package_dir = (Resolve-Path -Path $package_dir).Path

$java_file = Join-Path -Path $package_dir -ChildPath "Main.java"
$python_file = Join-Path -Path $package_dir -ChildPath "main.py"
$input_dir = Join-Path -Path $package_dir -ChildPath "test_inputs"
$output_dir = Join-Path -Path $package_dir -ChildPath "test_outputs"

if (Test-Path $java_file) {
    & javac $java_file
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error: Compilation failed."
        exit 1
    }
    $class_name = "$package_name.Main"
    $program = "java -cp $project_root $class_name"
} elseif (Test-Path $python_file) {
    $program = "python $python_file"
} else {
    Write-Host "Error: Neither Main.java nor main.py found in the specified package directory."
    exit 1
}

$num_cases = (Get-ChildItem -Path $input_dir -Filter "input_*.txt").Count

$total_cases = 0
$passed_cases = 0

for ($i = 1; $i -le $num_cases; $i++) {
    $input_file = "$input_dir\input_$i.txt"
    $expected_output_file = "$output_dir\output_$i.txt"

    $execution_time = [System.Diagnostics.Stopwatch]::StartNew()
    $actual_output = & cmd /c "$program < $input_file"
    $execution_time.Stop()
    $elapsed_time = $execution_time.Elapsed.TotalSeconds

    $actual_output_lines = $actual_output -split "`n" | ForEach-Object { $_.Trim() }
    $expected_output_lines = Get-Content $expected_output_file | ForEach-Object { $_.Trim() }

    if ($elapsed_time -gt 2) {
        Write-Host "Test case $i : Failed (Timeout) (Time: $elapsed_time s)"
    } else {
        $matched = $true
        for ($j = 0; $j -lt [math]::Max($actual_output_lines.Count, $expected_output_lines.Count); $j++) {
            if ($j -ge $actual_output_lines.Count -or $j -ge $expected_output_lines.Count -or $actual_output_lines[$j] -ne $expected_output_lines[$j]) {
                $matched = $false
                break
            }
        }

        if ($matched) {
            Write-Host "Test case $i : Passed (Time: $elapsed_time s)"
            $passed_cases++
        } else {
            Write-Host "Test case $i : Failed (Time: $elapsed_time s)"
            Write-Host "Expected Output:"
            $expected_output_lines | ForEach-Object { Write-Host $_ }
            Write-Host "Actual Output:"
            $actual_output_lines | ForEach-Object { Write-Host $_ }
        }
    }

    $total_cases++
}

Write-Host "Passed $passed_cases out of $total_cases test cases."
