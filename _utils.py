import functools
import traceback
import subprocess

def catch_exception(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            args[0].log(traceback.format_exc())
    return func

def is_module(track):
    return track.name.startswith('M[')

def is_aux_instrument(track):
    return track.name.startswith('IA')

def is_instrument(track):
    return track.name.startswith('I[') or is_aux_instrument(track) or is_module_fx(track)

def is_input(track):
    return '_IN' in track.name

def set_input_routing(track, routing_name):
    for routing in track.available_input_routing_types:
        if routing.display_name == routing_name:
            track.input_routing_type = routing
            return

def is_loop_track(track):
    return track.name == 'LOOP'

def get_loop_key(name):
    return name[len('loop['):-len(']')]

def set_output_routing(track, routing_name):
    for routing in track.available_output_routing_types:
        if routing.display_name == routing_name:
            track.output_routing_type = routing

def is_loop_scene(scene):
    return 'loop' in scene.name

def is_clip_scene(scene):
    return scene.name.startswith('CLIP')

def is_midi_router(track):
    return 'MIDI_ROUTER' in track.name

def is_audio_router(track):
    return 'AUDIO_ROUTER' in track.name

def strip_name_params(name):
    if name.find('[') != -1:
        return name[0:name.find('[')].strip()
    return name

def is_empty_clip(clip):
    if clip.is_midi_clip:
        clip.select_all_notes()
        if len(clip.get_selected_notes()) > 0 or clip.has_envelopes:
            return False
    if clip.is_audio_clip:
        return False
    return True

def is_clip_track(track):
    return track.name == 'CLIP'

def is_module_fx(track):
    return track.name.startswith('MFX')

def is_gfx(track):
    return track.name.startswith('GFX')

def is_record(track):
    return track.name == 'RECORD'

def is_midi_input(track, midi_input_names):
    return track.name.replace('_IN','') in midi_input_names and track.has_midi_output

def is_audio_input(track, audio_input_names):
    return track.name.replace('_IN','') in audio_input_names and track.has_audio_output

color_index_map = {
    9: 'blue',
    12: 'pink',
    39: 'lavender',
    56: 'red',
    61: 'green',
    69: 'maroon',
    13: 'white',
    59: 'gold',
    1: 'orange',
    20: 'teal',
    24: 'purple',
    55: 'white'
}

def color_name(index):
    return color_index_map[index]

row1 = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', 'equal'
]
row2 = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'lb', 'rb'
]
row3 = [
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'semi', 'apos'
]
row4 = [
    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', 'slash'
]
rows = [row1, row2, row3, row4]

def on_same_row(loop_name1, loop_name2):
    for row in rows:
        if loop_name1 in row and loop_name2 in row:
            return True
    return False







# def is_cbord_in(track):
#     return track.name == 'CBORD_IN'

# def is_as_in(track):
#     return track.name == 'AS_IN'

# def is_nanok_in(track):
#     return track.name == 'NANOK_IN'
    


# def is_instr(track):
#     return track.name == 'INSTR'

# def index_of_loop_scene(name, scenes):
#     i = 0
#     for scene in scenes:
#         if 'loop[' + name + ']' == scene.name:
#             return i

# def is_locked(clip):
#     return 'lock' in clip.name



# def set_output_routing(track, routing_name):
#     for routing in track.available_output_routing_types:
#         if routing.display_name == routing_name:
#             track.output_routing_type = routing

# # def is_mpe_track(track):
# #     return 'MPE' in track.input_routing_type.display_name

# def set_mpe_output_router(track):
#     router = int(track.input_routing_type.display_name.replace('_IN','')[-1])
#     if track.available_output_routing_routers[router+1]:
#         track.output_routing_router = track.available_output_routing_routers[router+1]

# def is_metronome(track):
#     return track.name == 'METRO'


