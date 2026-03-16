import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "movement.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(SCHEMA_PATH, "r") as f:
        cursor.executescript(f.read())

    archetypes = [
        {
            "name": "rise_and_sink",
            "body_locus": "full_body",
            "action_type": "elevation_change",
            "effort_quality": "sustained",
            "description": "Full body rises or sinks through vertical space.",
            "matching_rules": json.dumps({
                "primary_joint": "hip",
                "direction": "vertical",
                "min_displacement_cm": 10,
                "max_velocity_ms": 0.8
            })
        },
        {
            "name": "open_and_close",
            "body_locus": "arms_torso",
            "action_type": "shape_change",
            "effort_quality": "light",
            "description": "Arms and torso expand outward or contract inward.",
            "matching_rules": json.dumps({
                "primary_joint": "wrist",
                "direction": "horizontal",
                "min_displacement_cm": 20,
                "max_velocity_ms": 1.0
            })
        },
        {
            "name": "reach",
            "body_locus": "arm_hand",
            "action_type": "extension",
            "effort_quality": "light",
            "description": "One or both arms extend away from the body centre.",
            "matching_rules": json.dumps({
                "primary_joint": "wrist",
                "direction": "any",
                "min_displacement_cm": 25,
                "max_velocity_ms": 1.2
            })
        },
        {
            "name": "collapse",
            "body_locus": "full_body",
            "action_type": "yield_to_gravity",
            "effort_quality": "sudden",
            "description": "Body yields to gravity, losing vertical support.",
            "matching_rules": json.dumps({
                "primary_joint": "hip",
                "direction": "downward",
                "min_displacement_cm": 15,
                "max_velocity_ms": 2.5
            })
        },
        {
            "name": "percussive_strike",
            "body_locus": "limbs_feet",
            "action_type": "impact",
            "effort_quality": "sudden_strong",
            "description": "A limb or foot makes sudden strong impact.",
            "matching_rules": json.dumps({
                "primary_joint": "wrist",
                "direction": "any",
                "min_displacement_cm": 10,
                "min_velocity_ms": 2.0
            })
        },
        {
            "name": "sustained_flow",
            "body_locus": "full_body",
            "action_type": "continuous",
            "effort_quality": "sustained_free",
            "description": "Body moves continuously without pause or accent.",
            "matching_rules": json.dumps({
                "primary_joint": "hip",
                "direction": "any",
                "min_duration_sec": 2.0,
                "max_velocity_ms": 0.6
            })
        },
        {
            "name": "bound_freeze",
            "body_locus": "full_body",
            "action_type": "stillness",
            "effort_quality": "bound",
            "description": "Body holds completely still with intentional tension.",
            "matching_rules": json.dumps({
                "primary_joint": "hip",
                "direction": "none",
                "max_displacement_cm": 3,
                "min_duration_sec": 1.5
            })
        },
        {
            "name": "axial_rotation",
            "body_locus": "spine",
            "action_type": "twist",
            "effort_quality": "strong",
            "description": "Body rotates around its vertical axis.",
            "matching_rules": json.dumps({
                "primary_joint": "shoulder",
                "direction": "rotational",
                "min_angle_deg": 30,
                "max_velocity_ms": 1.5
            })
        },
        {
            "name": "weight_shift",
            "body_locus": "lower_body",
            "action_type": "transfer",
            "effort_quality": "strong",
            "description": "Weight transfers from one foot or side to another.",
            "matching_rules": json.dumps({
                "primary_joint": "hip",
                "direction": "lateral",
                "min_displacement_cm": 8,
                "max_velocity_ms": 1.0
            })
        },
        {
            "name": "advance_and_retreat",
            "body_locus": "full_body",
            "action_type": "locomotion",
            "effort_quality": "sudden",
            "description": "Body moves forward toward or backward away from a point.",
            "matching_rules": json.dumps({
                "primary_joint": "hip",
                "direction": "sagittal",
                "min_displacement_cm": 20,
                "max_velocity_ms": 2.0
            })
        },
        {
            "name": "swing",
            "body_locus": "limbs",
            "action_type": "pendular",
            "effort_quality": "sustained_free",
            "description": "A limb swings through space driven by gravity and momentum.",
            "matching_rules": json.dumps({
                "primary_joint": "wrist",
                "direction": "arc",
                "min_displacement_cm": 20,
                "max_velocity_ms": 2.0
            })
        },
        {
            "name": "spiral_unwind",
            "body_locus": "spine_limbs",
            "action_type": "sequential",
            "effort_quality": "sustained",
            "description": "Movement sequences through the spine and limbs in a spiral path.",
            "matching_rules": json.dumps({
                "primary_joint": "shoulder",
                "direction": "rotational",
                "min_angle_deg": 45,
                "max_velocity_ms": 1.0
            })
        },
        {
            "name": "vibration_tremble",
            "body_locus": "local_body_part",
            "action_type": "oscillation",
            "effort_quality": "quick_light",
            "description": "A body part oscillates rapidly with small amplitude.",
            "matching_rules": json.dumps({
                "primary_joint": "wrist",
                "direction": "any",
                "min_frequency_hz": 3.0,
                "max_displacement_cm": 5
            })
        },
        {
            "name": "circling_orbit",
            "body_locus": "full_body_path",
            "action_type": "locomotion",
            "effort_quality": "sustained",
            "description": "Body travels in a circular path through space.",
            "matching_rules": json.dumps({
                "primary_joint": "hip",
                "direction": "circular",
                "min_displacement_cm": 30,
                "max_velocity_ms": 1.5
            })
        },
        {
            "name": "mirror_symmetry",
            "body_locus": "bilateral_body",
            "action_type": "simultaneous",
            "effort_quality": "varies",
            "description": "Both sides of the body perform identical simultaneous movement.",
            "matching_rules": json.dumps({
                "primary_joint": "wrist",
                "direction": "any",
                "symmetry_threshold": 0.85,
                "min_displacement_cm": 15
            })
        }
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO movement_archetype
        (name, body_locus, action_type, effort_quality, description, matching_rules)
        VALUES (:name, :body_locus, :action_type, :effort_quality, :description, :matching_rules)
    """, archetypes)

    conn.commit()
    conn.close()
    print(f"Database created at {DB_PATH}")
    print(f"{len(archetypes)} archetypes seeded.")

if __name__ == "__main__":
    create_database()