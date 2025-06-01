import json

def generate_e_hallway_locations(
    start_section=2,
    end_section=40,
    slot_bottom_height=0,
    slot_height=1.46,
    sub_locations=(21, 25, 29),
    locations_map=None
):
    if locations_map is None:
        locations_map = {21: 11, 25: 15, 29: 19} # mapping for second floor locations

    locations = []
    for section in range(start_section, end_section + 1):
        pick_side = "Left" if section % 2 == 0 else "Right"

        for location in sub_locations:
            location_tag = f"E.{section:02d}.{location}"

            agv_suf = locations_map.get(location, location)
            agv_location = f"E {section:02d}{agv_suf:02d}"

            locations.append({
                "location_tag":        location_tag,
                "pick_side":           pick_side,
                "slot_bottom_height":  slot_bottom_height,
                "slot_height":         slot_height,
                "pallet_type":         "EURShort",
                "pallet_incline":      0,
                "agv_location":        agv_location
            })
    return locations

def main():
    data = generate_e_hallway_locations(2, 40)

    file_name = "E-hallway-test.json"

    with open(f"json_files/{file_name}", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()
