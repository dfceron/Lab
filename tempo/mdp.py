# coding: utf-8

import numpy as np

import markov_chain as mc

class State(mc.State):
    def __init__(self, tag, reward):
        super().__init__(tag)
        self.reward = reward

    def __repr__(self):
        return '{} ({})'.format(self.tag, self.reward)

class Transition(mc.Transition):
    def __init__(self, from_state, to_state, action, probability):
        super().__init__(from_state, to_state, probability)
        self.action = action

    def __repr__(self):
        return '{} --[{}, {}]--> {}'.format(self.from_state,
                                            self.action,
                                            self.probability,
                                            self.to_state)
class MDP(mc.MarkovChain):
    def __init__(self, S=None, A=None, P=None, R=None, gamma=None, initial_state=None):
        super(mc.MarkovChain,self).__init__(S,P,initial_state)


    ## Completa el código (sin resolver las bellman optimality equations)
