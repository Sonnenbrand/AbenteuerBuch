#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      f.reiter
#
# Created:     15.03.2019
# Copyright:   (c) f.reiter 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import json
with open(r'''C:\Users\f.reiter\Desktop\KampftabelleMonster.json''') as f:
    Tabelle = json.load(f)

print(Tabelle['0-10'])