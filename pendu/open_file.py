#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## pendu
## File description:
## open_file
##

import pickle

def list_worlds(path, worlds):
    try:
        world_file = open(path, "r")
        worlds = world_file.read()
        worlds = worlds.split(" ")
        for items in worlds:
            assert (len(items) <= 8)
    except FileNotFoundError:
        print("Error:File not successfully found")
        exit(84)
    except:
        print("Error:Wolrd of a len sup. to 8 characters")
        exit(84)
    return (worlds)

def player_file(path, player_score):
    try:
        player_file = open(path, "rb")
        my_unpickle = pickle.Unpickler(player_file)
        player_read = my_unpickle.load()
    except FileNotFoundError:
        player_read = [input("Select a name: "), "0"]
        player_file = open(path, "wb")
        my_pickler = pickle.Pickler(player_file)
        my_pickler.dump(player_read)
    return (player_read)

def player_fill_file(path, player_score):
    player_file = open(path, "wb")
    my_pickler = pickle.Pickler(player_file)
    my_pickler.dump(player_score)
