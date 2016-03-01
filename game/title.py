import pyglet

import level
import worlds
import graphics

# Click events
def on_story_mode_click():
    worlds.worlds[1]["1"].play()

def on_instructions_click():
    area = level.get_current_level().areas[1]
    area.play()

def on_story_click():
    pass

def on_exit_click():
    level.get_current_level().end()
    
    pyglet.app.exit()
    for window in pyglet.app.windows:
        window.close()
