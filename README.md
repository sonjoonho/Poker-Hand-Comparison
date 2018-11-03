# **Poker Hand Comparison**

This is a repository that contains my solution to the Grabyo Poker Hand Comparison technical test. It is written in **Python 3.6** with **Pytest** for testing (see `Pipfile` for more details). This project uses **Pipenv** for dependency management.

## Usage

### Example

```python
from Pokerhand.Pokerhand import Pokerhand

hand1 = Pokerhand("KC KH KD 7C 5S")
hand2 = Pokerhand("KS KH KD 7C 5S")

result = hand1.compareWith(hand2)
```

### Running tests

In the project root:

```shell
pipenv install -e .
pipenv run pytest
```

## Structure

```python
Pipfile
Pipfile.lock
PokerHand/__init__.py
PokerHand/Pokerhand.py # Contains main implementation
tests/test_comparison.py # Tests for hand comparison
tests/test_value.py # Tests for value calculation
```

This project was implemented in accordance to the PEP 8 style guidelines.

## Approach

The implemented algorithm is a simple method to compare hands. It primarily uses the number of distinct ranks in the hand, and also takes into consideration suits when necessary.

The approach also includes an enum called `Value` that represents that value of a hand. This provides readability.

One of the flaws of my algorithm is that it does not take into account the concept of **kickers**. This is used to settle ties. However, this would add significant complexity and a time commitment which I currently do not have the capacity to offer.

This problem could also have been approached using a lookup table. However, this requires a relatively large amount of memory, and due to the limited scope of the problem it does not offer a significant runtime advantage. If, however, we were scaling the problem up to compare large numbers of hands, this would provide a more viable approach.

## Original Text 

>> Poker Hand Comparison is a little program that will compare two hands of poker according to the rules of [Texas Hold'em rules](https://en.wikipedia.org/wiki/Texas_hold_%27em#Hand_values).
>> 
>> ## Requirements
>> 
>> The characteristics of the string of cards are:
>> * A space is used as card separator
>> * Each card consists of two characters (not case sensitive)
>> * The first character is the value of the card, valid characters are: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `T`(en), `J`(ack), `Q`(ueen), `K`(ing), `A`(ce)
>> * The second character represents the suit, valid characters are: `S`(pades), `H`(earts), `D`(iamonds), `C`(lubs)
>> 
>> The result of your poker hand compare can be one of these 3 options:
>> * WIN should return the integer `1`
>> * LOSS should return the integer `2`
>> * TIE should return the integer `3`
>> 
>> You are free to use any libraries you want but please do not anything that already evaluates poker hands ;)
>> 
>> Good luck!
