param (
    [string]$package_name
)

# 프로젝트 루트 디렉토리 설정 (필요에 따라 수정하세요)
$project_root = ".\"
$package_dir = Join-Path -Path $project_root -ChildPath $package_name.Replace('.', '\')

$code_file_java = Join-Path -Path $package_dir -ChildPath "Main.java"
$code_file_python = Join-Path -Path $package_dir -ChildPath "main.py"
$input_dir = Join-Path -Path $package_dir -ChildPath "test_inputs"
$output_dir = Join-Path -Path $package_dir -ChildPath "test_outputs"

if (Test-Path $code_file_java) {
    & javac $code_file_java
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error: Compilation failed for $package_name."
        exit 1
    }
    $class_name = "$package_name.Main"
    $program = "java -cp $project_root $class_name"
} elseif (Test-Path $code_file_python) {
    $program = "python $code_file_python"
} else {
    Write-Host "Error: Main.java or main.py not found in the specified package directory $package_name."
    exit 1
}

$num_cases = (Get-ChildItem -Path $input_dir -Filter "input_*.txt").Count

$total_cases = 0
$passed_cases = 0

$table_output = "| Test Case | Result | Time (ms) |`n|-----------|--------|-----------|"

for ($i = 1; $i -le $num_cases; $i++) {
    $input_file = "$input_dir\input_$i.txt"
    $expected_output_file = "$output_dir\output_$i.txt"

    $start_time = [DateTime]::Now
    $actual_output = & cmd /c "$program < $input_file"
    $end_time = [DateTime]::Now
    $elapsed_time = ($end_time - $start_time).TotalMilliseconds

    $actual_output_lines = $actual_output -split "`n" | ForEach-Object { $_.Trim() }
    $expected_output_lines = Get-Content $expected_output_file | ForEach-Object { $_.Trim() }

    $matched = $true
    for ($j = 0; $j -lt [math]::Max($actual_output_lines.Count, $expected_output_lines.Count); $j++) {
        if ($j -ge $actual_output_lines.Count -or $j -ge $expected_output_lines.Count -or $actual_output_lines[$j] -ne $expected_output_lines[$j]) {
            $matched = $false
            break
        }
    }

    if ($matched) {
        $result = "Passed"
        $passed_cases++
    } else {
        $result = "Failed"
    }

    $table_output += "`n| $i | $result | $elapsed_time |"
    $total_cases++
}

Write-Host "#### Passed $passed_cases/$total_cases test cases for $package_name."
Write-Host ""
Write-Host $table_output
Write-Host ""
