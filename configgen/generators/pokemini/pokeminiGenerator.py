#!/usr/bin/env python
import Command
import recalboxFiles
import shutil
from generators.Generator import Generator
import os.path

class PokeminiGenerator(Generator):
    # Main entry of the module
    # Configure pokemini and return a command
    def generate(self, system, rom, playersControllers):
        # Settings recalbox default config file if no user defined one
        

        commandArray = [recalboxFiles.pokeminiBin]
