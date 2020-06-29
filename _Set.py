from threading import Timer
from ClyphX_Pro.clyphx_pro.UserActionsBase import UserActionsBase
from _utils import catch_exception, is_module
from _Module import Module

class Set(UserActionsBase):

    def __init__(self, ActionsBase):
        self.base = ActionsBase
        self.tracks = list(self.base.song().tracks)
        self.scenes = list(self.base.song().scenes)
        self.modules = []
        self.active_module = None

        self.log('Building virtual set...')

        #TODO make inputs dynamic
        self.midi_inputs = ['CBORD', 'AS', 'NANOK']
        self.audio_inputs = ['LINE']
        self.held_inputs = set([])

        for track in self.tracks:
            if is_module(track):
                self.modules.append(Module(track, self))

        self.activate_module(0)


    def activate_module(self, index):
        if self.modules[index]:
            if self.modules[index] != self.active_module:
                if self.active_module:
                    self.active_module.stop_all_loops()
                for module in self.modules:
                    module.deactivate()
                self.modules[index].activate()
                self.active_module = self.modules[index]
            else:
                self.log('Module already active')
        else:
            self.log('Module index out of bounds')

    def select_input(self, name):
        self.held_inputs.add(name)

    def deselect_input(self, name):
        self.held_inputs.remove(name)

    def toggle_input(self, name):
        self.active_module.toggle_input(name)

    def clear_module(self, index):
        if self.modules[index]:
            self.modules[index].clear_all_loops()

    def log(self, message):
        self.base.canonical_parent.log_message(message)