#!/bin/bash

dir_path=${PWD}"/clickandbuilds/GiveDirect2/auth"

write_json_file()
{
cat > ${FILE} <<EOF
{
    "File Version": "0.1",
    "PubKey": {
	"GiveDirect-BI-Paywall": "GDHEWO2WAM6MFHPUHRZWCN3AWLW2BWXQU3VE67CLT5WVYGI6DSME24FT",
	"GiveDirect-Demo-TC-Champ-1-zippy": "GBTPPRH7OEJIN64KO5WTM3KB74HYYMWP6AZSTUZWUMRVD2FKHEIPLI66",
	"GiveDirect-Demo-TC-Champ-1-sevo": "GDNRHFKDSNDW26IV3HZG7NG5Y54GKRHCQFXCK5LBMP5WXUE6SPQ3WDWT"
    },
    "_comment": "Mainnet addresses"
}
EOF
}

echo "====================================================="
echo "This script will create a GiveDirect white-label"
echo "directory structure for app isolation."
echo "====================================================="

echo -n "Enter your build key and press [ENTER]: "
read name
short_name=${name:0:16}
echo
dir="${dir_path}/${short_name}"
echo "$dir"

if [[ ! -e $dir ]]; then
    mkdir $dir
    FILE="$dir/file.json"
    write_json_file $FILE
else
  echo "Build Key directory already registered, quitting."
  exit 1
fi
