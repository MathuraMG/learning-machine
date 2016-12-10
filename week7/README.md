####references

`for var in *test.txt; do cat $var | awk -v ORS='' '1' >> alldata.txt; echo -e '\n' >> alldata.txt ; done`
