import json
import random
import pickle

class Shlok:
    def __init__(self):
        self.load_shloks()
        self.load_exclude_shloks()
        self.check_full()

    def load_shloks(self):
        with open('shloks.json') as f:
            shloks = json.load(f)
        
        self.shloks = shloks
    def load_exclude_shloks(self):
        try:
            with open('exclude.pkl', 'rb') as f:
                self.exclude_shloks = pickle.load(f)
        except EOFError:
            self.exclude_shloks = []
    
    def check_full(self):
        if self.exclude_shloks.__len__() == 100:
            self.exclude_shloks = []
            with open('exclude.pkl', 'wb') as f:
                pickle.dump(self.exclude_shloks, f)


    def get_shlok(self):
        id = self.generate_random_id()
        self.exclude_shloks.append(id)
        with open('exclude.pkl', 'wb') as f:
            pickle.dump(self.exclude_shloks, f)
        for shlok in self.shloks:
            if shlok['id'] == id:
                return shlok


    def generate_random_id(self):
        while True:
            num = random.randint(1, 100)
            if num not in self.exclude_shloks:
                return num
