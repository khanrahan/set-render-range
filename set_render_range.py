"""
Script Name: Set Render Range
Written By: Kieran Hanrahan

Script Version: 2.0.0
Flame Version: 2022

URL: http://github.com/khanrahan/set-render-range

Creation Date: 02.05.24
Update Date: 02.05.24

Description:

    Set render range of selected Render or Write File nodes to the current frame.

Menus:

    Right-click selected nodes in the Batch schematic --> Edit... -> Set Render Range to
    Current Frame

To Install:

    For all users, copy this file to:
    /opt/Autodesk/shared/python

    For a specific user, copy this file to:
    /opt/Autodesk/user/<user name>/python
"""

import flame

TITLE = 'Set Render Range'
VERSION_INFO = (2, 0, 0)
VERSION = '.'.join([str(num) for num in VERSION_INFO])
TITLE_VERSION = f'{TITLE} v{VERSION}'
MESSAGE_PREFIX = '[PYTHON]'


def message(string):
    """Print message to shell window and append global MESSAGE_PREFIX."""
    print(' '.join([MESSAGE_PREFIX, string]))


def set_to_current_frame(selection):
    """Set From & To values of the Render Range to be the current frame."""
    message(TITLE_VERSION)
    message(f'Script called from {__file__}')

    frame = flame.batch.current_frame

    for node in selection:
        node.range_start = frame
        node.range_end = frame
        message(f'{node.name.get_value()} set to only render frame {frame}')

    message('Done!')


def scope_output_node(selection):
    """Filter for only Render or Write File nodes."""
    valid_objects = (
            flame.PyRenderNode,
            flame.PyWriteFileNode,
    )

    return all(isinstance(item, valid_objects) for item in selection)


def get_batch_custom_ui_actions():
    """Python hook to add custom right click menu item."""
    return [{'name': 'Edit...',
             'actions': [{'name': 'Set Render Range to Current Frame',
                          'isVisible': scope_output_node,
                          'execute': set_to_current_frame,
                          'minimumVersion': '2022.0.0.0'}]
            }]
