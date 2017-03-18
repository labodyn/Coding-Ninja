"""Inspiration for this code comes from shortcutfoo.com. 
This is a free version for personal use."""

import pickle
import time
import random

class dojo_training:

    def __init__(self, dojo_name):
        self.dojo_name = dojo_name.lower()
        self.scores_dir = 'scores/' + self.dojo_name + '.pkl'

        # Get shortcuts
        self.commands = []
        self.meanings = []
        with open('shortcuts/' + self.dojo_name + '.txt') as f:
            for line in f:
                command, meaning = line.split('  ')
                self.commands.append(command)
                self.meanings.append(meaning)

        # Get past scores in the commands
        try:
            with open(self.scores_dir) as f:
                self.scores_list = pickle.load(f)
        except FileNotFoundError:
            scores_list = [0 for _ in range(len(self.commands))]

        self.scores = dict()

    def update_scores():
        with open(self.scores_dir) as f:
            pass

    def test_shortcut():
        pass

    def train(self):
        pass

    def rewards():
        pass

if __name__ == '__main__':

    print('Welcome to Code Ninja!')
    dojo_name = input('In which dojo would you like to train? ')
    dojo = dojo_training(dojo_name)
    dojo.train()
