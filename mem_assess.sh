#!/bin/bash
#!/opt/anaconda3/bin/python

RUNS=200
sum=0
count=0

echo "Running mem_assess.py $RUNS times ..."

for i in $(seq 1 $RUNS)
do
    python mem_assess.py

    last_mem=$(tail -n 1 ../mem/efficient/10/out13.txt) # change this

    if [[ -z "$last_mem" ]]; then
        echo "Run $i: no output (skipped)"
        continue
    fi

    if ! [[ "$last_mem" =~ ^-?[0-9]+(\.[0-9]+)?$ ]]; then
        echo "Run $i: invalid output '$last_mem' (skipped)"
        continue
    fi

    # only keep track of non negative values
    if (( $(echo "$last_mem >= 0" | bc -l) )); then
        sum=$(echo "$sum + $last_mem" | bc)
        count=$((count+1))
        echo "Run $i: mem=${last_mem} (accepted)"
    else
        echo "Run $i: mem=${last_mem} (discarded)"
    fi
done

echo "--------------------------------"

if (( count == 0 )); then
    echo "No valid mem values recorded."
else
    avg=$(echo "scale=4; $sum / $count" | bc)
    echo "Valid runs: $count / $RUNS"
    echo "Average mem: $avg"
fi