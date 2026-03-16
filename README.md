# Movement Language Discovery System

An interactive installation that captures human movement in real time,
matches it to a taxonomy of universal movement archetypes, and
surfaces cultural context from a community-controlled local database.

Built as Part 2 of a two-part thesis project at George Brown College.
Part 1 is a companion offline RAG system for querying cultural movement knowledge.

## Project Status

Work in progress — Spring 2026.

## System Overview

1. User performs a movement in front of a camera
2. MediaPipe captures skeletal joint coordinates in real time
3. A rule-based matcher compares the movement to 15 universal archetypes
4. The closest match is displayed with a confidence score and cultural context

## Architecture
```
capture/      — MediaPipe webcam capture and joint extraction
matcher/      — Rule-based archetype matching engine
database/     — SQLite schema, seed data, and query layer
interface/    — FastAPI backend and HTML/CSS/JS frontend
```

## Movement Archetypes

15 universal archetypes drawn from Laban Movement Analysis (LMA):
rise_and_sink, open_and_close, reach, collapse, percussive_strike,
sustained_flow, bound_freeze, axial_rotation, weight_shift,
advance_and_retreat, swing, spiral_unwind, vibration_tremble,
circling_orbit, mirror_symmetry.

## Stack

- Python 3.12
- MediaPipe 0.10.21 (skeletal capture)
- SQLite (local database)
- FastAPI + Uvicorn (web interface)
- HTML/CSS/JS (frontend)

## Hardware

- Development: MacBook Pro (CPU only, no GPU)
- Deployment target: Raspberry Pi 5 8GB

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python database/seed.py
```

## Design Principles

- Offline-first: no data leaves the device
- Community sovereignty: cultural content requires explicit partnership
  and consent before ingestion
- Transparent matching: every result shows a confidence score
- POC scope: universal archetypes only — cultural specificity follows
  community partnership
