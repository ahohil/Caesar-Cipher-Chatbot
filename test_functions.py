from my_module.functions import *

#Test function does the following:
    # Test that function is callable
    # Test that it gives back some string for some input
    # Test that it give correct output for some given input
    # Replace this statement

    #Code adapted from A3
def test_remove_punctuation():
    
    assert callable(remove_punctuation)
    assert isinstance(remove_punctuation('hello'), str)
    assert remove_punctuation("Python's fun, but Python's moody!") == "Pythons fun but Pythons is moody"

    #Original Code
def test_bot_asks_question():
    
    assert callable(bot_asks_question)
    assert isinstance(bot_asks_question('Python'), str)
    assert bot_asks_question("Wow! Sunsets is San Diego are beautiful.") == "wow sunsets in san diego are beautiful"