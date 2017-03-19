"""Inspiration for this code comes from shortcutfoo.com. 
This is a free version for personal use."""

import pickle
import time
import random

class ninja_training:

    def __init__(self, dojo_name):

        self.time_per_answer = 15
        self.dojo_name = dojo_name

        # Directory name from where to load/save the scores
        self.scores_dir = 'scores/' + dojo_name + '.pkl'

        # Get shortcut commands and meanings
        self.commands = {}
        with open('shortcuts/' + dojo_name + '.txt') as f:
            for line in f:
                command, meaning = line.rstrip().split('  ')
                self.commands[command] = meaning

        # Get dictionary with the scores for each command. Create a new empty
        # scores dict if no scores list is found. The value of each score is a
        # list containing: the total number of correct answers, total time to
        # answer, number of times asked
        try:
            with open(self.scores_dir, 'rb') as f:
                self.scores_dict = pickle.load(f)
        except FileNotFoundError:
            self.scores_dict = {command:[0,0,0] for command in self.commands}
        self.save_scores()

    def save_scores(self):
        with open(self.scores_dir, 'wb') as f:
            pickle.dump(self.scores_dict, f)

    @staticmethod
    def clean_terminal(number_of_lines):
        for i in range(number_of_lines):
            print('\033[F' + ' '*79 + '\r', end='')

    def test_command(self, command):

        start_time = time.time()
        meaning = self.commands[command]

        # Ask command for operation
        answered_command = input('{}: '.format(meaning))

        # Evaluate answer
        if answered_command == 'quit':
            quit()
        is_correct = (command == answered_command)
        answer_time = time.time() - start_time
        if not is_correct:
            qualifier = 'Wrong!'
        elif answer_time > self.time_per_answer:
            qualifier = 'Too slow!'
        else:
            qualifier = 'Correct!'

        # Update and save the score statistics for the command
        score = self.scores_dict[command]
        score[0] += int(is_correct) 
        score[1] += min(answer_time, self.time_per_answer)
        score[2] += 1
        self.save_scores()

        # Give output on the answered command
        self.clean_terminal(2)
        output = meaning + '. Answer: ' +  answered_command
        output += '. True: ' + command
        output = '{:<70}'.format(output)
        print(output + '{:>9}'.format(qualifier))

    def __str__(self):
        scores = self.scores_dict.values()
        correct_pct = sum(score[0] for score in scores)/(sum(score[2] for score
            in scores) + 0.000001)*100
        return ('\nEntering the dojo of {}.\n'
        'You have a white belt for this dojo!\n'
        'Percentage of correct commands: {:2.2f}%'.format(self.dojo_name,
            correct_pct))

    def train(self):
        print(self)
        input('Press enter to start training')
        print('\n' + '-'*79)
        answer = None
        while answer != 'quit':
            command = random.choice(list(self.commands))
            self.test_command(command)

    def rewards():
        pass

if __name__ == '__main__':

    print('Welcome to Code Ninja!')
    dojo_name = input('In which dojo would you like to train? ').lower()
    dojo = ninja_training(dojo_name)
    dojo.train()
