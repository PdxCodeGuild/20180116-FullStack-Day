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
    if out_unit == 'inches':
        result = dist * unit_inches["inches"]
        print(result)
        break
    elif out_unit == 'foot':
        result = dist * unit_inches["foot"]
        print(result)
        break
    elif out_unit == 'yards':
        result = dist * unit_inches["yards"]
        print(result)
        break
    elif out_unit == 'meters':
        result = dist * unit_inches["meters"]
        print(result)
        break
    elif out_unit == 'kilometers':
        result = dist * unit_inches["kilometers"]
        print(result)
        break
    elif out_unit == 'miles':
        result = dist * unit_inches["miles"]
        print(result)
        break
#########################################################
while in_unit == 'foot':
    if out_unit == 'inches':
        result = dist * unit_feet["inches"]
        print(result)
        break
    elif out_unit == 'foot':
        result = dist * unit_feet["foot"]
        print(result)
        break
    elif out_unit == 'yards':
        result = dist * unit_feet["yards"]
        print(result)
        break
    elif out_unit == 'meters':
        result = dist * unit_feet["meters"]
        print(result)
        break
    elif out_unit == 'kilometers':
        result = dist * unit_feet["kilometers"]
        print(result)
        break
    elif out_unit == 'miles':
        result = dist * unit_feet["miles"]
        print(result)
        break
########################################################
while in_unit == 'yards':
    if out_unit == 'inches':
        result = dist * unit_yards["inches"]
        print(result)
        break
    elif out_unit == 'foot':
        result = dist * unit_yards["foot"]
        print(result)
        break
    elif out_unit == 'yards':
        result = dist * unit_yards["yards"]
        print(result)
        break
    elif out_unit == 'meters':
        result = dist * unit_yards["meters"]
        print(result)
        break
    elif out_unit == 'kilometers':
        result = dist * unit_yards["kilometers"]
        print(result)
        break
    elif out_unit == 'miles':
        result = dist * unit_yards["miles"]
        print(result)
        break
##########################################################
while in_unit == 'meters':
    if out_unit == 'inches':
        result = dist * unit_meters["inches"]
        print(result)
        break
    elif out_unit == 'foot':
        result = dist * unit_meters["foot"]
        print(result)
        break
    elif out_unit == 'yards':
        result = dist * unit_meters["yards"]
        print(result)
        break
    elif out_unit == 'meters':
        result = dist * unit_meters["meters"]
        print(result)
        break
    elif out_unit == 'kilometers':
        result = dist * unit_meters["kilometers"]
        print(result)
        break
    elif out_unit == 'miles':
        result = dist * unit_meters["miles"]
        print(result)
        break
 ######################################################
while in_unit == 'kilometers':
    if out_unit == 'inches':
        result = dist * unit_kilometers["inches"]
        print(result)
        break
    elif out_unit == 'foot':
        result = dist * unit_kilometers["foot"]
        print(result)
        break
    elif out_unit == 'yards':
        result = dist * unit_kilometers["yards"]
        print(result)
        break
    elif out_unit == 'meters':
        result = dist * unit_kilometers["meters"]
        print(result)
        break
    elif out_unit == 'kilometers':
        result = dist * unit_kilometers["kilometers"]
        print(result)
        break
    elif out_unit == 'miles':
        result = dist * unit_kilometers["miles"]
        print(result)
        break
###########################################################
while in_unit == 'miles':
    if out_unit == 'inches':
        result = dist * unit_miles["inches"]
        print(result)
        break
    elif out_unit == 'foot':
        result = dist * unit_miles["foot"]
        print(result)
        break
    elif out_unit == 'yards':
        result = dist * unit_miles["yards"]
        print(result)
        break
    elif out_unit == 'meters':
        result = dist * unit_miles["meters"]
        print(result)
        break
    elif out_unit == 'kilometers':
        result = dist * unit_miles["kilometers"]
        print(result)
        break
    elif out_unit == 'miles':
        result = dist * unit_miles["miles"]
        print(result)
        break