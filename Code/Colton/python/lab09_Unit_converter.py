unit_inches = {'inches': 1, 'foot': .08, 'yards': .027, 'meters': .025, 'kilometers': 0.0000254, 'miles': 0.000016}
unit_feet = {'inches': 12, 'foot': 1, 'yards': .33, 'meters': .0348, 'kilometers': .003, 'miles': .001}
unit_yards = {'inches': .02, 'foot': 3, 'yards': 1, 'meters': .9144, 'kilometers': .0009, 'miles': .0005}
unit_miles = {'inches': 63360, 'foot': 5280, 'yards': 1760, 'meters': 1609.34, 'kilometers': 1.6, 'miles': 1}
unit_meters = {'inches': 39.3701, 'foot': 3.28, 'yards': 1.09, 'meters': 1, 'kilometers': .001, 'miles': .00062}
unit_kilometers = {'inches': 39370, 'foot': 3280, 'yards': 1093, 'meters': 1000, 'kilometers': 1, 'miles': .62}

dist = int(input("What is the distance?\n:"))
in_unit = input("What is the input unit?\ninches, foot, yards, meters, kilometers, or miles\n:").lower()
while in_unit not in unit_meters.keys():
    in_unit = input("What is the input unit?\ninch, foot, yards, meters, kilometers, or miles\n:").lower()

out_unit = input("What is the output unit?\ninches, foot, yards, meters, kilometers, or miles\n:").lower()
while out_unit not in unit_meters.keys():
    out_unit = input("What is the output unit?\ninches, foot, yards, meters, kilometers, or miles\n:").lower()

while in_unit == 'inches':
    result = dist * unit_inches[out_unit]
    print(result)
    break

##############################
while in_unit == 'foot':
    result = dist * unit_feet[out_unit]
    print(result)
    break

########################################################
while in_unit == 'yards':
    result = dist * unit_yards[out_unit]
    print(result)
    break

##########################################################
while in_unit == 'meters':
    result = dist * unit_meters[out_unit]
    print(result)
    break
 ######################################################
while in_unit == 'kilometers':
    result = dist * unit_kilometers[out_unit]
    print(result)
    break
###########################################################
while in_unit == 'miles':
    result = dist * unit_miles[out_unit]
    print(result)
    break