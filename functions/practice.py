"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world():
    '''Print 'Hello World' to the console.'''

    print "Hello World"


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name):
    '''Greet the given name with "Hi", printing to the console.  
    Empty names are called anonymous.'''

    if name == '' or name == None:
        name = 'anonymous'
    print "Hi %s" % name



# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.

def print_product(int_1, int_2):
    '''Prints the product of two given integers.'''

    assert type(int_1) in {int, long} and type(int_2) in {int, long}

    print int_1 * int_2


# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times

def repeat_string(input_string, integer):
    '''Print input_string a number of times specified by the given integer.
    Will not accept integers over a hundred thousand.'''

    assert type(input_string) == str  # First argument must be a string
    assert type(integer) == int and integer <= 10 ** 5  # Second argument must be an integer below 100,000

    if integer < 0:
        raise ValueError ("Must print input_string at least 0 times")
    else:
        print input_string * integer


# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".

def print_sign(integer):
    '''Print the sign of a given number.
    Designed for integers but accepts floats.'''

    assert type(integer) in {int, float, long}

    if integer == 0:
        print 'Zero'
    elif integer < 0:
        print "Lower than 0"
    else:
        print "Higher than 0"


# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.

def is_divisible_by_three(integer):
    '''Return True if an integer is divisible by three, False if not.'''

    return integer % 3 == 0

# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.


def num_spaces(sentence):
    '''Counts the number of spaces in a given sentence.'''

    if type(sentence) == str:
        return sentence.count(' ')
    elif type(sentence) == list:
        if [type(word) for word in sentence] == str * len(sentence):
            print "Sentence should be one string. Returning number of separations."
            return len(sentence) - 1
    else:
        raise TypeError("argument should be a string")


# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.

def total_meal_price(subtotal, tip_percentage = 0.15):
    '''Calculate the total price of a meal, given the subtotal and optional tip percentage as a decimal.
    Tip percentage defaults to 0.15 if not provided.'''

    if tip_percentage > 1:
        print "Warning: tip is over 100%. You may want to divide by 100."
    elif tip_percentage < 0:
        raise ValueError("tip cannot be set to a negative number")

    return subtotal + subtotal * tip_percentage

# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.

def sign_and_parity(integer): #DOCTEST IS WRONG ACCORDING TO INSTRUCTIONS
    '''Given an integer, return a tuple of strings naming its sign and parity.'''
    assert int(integer) == integer  # Argument must be an integer, or a float of equivalent value

    if integer % 2 == 0:
        parity = 'Even'
    else:
        parity = 'Odd'

    if integer < 0:
        sign = 'Negative'
    elif integer > 0:
        sign = 'Positive'
    else:
        sign = 'Zero'

    return [parity, sign]

parity, sign = sign_and_parity(142857)
print parity, sign


###############################################################################

# PART TWO

# 1. Write a function that takes a name and a job title as parameters, making
#    it so the job title defaults to "Engineer" if a job title is not passed
#    in. Return the person's title and name in one string.

def full_title(name, job_title = 'Engineer'):
    '''Return the person's job title and name in one string.'''

    return '%s %s' % (job_title, name)

# 2. Given a recipient name & job title and a sender name, print the following
#    letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


def write_letter(recipient, job_title, sender):
    '''Print an encouraging letter to recipient from sender, using job_title.'''


    print "Dear %s, I think you are amazing! Sincerely, %s" % (full_title(recipient, job_title), sender)


###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
