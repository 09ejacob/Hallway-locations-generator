import json
import os
import sys

def load_config(path="config.json"):
    if not os.path.isfile(path):
        print(f"Error: configuration file '{path}' not found.")
        sys.exit(1)

    try:
        with open(path, "r", encoding="utf-8") as f:
            cfg = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: could not parse '{path}' as JSON:\n{e}")
        sys.exit(1)

    cfg.setdefault("hallway_name", "A")
    cfg.setdefault("start_section", 2)
    cfg.setdefault("end_section", 3)
    cfg.setdefault("second_floor", False)
    cfg.setdefault("slot_bottom_height", 0)
    cfg.setdefault("slot_height", 1.46)
    cfg.setdefault("output_directory", "json_files")
    cfg.setdefault("file_name", "default-hallway.json")

    if not isinstance(cfg["hallway_name"], str):
        print("Error: 'hallway_name' must be a string.")
    if not isinstance(cfg["start_section"], int) or not isinstance(cfg["end_section"], int):
        print("Error: 'start_section' and 'end_section' must be integers.")
        sys.exit(1)
    if not isinstance(cfg["second_floor"], bool):
        print("Error: 'second_floor' must be true or false.")
        sys.exit(1)
    if not isinstance(cfg["slot_bottom_height"], (int, float)) or not isinstance(cfg["slot_height"], (int, float)):
        print("Error: 'slot_bottom_height' and 'slot_height' must be numbers.")
        sys.exit(1)
    if not isinstance(cfg["output_directory"], str) or not isinstance(cfg["file_name"], str):
        print("Error: 'output_directory' and 'file_name' must be strings.")
        sys.exit(1)

    return cfg

def generate_e_hallway_locations(
    hallway_name,
    start_section,
    end_section,
    second_floor,
    slot_bottom_height,
    slot_height
):
    if not second_floor:
        sub_locations = (11, 15, 19)
    else:
        sub_locations = (11, 15, 19, 21, 25, 29)

    locations_map = {21: 11, 25: 15, 29: 19}

    locations = []
    for section in range(start_section, end_section + 1):
        pick_side = "Left" if (section % 2 == 0) else "Right"

        for loc in sub_locations:
            location_tag = f"{hallway_name}.{section:02d}.{loc}"

            mapped = locations_map.get(loc, loc)
            agv_location = f"{hallway_name} {section:02d}{mapped:02d}"

            locations.append({
                "location_tag":       location_tag,
                "pick_side":          pick_side,
                "slot_bottom_height": slot_bottom_height,
                "slot_height":        slot_height,
                "pallet_type":        "EURShort",
                "pallet_incline":     0,
                "agv_location":       agv_location
            })

    return locations

def main():
    # 1) Load config from disk
    cfg = load_config("config.json")

    hallway_name = cfg["hallway_name"]
    start_section = cfg["start_section"]
    end_section = cfg["end_section"]
    second_floor = cfg["second_floor"]
    slot_bottom_height = cfg["slot_bottom_height"]
    slot_height = cfg["slot_height"]
    out_dir = cfg["output_directory"]
    file_name = cfg["file_name"]

    # 2) Generate the data list
    data = generate_e_hallway_locations(
        hallway_name,
        start_section,
        end_section,
        second_floor,
        slot_bottom_height,
        slot_height
    )

    # 3) Ensure the output directory exists
    os.makedirs(out_dir, exist_ok=True)

    # 4) Write JSON
    output_path = os.path.join(out_dir, file_name)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Generated '{output_path} with {len(data)} entries.")


if __name__ == "__main__":
    main()
