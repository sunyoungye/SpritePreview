# Sprite Animation Preview Tool
This project is a desktop sprite animation preview tool built in Python using PyQt6, designed to visualize sprite animations with real-time playback control.

## Overview
The tool allows users to load and preview sprite animations while adjusting playback speed dynamically.
It focuses on event-driven UI design, timer-based animation updates, and clear state management.

## Key Features
- Real-time sprite animation playback
- Adjustable FPS control via slider (1-100 FPS)
- Start / Stop controls for animation playback
- Menu actions for pausing and exiting the application
- Responsive UI updates based on playback state

## Technical Highlights
- Used 'QTimer' to drive frame updates for smooth animation playback
- Implemented event-driven UI logic with PyQt6 widgets and signals
- Managed application state to synchronize UI controls and animation flow 

## Tech Stack
- Python
- PyQt6

## How to Run
Place the sprite_images folder and Sprite.py file into a PyCharm project, then run Sprite.py.
