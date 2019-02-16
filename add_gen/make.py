#!/usr/bin/python3
import glob
import json
import datetime
import re
import string

#########
# NOTE: It's recommended by Fritz that this script run twice a day to keep addresses fresh in case they move there servers.
#########
ripple_addr_re = "r[0-9a-zA-Z]{33}"
ripple_dest_re = "[0-9]{5}.*[0-9]"

if __name__ == "__main__":
    try:
        output_files = []
        output_vals = {}
        number = 0
        for filename in glob.glob('*.json'):
            number += 1
            data = json.load(open(filename))
            data = filename[:-5] + "_" + data["how"] + "_" + str(data["min_amount"])
            vals = data.split('_')
            output_vals[number] = vals

        # Start writing the sed file
        f = open("make.sed", "w")
        f.write("s/TS_NOW/" + str(datetime.datetime.utcnow().isoformat()) + "/\n")
        xlm_address = ""
        for y in output_vals.values():
            paywall = y[0]
            asset_code = y[1]
            xlm_address = y[2]
            asset_code_address = ""
            asset_code_min = ""
            if (asset_code == "XRP"):
                asset_code_address = y[7].translate(str.maketrans('', '', string.whitespace))
                match = re.search(ripple_addr_re, asset_code_address)
                if (match):
                    match = re.search(ripple_addr_re, asset_code_address)
                    ripple_addr = match.group(0)
                    match = re.search(ripple_dest_re, asset_code_address)
                    ripple_dest = match.group(0)
                    asset_code_address = ripple_addr + " - " + ripple_dest
                asset_code_min = y[8]
                f.write("s/RIPPLE_ADDRESS/" + str(ripple_addr) + "/\n")
                f.write("s/RIPPLE_TAG/" + str(ripple_dest) + "/\n")
                f.write("s/RIPPLE_MIN/" + str(asset_code_min) + "/\n")
            elif (asset_code == "ETH"):            
                asset_code_address = y[3]
                asset_code_min = y[4]
                f.write("s/ETHER_ADDRESS/" + str(asset_code_address) + "/\n")
                f.write("s/ETHER_MIN/" + str(asset_code_min) + "/\n")            
            elif (asset_code == "BTC"):            
                asset_code_address = y[3]
                asset_code_min = y[4]
                f.write("s/BITCOIN_ADDRESS/" + str(asset_code_address) + "/\n")
                f.write("s/BITCOIN_MIN/" + str(asset_code_min) + "/\n")            
            elif (asset_code == "LTC"):            
                asset_code_address = y[3]
                asset_code_min = y[4]
                f.write("s/LITECOIN_ADDRESS/" + str(asset_code_address) + "/\n")
                f.write("s/LITECOIN_MIN/" + str(asset_code_min) + "/\n")            
            else:
                print("Coin type skipped : " + str(asset_code) + " UNKNOWN!")
            print(str(asset_code) + " : " + str(asset_code_address) + " - " + str(asset_code_min))
        # Finish with XLM
        print("XLM : " + xlm_address + " - " + ".0001")
        f.write("s/STELLAR_ADDRESS/" + str(xlm_address) + "/\n")
        f.write("s/STELLAR_MIN/.0001/\n")
    except Exception as e:
        print("Exception: ",e)
        raise


