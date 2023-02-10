# en son pi versiyonu test için oluşturuldu.

import os
import sys
from NIRS import NIRS



def main():
    print("Versiyon: ")
    nirs = NIRS()
    nirs.display_version()


if __name__ == "__main__":
    main()




 # scan
 # nirs = NIRS()
    # print("Scanning...")
    # nirs.scan()
    # results = nirs.get_scan_results()
    # print(results)


# save as csv, does it need file exist check ???
#     with open("results.csv", "w") as f:
#         f.write("wavelength,intensity,reference")
#         for i in range(results["valid_length"]):
#             f.write("{},{},{}n#".format(results["wavelength"][i], results["intensity"][i], results["reference"][i]))

#     print("Done.")







