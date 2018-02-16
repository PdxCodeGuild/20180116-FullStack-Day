#Version 1
# ft = input('How many feet do you want to convert to metric?')
# x = int(ft)
# y = x*0.3048
# output = 'That is ' + str(y) + ' meters.'
# print(output)

#Version 2+3
#Allow the user to also enter the units. Then depending on the units, convert the distance into meters.
# The units we'll allow are feet, miles, meters, and kilometers.
#           0       1       2           3
# units = ['feet', 'miles', 'meters', 'kilometers', 'yards', 'inches']
# unit = input("Enter the type of unit you wish to convert from (Feet, Miles, Meters, Kilometers, Yards or Inches: ")
# convertto = input('Enter the type of unit you wish to convert to : ')
# convertvalue = float(input('Enter the amount you wish to convert: '))
# #Feet conversion formulas
# fttm = str(convertvalue*0.3048)
# fttmi = str(convertvalue*0.000189394)
# fttkm = str(convertvalue*0.0003048)
# ftty = str(convertvalue*0.333333)
# fttin =str(convertvalue*12)
# #Mile conversion formulas
# mitft = str(convertvalue*5280)
# mitm = str(convertvalue*1609.34)
# mitkm = str(convertvalue*1.60934)
# mity = str(convertvalue*1760)
# mitin = str(convertvalue*63360)
# #Meter conversion Formulas
# mtft = str(convertvalue*3.28084)
# mtmi = str(convertvalue*0.000621371)
# mtkm = str(convertvalue*0.001)
# mty = str(convertvalue*1.09361)
# mtin = str(convertvalue*0.000015783)
# #Kilometer conversion formulas
# kmtm = str(convertvalue*1000)
# kmtft = str(convertvalue*3280.84)
# kmtmi = str(convertvalue*0.621371)
# kmty = str(convertvalue*1093.61)
# kmtin = str(convertvalue*39370.1)
# #Yard conversion formulas
# ytft = str(convertvalue*3)
# ytm = str(convertvalue*0.9144)
# ytmi = str(convertvalue*0.000568182)
# ytkm = str(convertvalue*0.0009144)
# ytin =str(convertvalue*36)
# #Inch conversion formulas
# intft = str(convertvalue*0.0833333)
# intm = str(convertvalue*0.0254)
# intmi = str(convertvalue*63360)
# inty = str(convertvalue*0.0277778)
# #intkm =str(convertvalue*) Cannot find decimal equivalent.
# #Math statements for feet
# if unit == units[0] and convertto == units[1]:
#     print(f"That would be {fttmi}mi.")
# if unit == units[0] and convertto == units[2]:
#     print(f"That would be {fttm}m.")
# if unit == units[0] and convertto == units[3]:
#     print(f"That would be {fttkm}km.")
# if unit == units[0] and convertto == units[4]:
#     print(f"That would be {ftty}yrd.")
# if unit == units[0] and convertto == units[5]:
#     print(f"That would be {fttin}in.")
#     # Math statements for miles
# if unit == units[1] and convertto == units[0]:
#     print(f"That would be {mitft}ft.")
# if unit == units[1] and convertto == units[2]:
#     print(f"That would be {mitm}m.")
# if unit == units[1] and convertto == units[3]:
#     print(f"That would be {mitkm}km.")
# if unit == units[1] and convertto == units[4]:
#     print(f"That would be {mity}yrd.")
# if unit == units[1] and convertto == units[5]:
#     print(f"That would be {mitin}in.")
#
#     #Math statements for meters
# if unit == units[2] and convertto == units[0]:
#     print(f"That would be {mtft}ft.")
# if unit == units[2] and convertto == units[1]:
#     print(f"That would be {mtmi}mi.")
# if unit == units[2] and convertto == units[3]:
#     print(f"That would be {mtkm}km.")
# if unit == units[2] and convertto == units[4]:
#     print(f"That would be {mty}yrd.")
# if unit == units[2] and convertto == units[5]:
#     print(f"That would be {mtin}in.")
#
#     #Math statements for kilometers
# if unit == units[3] and convertto == units[0]:
#     print(f"That would be {kmtft}ft.")
# if unit == units[3] and convertto == units[1]:
#     print(f"That would be {kmtmi}mi.")
# if unit == units[3] and convertto == units[2]:
#     print(f"That would be {kmtm}m.")
# if unit == units[3] and convertto == units[4]:
#     print(f"That would be {kmty}yrd.")
# if unit == units[3] and convertto == units[5]:
#     print(f"That would be {kmtin}in.")
#
#     #Math statements for Yards
# if unit == units[4] and convertto == units[0]:
#     print(f"That would be {ytft}ft.")
# if unit == units[4] and convertto == units[1]:
#     print(f"That would be {ytmi}mi.")
# if unit == units[4] and convertto == units[2]:
#     print(f"That would be {ytm}m.")
# if unit == units[4] and convertto == units[3]:
#     print(f"That would be {ytkm}km.")
# if unit == units[4] and convertto == units[5]:
#     print(f"That would be {ytin}in.")
#
#     #Math statements for inches
# if unit == units[5] and convertto == units[0]:
#     print(f"That would be {intft}ft.")
# if unit == units[5] and convertto == units[1]:
#     print(f"That would be {intmi}mi.")
# if unit == units[5] and convertto == units[2]:
#     print(f"That would be {intm}m.")
# # if unit == units[5] and convertto == units[3]:
# #     print(f"That would be {intkm}km.")
# if unit == units[4] and convertto == units[4]:
#     print(f"That would be {inty}y.")

#Version 4
#convert from the input units to meters, then convert from meters to the output units


units = ['feet', 'miles', 'meters', 'kilometers']
distance = float(input('What is the distance? '))
unitin = input('Are the input units in Feet, Miles, Meters, or Kilometers? ').lower()
unitout = input('What are the output units? ').lower()

ftm = distance*0.3048
mitm = distance*1609.34
# mtm = distance*1
kmtm = distance*1000
conv = {"feet": 0.3048, "miles": 1609.34, "meters": 1, "kilometers": 1000}

if unitin == 'meters' and unitout in units:
    distance = distance/conv[unitout]
elif unitin != 'meters' and unitin in units and unitout in units:
    distance = distance*conv[unitin]
    distance = distance/conv[unitout]

#
# mtf = convert_to_meters[0]*3.28084
# mtmi = convert_to_meters[1]*0.000621371
# mtkm = convert_to_meters[3]*0.001
# convert_from_meters = {}

# if unitin == 'feet' and unitout == 'meters':
#     print(f"That is {convert_to_meters[0]} {unitout}.")
# if unitin == 'miles' and unitout == 'meters':
#     print(f"That is {convert_to_meters[1]} {unitout}.")
# if unitin == 'kilometers' and unitout == 'meters':
#     print(f"That is {convert_to_meters[2]} {unitout}.")


