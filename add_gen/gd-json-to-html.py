#!/usr/bin/python3
import glob
import json
import datetime
import re

#########
# NOTE: It's recommended by Fritz that this script run twice a day to keep addresses fresh in case they move there servers.
#########

ripple_re = "\*{2}__Deposit"
ripple_addr_re = "r[0-9a-zA-Z]{33}"
ripple_dest_re = "[0-9]{5}.*[0-9]"
QR_GEN_URL = "https://chart.googleapis.com/chart?cht=qr&chl=%s&chs=160x160&chld=L|0"
XLM_EXPLORER_URL = "https://stellar.expert/explorer/public/account/"

if __name__ == "__main__":
    debug = False
    try:
        output_files = []
        output_vals = {}
        for filename in glob.glob('*.json'):
            data = json.load(open(filename))
            data = filename[:-4] + data["how"]
            vals = data.split('.')
            if vals[0] not in output_files:
                output_files.append(vals[0])
            output_vals[vals[3]] = vals

        print("output_files = " + str(output_files))
        for file_prefix in output_files:
            print("file_prefix = " + str(file_prefix))
            output_file = "./" + file_prefix + ".html"
            out = "<html><head><title>" + file_prefix + " - " + str(datetime.datetime.utcnow().isoformat()) + "</title></head><body><pre>"
            
	    # process all other addresses now
            first_time = True
            for y in output_vals.values():
                if file_prefix in y:
                    paywall = y[0]
                    asset_code = y[1]
                    xlm_address = y[2]
                    asset_code_address = y[3]
                    # add XLM line first
                    if (first_time):
                        qr_address = QR_GEN_URL % (xlm_address)
                        print(qr_address)
                        out = out + "<br>XLM: " + xlm_address + "(<a href=" + qr_address + ">QR</a>)(<a href=" + XLM_EXPLORER_URL + xlm_address + ">Details</a>)"
                        first_time = False

                    match = re.search(ripple_re, asset_code_address)
                    if (match):
                        match = re.search(ripple_addr_re, asset_code_address)
                        ripple_addr = match.group(0)

                        match = re.search(ripple_dest_re, asset_code_address)
                        ripple_dest = match.group(0)
                        out = out + "<br>" + asset_code + ": " + ripple_addr + " (<font color=\"FF0000\">Required Dest. Tag: "  + ripple_dest + "</font>)"
                        print(paywall + " - " + asset_code + " - " + xlm_address + " - " + ripple_addr + " - " + ripple_dest)
                    else:
                        qr_address = QR_GEN_URL % (asset_code_address)
                        out = out + "<br>" + asset_code + ": " + asset_code_address + "(<a href=" + qr_address + ">QR</a>)"
                        print(paywall + " - " + asset_code + " - " + xlm_address + " - " + asset_code_address)
            out = out + "</pre></body></html>"
            with open(output_file, 'w+') as data_file:
                data_file.write(out)
                # implicit close when exiting with clause
    except Exception as e:
        print("Exception: ",e)
        raise

