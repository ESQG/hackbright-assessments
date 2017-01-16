"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   ARRGH FINISH LATER


2. What is a class?

    A class is a data type, usually referring to a custom-designed data type as opposed to a built-in 
type such as int, float, long, str (string), or list in Python.  Once a class is defined, an object
belonging to that class is called an instance of the class; we can use a variable to refer
to it, as we would to an instance of a built-in type.  In Python, classes can have specialized variables, called
"attributes", and specialized functions, called "methods".  There are also many default methods that are set in
Python for using a class istance, such as a method for "print me" or "check if I am equal to some other object in my class"
(which is False by default); the latter method is called when the "==" sign is used.
    So for example, if we were making the game Sims we might define a class Human, and an instance of Human would be a person.
There are attributes we expect a person to have, like a name, height, age and so on.  And then there are methods, for 
"things a person can do" or "things you can do to a person", like "sleep" or "give gift".  We can also
check if harry == sally, and expect False; but we would have to decide whether two people with the same name
were considered equal.  And then, we would *not* expect to be able to compare people, e.g. "harry < sally".  In Python
that would return a default value of False and it's fine to leave it that way.  Or we could decide
that people should be compared by last name and then first name; thus, a list of Humans could be sorted.  And we might
specify that if we say "print person" the person's name would be printed, or perhaps all their attributes.
    In the class int, one doesn't expect an integer to have a name--although we *could* write a special class of 
"named integer", so for example (3).name would be "three".  So, all of that is to say, a class encapsulates not only some
data, but its attributes define the expected structure of that data, and its methods, what we expect to do with it.


3. What is an instance attribute?

    Oops, I went into that above.  It's a piece of data stored along with the instance, that can be referred to by a
variable.  What makes it different from a class attribute is that it's stored per instance, not for the whole class at once;
for example, each person in class Human may have a name, but it makes sense to store their name as an instance attribute 
because each person has a different name.

4. What is a method?

    A method is a function designed for use by (or on) elements of a given class.  In Python we define such methods
under the class definition.  As I said above Python has many built-in methods, some are expected for any object, and others
are optional but are called when we try to do things.  For example, "print x" calls the "__str__" method on x, and if there
isn't one it calls the __repr__ method. (I think, based on how I've done things with classes, though I haven't looked up the
order of precedence.)  "x + y" calls the __add__ method on x and attempts to add y to x using this method.
"a < b" calls the __lt__ method on a (I belive).  Sorting a list calls the "__lt__" method on elements of a list.  (That seems
to be all it needs.)  But methods aren't all built-in, they can be defined however we want,
and then in Python, called with a dot after the instance's variable.  
    In the class Human, we might define a method called "give gift" which takes a gift, and a recipient, 
and gives the gift from the person the method was called on, to the recipient.
(If a list of possessions was an instance attribute, perhaps calling person.give_gift(recipient, thing) would remove
thing from the person's possessions and append it to the recipient's possessions.)

5. What is an instance in object orientation?

    I don't know if I understand the question.  But, an instance of a class is a piece of data created with the properties
of that class, meaning methods, attributes, and any attributes specific to itself.  In terms of memory storage, I believe the
instance would have pointers going back to its class definition, so that calling a method or a class attribute would
find that information in the class that the instance came from, and use it.


6. How is a class attribute different than an instance attribute?
   For an instance of Human, you might have a class attribute called "diet", specifying what things any person
