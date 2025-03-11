# Set Render Range

Plugin for [Autodesk Flame software](http://www.autodesk.com/products/flame).

Set the render range on the selected Render or Write nodes to the current frame.

## Installation

### Flame 2025 and newer
To make available to all users on the workstation, copy `set_render_range.py` to `/opt/Autodesk/shared/python/`

For specific users, copy `set_render_range.py` to the appropriate path below...
|Platform|Path|
|---|---|
|Linux|`/home/<user_name>/flame/python/`|
|Mac|`/Users/<user_name>/Library/Preferences/Autodesk/flame/python/`|

### Flame 2022 up to 2024.2
To make available to all users on the workstation, copy `set_render_range.py` to `/opt/Autodesk/shared/python/`

For specific users, copy `set_render_range.py` to `/opt/Autodesk/user/<user name>/python/`

### Last Step
Finally, inside of Flame, go to Flame (fish) menu `->` Python `->` Rescan Python Hooks

## Menus
- Right-click selected nodes in the Batch schematic `->` Edit... `->` Set Render Range to Current Frame

## Acknowledgements
Many thanks to [pyflame.com](http://www.pyflame.com)
