#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## pendu
## File description:
## main function
##

import pickle
from random import randrange
from open_file import *

def restart_game(restart):
    restart = str(input("Would you want to continue to play ? : "))
    while (restart != "yes" and restart != "no"):
        restart = str(input("Would you want to continue to play ? : "))
    return (restart)

def display_text(my_world):
    success = 0
    for letter in my_world:
        if letter == '*':
            success = 1
    if success == 0:
        print("You win")
    return (success)

def fail_and_success(found, nb_fail, my_world, selected_world):
    if found == 1:
        print("Success: You found a character ", my_world)
    else:
        nb_fail -= 1
        print("Fail: The character isn't in the world. You have",
            nb_fail, "fail to find the world")
    if nb_fail == 0:
        print("You loose the world was:", selected_world)
    return (nb_fail)

def gameplay(selected_world, my_world):
    nb_fail = 8
    success = 1
    print("The world you need to find is :", my_world, "with nb fail:", nb_fail)
    while (success != 0 and nb_fail != 0):
        char = (input("Choose a character between (a, z): ")).lower()
        while (len(char) != 1 or (char < 'a' or char > 'z')):
            char = (input("Choose a character between (a, z): ")).lower()
        i = 0
        found = 0
        for letter in selected_world:
            if letter == char:
                my_list = list(my_world)
                my_list[i] = char
                my_world = ''.join(my_list)
                found = 1
            i += 1
        nb_fail = fail_and_success(found, nb_fail, my_world, selected_world)
        success = display_text(my_world)
    return (nb_fail)

def pendu():
    player_score = player_file("player_score", player_score = {})
    worlds = list_worlds("worlds", worlds = {})
    play = "yes"
    score = 0
    my_score = int(player_score[1])
    while (play == "yes"):
        selected_world = worlds[randrange(1, len(worlds))]
        my_world = ""
        for letter in selected_world:
            my_world += "*"
        print(player_score[0] + ", you have", my_score, "points")
        score = gameplay(selected_world, my_world)
        if score != 0:
            my_score += (score * 2)
        else:
            my_score -= 4
        print("Your points are about:", score * 2)
        play = restart_game(play)
    player_score[1] = str(my_score)
    player_fill_file("player_score", player_score)

pendu()
