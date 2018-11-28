#!/bin/sh

echo "\n\n"
echo "Fetching BI json Addresses"
echo "GiveDirect.BI*interstellar.exchange"
echo "DEPOSIT_ACCOUNT_BI = GDHEWO2WAM6MFHPUHRZWCN3AWLW2BWXQU3VE67CLT5WVYGI6DSME24FT"
echo "---------------------"
wget -q --show-progress -O BI_BTC_GDHEWO2WAM6MFHPUHRZWCN3AWLW2BWXQU3VE67CLT5WVYGI6DSME24FT.json 'http://cryptoanchor.io/stellar/deposit?asset_code=BTC&account=GDHEWO2WAM6MFHPUHRZWCN3AWLW2BWXQU3VE67CLT5WVYGI6DSME24FT'
wget -q --show-progress -O BI_LTC_GDHEWO2WAM6MFHPUHRZWCN3AWLW2BWXQU3VE67CLT5WVYGI6DSME24FT.json 'http://cryptoanchor.io/stellar/deposit?asset_code=LTC&account=GDHEWO2WAM6MFHPUHRZWCN3AWLW2BWXQU3VE67CLT5WVYGI6DSME24FT'
wget -q --show-progress -O BI_ETH_GDHEWO2WAM6MFHPUHRZWCN3AWLW2BWXQU3VE67CLT5WVYGI6DSME24FT.json 'http://cryptoanchor.io/stellar/deposit?asset_code=ETH&account=GDHEWO2WAM6MFHPUHRZWCN3AWLW2BWXQU3VE67CLT5WVYGI6DSME24FT'
wget -q --show-progress -O BI_XRP_GDHEWO2WAM6MFHPUHRZWCN3AWLW2BWXQU3VE67CLT5WVYGI6DSME24FT.json 'http://cryptoanchor.io/stellar/deposit?asset_code=XRP&account=GDHEWO2WAM6MFHPUHRZWCN3AWLW2BWXQU3VE67CLT5WVYGI6DSME24FT'

echo "\n"
echo "Create make.sed from json files..."
echo "---------------------"
./make.py

echo "\n"
echo "Use sed to create html file..."
echo "---------------------"
sed -f ./make.sed ./make.template > ./make.html

echo "\n"
echo "Running grep test to confirm all addresses were update in the template..."
echo "---------------------"
grep title make.template
grep title make.html
grep GDHEWO2WAM6MFHPUHRZWCN3AWLW2BWXQU3VE67CLT5WVYGI6DSME24FT make.html | wc -l

echo "\n"
echo "Removing json files..."
echo "---------------------"
rm ./*.json
echo "Done."