could eat and successfully digest.  Humans can generally successfully eat lots of parts of plants, fungi and animals.
However, an individual person might have allergies or preferences preventing them from eating all the same things.
That person might also have an instance attribute called "dietary restrictions" specifying things that Humans in general
can eat, but this instance (person) cannot.  In this setup, "diet" is a class attribute because it describes our diet as a
species (although in Python we can override this variable with an instance attribute, or mutate it for the whole class if 
it's a mutable data type) and then "restrictions" is specific to each person, likely different for each person,
making it an instance attribute.
    At less length: an instance attribute is stored with the instance, and a class attribute is stored with the whole class.
In Python, writing a.name will first look for an instance attribute "name" on a, and then check for a class attribute "name"
on the class type(a). (And then keep checking ancestor classes until it succeeds or throws an error.)

"""


# Parts 2 through 5:
# Create your classes and class methods

# Part 2

class Student(object):

    def __init__(self, first_name, last_name='Unknown', address='Address Unknown'):  # Must specify first name; last name and address are optional
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __repr__(self):
        return "<Student %s %s>" % (first_name, last_name)

class Question(object):
    """Stores a question and answer, with a default answer of "Unknown".  
    Displays as the question; also prints as the question only.
    >>> q = Question("Why did the chicken cross the road?", "To get to the Other Side!")
    >>> q
    <Question: Why did the chicken cross the road?>
    >>> print q
    Why did the chicken cross the road?
    >>> str(q)
    'Why did the chicken cross the road?'

    The ask_and_evaluate method returns True if the answer is correct, False otherwise.  See its docstring.
    """

    def __init__(self, question, answer='Unknown'): # Answer is optional
        self.question = question
        self.correct_answer = answer.rstrip(".!") # Strips punctuation off of answer

    def __repr__(self):
        return "<Question: %s>" % self.question

    def __str__(self):
        return self.question

    def ask_and_evaluate(self):
        """Prompts user with a question, then evaluates if it is the correct answer.  Ignores trailing whitespace and
        ending periods and exclamation marks.  Case insensitive.

        >>> q = Question("Why did the chicken cross the road?", "To get to the Other Side!")

        If you call q.ask_and_evaluate() you get:
        Why did the chicken cross the road? > To get to the other side
        True
        """

        answer = raw_input(str(self) + " > ").strip().rstrip(".!")
        if answer.lower() == self.correct_answer.lower():
            return True
        else:
            return False

class Exam(object):
    """
    The Exam class stores a name of the exam and a list of questions.  It prints as the exam name, with questions
    numbered and separated by blank lines.  The .administer() method calls .ask_and_evaluate() on each question.

    >>> midterm = Exam("Midterm")
    >>> midterm
    <Exam: Midterm>
    >>> midterm.add_question("Why did the chicken cross the road?", "To get to the other side")
    >>> midterm.add_question("What was the original pun in that joke?", "The Other Side meant the afterlife")
    >>> midterm.add_question("What is your name?", "Elizabeth")
    >>> midterm.add_question("What is your quest?", "To become a software engineer")
    >>> midterm.add_question("What is your favorite color?", "Forest green")

    >>> print midterm
    Midterm exam:
    <BLANKLINE>
    1. Why did the chicken cross the road?
    <BLANKLINE>
    2. What was the original pun in that joke?
    <BLANKLINE>
    3. What is your name?
    <BLANKLINE>
    4. What is your quest?
    <BLANKLINE>
    5. What is your favorite color?

    I can't figure out how to make the following a doctest without having to enter the input myself, but I expect:
    midterm.administer()
    Why did the chicken cross the road? > To get to the other side.
    What was the original pun in that joke? > The Other Side meant the afterlife.
    What is your name? > Elizabeth
    What is your quest? > To become a software engineer
    What is your favorite color? > Forest green
    1.0

    midterm.administer()
    Why did the chicken cross the road? > To get to the other side
    What was the original pun in that joke? > I don't know
    What is your name? > Elizabeth
    What is your quest? > To become a software engineer!
    What is your favorite color? > Green
    0.6
    
"""

    def __init__(self, name):
        self.name = name
        self.questions = []    # use elements of the class Question to fill this out

    def add_question(self, question, answer):
        """Uses the given question and answer to initialize a new Question instance and append it to self.questions."""

        self.questions.append(Question(question, answer))  # Appends an element of the class Questions to the lsit.

    def administer(self):
        """Prompts user for each question in turn, evaluates the answer, and returns a score of fraction correct."""

        self.score = 0
        for question in self.questions:
            self.score += question.ask_and_evaluate()   # True counts as 1, False counts as 0
        return self.score / float(len(self.questions))

    def __repr__(self):
        return "<Exam: %s>" % self.name

    def __str__(self):
        lines = ["%s exam:" % self.name]
        for i, question in enumerate(self.questions):
            question_line = str(i+1)+". " + str(question)
            lines.append(question_line)
        return '\n\n'.join(lines)


# Part 4

def take_test(exam, student):
    """Administer the given exam to the student; then assign the resulting score to that student."""

    student.score = exam.administer()

def example():

    amelia = Student("Amelia", "Bedelia")

    exam = Exam("Housekeeping")
    exam.add_question("How do you put out the lights?", "Find the lightswitch and turn it off.")
    exam.add_question("How do you draw the drapes?", "Open them if it's light out, close them if it's dark.")
    exam.add_question("How do you dress the chicken?", "Clean it and prepare it for cooking.")
    exam.add_question("How do you make a lemon meringue pie?", "Using a very good recipe.")

    take_test(exam, amelia)
    #Note: Amelia Bedelia's answers would be as follows:
    # Take the lightulbs out and hang them outside.
    # Get a piece of paper and sketch the drapes on it.
    # Make tiny clothes to fit the chicken, then dress it in them.
    # Using a very good recipe.

# Part 5

#TIME SPENT: 2.5 hours Saturday.

class Quiz(Exam):
    """Like an exam, except that administering it returns True if the score is at least 50%, and False otherwise."""

    def administer(self):
        return super(Quiz, self).administer() >= 0.5   # True if at least half the questions are right.

    def __repr__(self):
        return "< Quiz: %s>" % self.name

    def __str__(self):
        reused_lines = super(Quiz, self).__str__().split('\n\n')
        print reused_lines
        first_line = "%s quiz:"
        reused_lines[0] = first_line
        return '\n\n'.join(reused_lines)

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED"
    print

