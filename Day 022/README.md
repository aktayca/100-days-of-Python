# Day 22

## Pong

Classic two-player tennis action. Control paddles to volley the ball in this arcade recreation.

A project focused on multi-class interactions and real-time collision handling.

### Features

- Local multiplayer (Right: Up/Down, Left: W/S)
- Realistic ball physics with directional bounces
- Progressive speed increase after paddle hits
- Score tracking with win condition at 5 points
- Dynamic center line and real-time court rendering

### Technical Implementation

**Directional Ball Physics:** Modulo-based direction switching using predefined angle tuples for consistent bounces.

**Efficient Collision Detection:** Combined distance checking with coordinate boundaries for optimal paddle detection.

**Game State Management:** Nested loop structure handling round resets while maintaining overall game flow.

**Visual Feedback System:** Temporary text display with automatic cleanup for scoring announcements.

![Pong Screenshot](images/pong.png)
