# Hallway-locations-generator
Hallway locations generator for a warehouse

## User guide
You can configure the settings for the hallway locations generator in the config.json file found in the root of the repository. 

There are a few options to explain in the config.json file:
1. **hallway_name** - name of the hallway which will be in the start of each location.
2. **start_section** - from which location the program will start generating locations.
3. **end_section** - where the program will stop generating locations.
4. **second_floor** - if the program will generate second floor locations. This will generate a duplicate of each location with appropriate location tags.
5. **slot_bottom_height** - the height of the bottom of the first floor locations.
6. **slot_height** - the height of the first floor locations.
7. **slot_bottom_height_floor_2** - the height of the bottom of the second floor locations (if there is a second floor).
8. **slot_height_floor_2** - the height of the second floor locations (if there is a second floor).
9. **flip_pick_side** - flip the pick side so that the pick side is on the right side instead of the left side for even numbered locations and opposite for odd numbered locations.
10. **exclude_sections** - exclude specific sections by entering the locations to exclude in a list. For example if you want to exclude X.12.11, X.12.15, and X.12.19, just add *12* to the list.
11. **output_directory** - where to save the generated json file.
12. **file_name** - the name of the generated json file.

After configuring the config.json file, run the main.py file and it will generate a json file with the desired locations.

##Extra:
The locations will be created in a format like this:
```
{
    "location_tag": "A.02.11",
    "pick_side": "Left",
    "slot_bottom_height": 0,
    "slot_height": 1.46,
    "pallet_type": "EURShort",
    "pallet_incline": 0,
    "agv_location": "A 0211"
}
```
