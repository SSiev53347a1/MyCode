#!/usr/bin/evv python3

# This program test if, elif, else in the format of CABLE TV Channel choices

## Collecting information from consumer
## Package types
## Basic Channels 1-10 if input falls between 1 and 10 print basic
## Standard Channels 1-40 if input falls between 1 and 40 but greater than 10 print Standard
## Premium Channels 1-100 if input falls between 41 and 100 but greater than 40 print Premium
## HD Channels 101-200 if input falls between 101 and 200 but greater tha 100 print HD Channels
## Epensive Channels Extra 201-600 

def channel():

#rem lineups=['basic_channels', 'standard_channels', 'premium_channels', 'hd_channels', 'extra_channels']
    channel_select = int(input("what is your favorite channel to watch from 1 to 600: "))
    if channel_select >= 1 and channel_select <= 10:
        print ("you selected {}: The basic package will work for you".format (channel_select))
    elif channel_select >= 11 and channel_select <= 40:
        print ("you selected {}: The Standard package will work for you".format (channel_select))
    elif channel_select >= 41 and channel_select <= 100:
        print ("you selected {}: The Premium package will work for you".format (channel_select))
    elif channel_select >= 101 and channel_select <= 200:
        print ("you selected {}: The HD Service will work for you".format (channel_select))
    elif channel_select >= 201 and channel_select <= 600:
        print ("you selected {}: The Extra Channel Package will work for you".format (channel_select))
    else:
        print ("Please make your selection a number between 1 and 600")
    channel() 
    
channel()

