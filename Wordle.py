########################################
# Name: Jennifer Arreola
# Collaborators (if any):
# GenAI Transcript (if any): https://chatgpt.com/c/66f87cf4-855c-8013-abdf-4c8f8beae8cb (used to figure out how to update the unmatched string correctly, perfect_matchs was a result of the suggestions)
# Estimated time spent (hr): 5.45 hrs
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        guess = check_guess() # identfies guess to be the checked guess to see if attempt was succesful
        count = gw.get_current_row() #checks on what attempt number the user is on
        if guess == secret: #checks if the guess is the secret word
                gw.show_message("You've guessed correctly!")
                gw.set_current_row(N_ROWS) #ends game by maxing out guesses/rows
        else: 
            if count == N_ROWS : #if last attempt is used meaning the count is now equal to the total amount of rows then secret word is revealed
                gw.show_message("The correct word is" + " " +secret.upper() + " ! " +" Better luck next time! ") #message that reveals secret word
        

    def check_guess():
        guess = "" #creates empty string to hold the inputed guess
        for col in range(N_COLS): #iterates through the letter boxes in current row
            guess += gw.get_square_letter(gw.get_current_row(),col) #retrieves and adds the guessed letters to the empty string of guess
        guess = guess.lower() #converts guess to lower cases
    
        if guess in five_letter_list(): #checks the guess is a valid length and exists
            color_squares(guess) #colors squares and keys with respective colors based on matching letters
            gw.show_message("Nice guess! :)") #if guess meets criteria it will display a congratulary message 
            gw.set_current_row(gw.get_current_row() + 1) #moves on to next guess attempt
        else:
            gw.show_message("Make sure the word is five letters long and exists :)") #message shown if criteria is not met for five letter word guess 
    
        return guess #returns guess to be used in enter_action to stop the game if guess == secret
    
    def color_squares(guess):
        unmatched = list(secret) #copy of secret word as a list to keep track of matches
        perfect_matches = [False] * len(secret) #keeps track of all perfect mataches by initializing a list where they are non matches
        perfect_match(guess, unmatched, perfect_matches) #checks for perfect matches by taking the arguments of the guess and unmatched, while updating and using the perfect_matches list
        present_or_wrong(guess, unmatched, perfect_matches) #checks for letters that are present and deems all other wrong

    def perfect_match(guess, unmatched, perfect_matches):
        for i in range (len(guess)): #iterates through the letters in the guess
            if guess[i] == unmatched[i]: #checks if both the letter and index are the same
                gw.set_square_color(gw.get_current_row(), i , CORRECT_COLOR) #colors the matching letters box green
                perfect_matches[i] = True #updates perfect match list to true for matched letter
                unmatched[i]  = None #updates unmatched list to skip over the perfect match
                color = gw.get_key_color(guess[i]) #checks the color of the key that was guessed correctly 
                if color not in [CORRECT_COLOR]: #if it hasn't already been colored it will color it the key green
                    gw.set_key_color(guess[i], CORRECT_COLOR)
    
    def present_or_wrong(guess, unmatched, perfect_matches):
        for i in range(len(guess)): #iterates through the letters in the guess
            if not perfect_matches[i]: #only checks the ones that are not perfect matches
                if guess[i] in unmatched: #checks if any remaining letters are present in matched
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR) #colors present letter box yellow
                    unmatched[unmatched.index(guess[i])] = None #removes present letter from unmatched using the guess index
                    color = gw.get_key_color(guess[i]) #retrieves current key color of letter 
                    if color not in [CORRECT_COLOR,PRESENT_COLOR]: #prioritzes it leaving it green if already guessed correctly
                        gw.set_key_color(guess[i], PRESENT_COLOR) #colors key yellow if it's not already green or yellow
                else:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR) #colors all other letter box guesses gray
                    color = gw.get_key_color(guess[i]) #checks the color the non matched keys
                    if color not in [CORRECT_COLOR,PRESENT_COLOR]: #priorites it leaving it green or yellow if present
                        gw.set_key_color(guess[i], MISSING_COLOR) #colors key grey

    def five_letter_list(): #creates a list of all five letter words in ENGLISH_WORDS
        """Returns a list of all 5 letter words in ENGLISH_WORDS"""
        five_letters = [ ] #creates a blank list to put word in
        for word in ENGLISH_WORDS:
            if len(word) == 5: #check that the length of the word is five
                five_letters += [ word ] #once criteria is met adds the word to the list
        return five_letters #returns list
    
    
    
    secret = random.choice(five_letter_list()) #randomly selects a word from the list
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
