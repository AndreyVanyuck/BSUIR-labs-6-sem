#!/bin/bash
tests=(tests/input*.txt)

for i in "${!tests[@]}"; do
    echo "Running test $((i + 1))"
    ./build/program <"${tests[$i]}" >"tests/output$((i + 1)).txt"
    if cmp -s "tests/expected_output_$((i + 1)).txt" "tests/output$((i + 1)).txt"; then
        echo "Passed"
    else
        echo "Fail"
        break
    fi
done
