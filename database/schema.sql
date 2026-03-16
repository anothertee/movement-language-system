CREATE TABLE IF NOT EXISTS movement_archetype (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    body_locus TEXT NOT NULL,
    action_type TEXT NOT NULL,
    effort_quality TEXT NOT NULL,
    source_framework TEXT NOT NULL DEFAULT 'LMA',
    description TEXT,
    matching_rules TEXT
);

CREATE TABLE IF NOT EXISTS cultural_tag (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tradition TEXT NOT NULL,
    region TEXT,
    source_framework TEXT
);

CREATE TABLE IF NOT EXISTS archetype_cultural_expression (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    archetype_id INTEGER NOT NULL,
    cultural_tag_id INTEGER NOT NULL,
    significance TEXT,
    is_contested INTEGER DEFAULT 0,
    FOREIGN KEY (archetype_id) REFERENCES movement_archetype(id),
    FOREIGN KEY (cultural_tag_id) REFERENCES cultural_tag(id)
);