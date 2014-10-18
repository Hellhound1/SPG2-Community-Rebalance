# Community Rebalance Mod
# Commodity Reading Tool
# By Valeroth
# 

import sys
import os

# This is where the file was on my machine,  you'll like have to adjust it.
write_file = file("E:\\Games\\Steam\\steamapps\\common\\Starpoint Gemini 2\\Spg2\\World\\Sectors\\commodity_output.csv", "w")
write_file.write("Sector,XPosition,YPosition,ZPosition,KeyName,MaxCargo,Ice, , ,Carbon, , ,Fluorine, , ,Iodine, , ,Sulfur, , ,Phosphorous, , ,Magnesium, , ,Copper, , ,Iron, , ,Silicon, , ,Aluminum, , ,Silver, , ,Granite, , ,Gold, , ,Titanium, , ,Thorium, , ,Tellurium, , ,Uranium, , ,Plutonium, , ,Diamond, , ,Crystal, , ,Shard, , ,Hydrogen, , ,Nitrogen, , ,Oxygen, , ,Helium, , ,Argon, , ,Neon, , ,Xenon, , ,Ionized_gas, , ,Spices, , ,Sea_algae, , ,Fish, , ,Meat, , ,Vegetables, , ,Crops, , ,Soyfood, , ,Protein_bars, , ,Tark_leaves, , ,Hogwash, , ,Thaurian_weed, , ,Squibb_tentacles, , ,Nyxian_ale, , ,Vantus_eggs, , ,Ammartan_algae, , ,Rift_dust, , ,Wood, , ,Leather, , ,Steel, , ,Aluminum_foils, , ,Industrial_polymers, , ,Rubber, , ,UniGlass, , ,TitaNova_plates, , ,Bioplastics, , ,Textile, , ,Arachos_silk, , ,Scarab_husk, , ,Brunt_tusk, , ,Brunt_fur, , ,Shell_casings, , ,Holo_projectors, , ,Explosives, , ,Infused_core, , ,Crystal_matrix, , ,Superconductors, , ,Bio-circuitry, , ,Engine_parts, , ,Vehicle_components, , ,AntiGrav_coils, , ,Air_filters, , ,Photocells, , ,Thorium_shells, , ,Energy_cells, , ,Plasma_charges, , ,Thrusters, , ,Prefab_shelters, , ,Clothes, , ,Surgical_equipment, , ,Solar_panels, , ,Envirosuits, , ,Oxygen_recyclers, , ,Computers, , ,Hologames, , ,Mining_charges, , ,ATR_-_All-terrain_rovers, , ,Furniture, , ,Fertilizers, , ,Medicines, , ,Prosthetics, , ,Laser_sidearm, , ,Plasma_rifles, , ,Heavy_weapons, , ,X900_Personal_armor, , ,Oxygen_tanks, , ,Station_composites, , ,Fuel, , ,Hydroponics_pod, , ,Utility_droids, , ,Cybernet_implants, , ,Shard_blades, , ,Combat_mechs\n")

sector = 0
while sector < 340:
    sectorfile = "Sector_"+ str(sector) + ".ics"
    read_file = file(os.path.join("E:\\Games\\Steam\\steamapps\\common\\Starpoint Gemini 2\\Spg2\\World\\Sectors", sectorfile))
    file_contents = list(read_file.readlines())
    lines = len(file_contents)
    print "Read in", lines, "lines from", sectorfile

    line_location = 0
    for line_check in file_contents:
        if "Station:" in line_check:
            # print "Station Found!"
            position = line_location + 3
            keyname = line_location + 5
            maxcargo = line_location + 10
            commodities = line_location + 19
            xpos = file_contents[position].split()[1]
            ypos = file_contents[position].split()[2]
            zpos = file_contents[position].split()[3]
            keyn = file_contents[keyname].split()[1]
            maxc = file_contents[maxcargo].split()[1]
            carc = file_contents[commodities].replace("\t",",")
            write_file.write(str(sector)+","+xpos+","+ypos+","+zpos+","+keyn+","+maxc+carc)
        line_location = line_location + 1
    sector = sector + 1

# Now for Planets
planet_file = file("E:\\Games\\Steam\\steamapps\\common\\Starpoint Gemini 2\\Spg2\\World\\World.ics")
file_contents = list(planet_file.readlines())
lines = len(file_contents)
print "Read in", lines, "lines from World.ics"
line_location = 0
for line_check in file_contents:
    if "Planet:" in line_check:
        # print "Station Found!"
        position = line_location + 3
        keyname = line_location + 5
        # Do planets not have a max cargo?
        maxcargo = "???"
        commodities = line_location + 15
        xpos = file_contents[position].split()[1]
        ypos = file_contents[position].split()[2]
        zpos = file_contents[position].split()[3]
        keyn = file_contents[keyname].split()[1]
        maxc = "???"
        carc = file_contents[commodities].replace("\t",",")
        sector = "???"
        write_file.write(sector+","+xpos+","+ypos+","+zpos+","+keyn+","+maxc+carc)
    line_location = line_location + 1
    
write_file.close()
