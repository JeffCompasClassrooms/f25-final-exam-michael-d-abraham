import pytest
import pytest_describe
import pytest_spec
from brute import Brute


# Unit tests for the Brute class
# We'll test bruteOnce without test doubles and bruteMany with test doubles

def describe_brute_once():


    def test_brute_once_with_correct_password():
        """Test that bruteOnce returns True when given the correct password"""
        # Instance of Bruteto use
        secret = "mike"
        brute = Brute(secret)
        
        # Test that its worked 
        result = brute.bruteOnce("mike")
        
        # TRUEEE needs to be true 
        assert result == True
    
    def test_brute_once_with_incorrect_password():
        # INstannce
        secret = "Mike"
        brute = Brute(secret)
        
        # Wrong result
        result = brute.bruteOnce("NotMike")
        
        # Flase test one
        assert result == False
    
    def test_brute_once_with_empty_string():
        # Brute instance with empty string
        secret = ""
        brute = Brute(secret)
        
        # same 
        result = brute.bruteOnce("")
        
        #True becuaes they are both empty
        assert result == True
    
    def test_brute_once_with_empty_string_false():
        secret = "mike"
        brute = Brute(secret)
        
        # empty string (doesn't match)
        result = brute.bruteOnce("")
        
        # Flase homies dont match
        assert result == False
    
    

    def test_brute_once_with_max_len_lettes():
        # Do exactly 8 numbers
        secret = "mikeisme"
        brute = Brute(secret)
        
        # correct (true test)
        result_correct = brute.bruteOnce("mikeisme")
        assert result_correct == True
        
        # incorrect (false test)
        result_wrong = brute.bruteOnce("imsteves")
        assert result_wrong == False

    def test_brute_once_with_max_len_numbers():
        # Do exactly 8 numbers
        secret = "12345678"
        brute = Brute(secret)
        
        # correct (true test)
        result_correct = brute.bruteOnce("12345678")
        assert result_correct == True
        
        # incorrect (false test)
        result_wrong = brute.bruteOnce("12345679")
        assert result_wrong == False
    
    def test_brute_once_with_number():
        secret = "12345"
        brute = Brute(secret)
        
        # true
        result = brute.bruteOnce("12345")
        assert result == True
        
        # false
        result = brute.bruteOnce("54321")
        assert result == False
    
    def test_brute_once_with_letters_only():

        secret = "mike"
        brute = Brute(secret)
        
        # correct 
        result = brute.bruteOnce("mike")
        assert result == True
        
        # False (case sensitive)
        result = brute.bruteOnce("MIKE")
        assert result == False


# I need some tests for random guess (big coverage guy)
def describe_random_guess():
    """Test suite for the randomGuess method"""
    
    def test_random_guess_length():
        """Test that randomGuess returns a string of length 1-8"""
        
        # Create a Brute instance
        secret = "test"
        brute = Brute(secret)
        
        # couple random guesses to test randomness
        for i in range(20):
            random_string = brute.randomGuess()
            
            # Check length is between 1 and 8
            assert len(random_string) >= 1
            assert len(random_string) <= 8
    
    def test_random_guess_is_alphanumeric():
        """Test that randomGuess returns only alphanumeric characters"""
        # Create a Brute instance
        secret = "test"
        brute = Brute(secret)
        
        # Generate random guesses
        for i in range(20):
            random_string = brute.randomGuess()
            
            # Check all characters are alphanumeric (letters or digits)
            assert random_string.isalnum()
    
    def test_random_guess_is_random():
        """Test that randomGuess produces different results"""
        # Create a Brute instance
        secret = "test"
        brute = Brute(secret)
        
        # Generate multiple random guesses
        guesses = []
        for i in range(50):
            guesses.append(brute.randomGuess())
        
        # Check that we got some variety (not all the same)
        # This is probabilistic but very likely with 50 attempts
        unique_guesses = set(guesses)
        assert len(unique_guesses) > 1 


        

def describe_brute_many():
    # DOUBLESSSSS
    
    def test_brute_many_success_with_mock_random_guess(mocker):
        # Create a Brute instance
        secret = "mike"
        brute = Brute(secret)
        
        # Mock randomGuess
        mocker.patch.object(brute, 'randomGuess', return_value="mike")
        
        # limit of 10 attempts to find passowrd
        result = brute.bruteMany(limit=10)
        
        # Should return a time (not -1)
        assert result != -1
        assert result >= 0  # doesn't mater what time just a posstive time
    
    def test_brute_many_failure_when_limit_reached(mocker):
        # test brutemany when the limit is reached without success retunrs -1

        # instance
        secret = "mike"
        brute = Brute(secret)
        
        # Mock 
        mocker.patch.object(brute, 'randomGuess', return_value="steve")
        

        # small limit (mess withthis till it fails) 
        result = brute.bruteMany(limit=5)
        
        # I want tit to retunr -1 becuase it failed 
        assert result == -1
    
    def test_brute_many_success_on_second_attempt(mocker):
        # succesed on seciont attempt
        # instance
        secret = "right"
        brute = Brute(secret)
        

        # Mock randomGuess to return wrong first, then correct
        # Keep trying until it gets it
        mocker.patch.object(brute, 'randomGuess', side_effect=["wrong1", "right", "wrong2"])


        result = brute.bruteMany(limit=10)
        
        # tests
        assert result != -1
        assert result >= 0
    
    def test_brute_many_with_limit_zero(mocker):
        # edge case limit of 0
        # instance
        secret = "mike"
        brute = Brute(secret)
        
        # Mock randomGuess (won't be called because limit is 0 (pretty sure LOL))
        mocker.patch.object(brute, 'randomGuess', return_value="mike")
        
        # limit 0
        result = brute.bruteMany(limit=0)
        
        #please rturn -1 because no attempts were made rihgt?!
        assert result == -1
    
    def test_brute_many_with_limit_one_success(mocker):
        # limit of 1 and successful guess
        # instance
        secret = "mike"
        brute = Brute(secret)
        
        # Mock 
        mocker.patch.object(brute, 'randomGuess', return_value="mike")
        
        # limit 1
        result = brute.bruteMany(limit=1)
        
        # Should succeed
        assert result != -1
    
    def test_brute_many_with_limit_one_failure(mocker):
        # limit of 1 and fialed guess
        # instance
        secret = "mike"
        brute = Brute(secret)
        
        # Mock randomGuess to return wrong password
        mocker.patch.object(brute, 'randomGuess', return_value="steve")
        
        # limit 1
        result = brute.bruteMany(limit=1)
        
        # Should fail
        assert result == -1
    
    def test_brute_many_verifies_random_guess_called(mocker):
        # test if brute many actaully calls random guess method
        # Create a Brute instance
        secret = "mike"
        brute = Brute(secret)
        

        # mock for randomGuess
        mock_random = mocker.patch.object(brute, 'randomGuess', return_value="stebe")
        
        # limit of 5
        result = brute.bruteMany(limit=5)
        
        #  randomGuess should be called 5 times
        assert mock_random.call_count == 5
    
    def test_brute_many_stops_on_first_success(mocker):
        """Test that bruteMany stops calling randomGuess after success"""
        # Create a Brute instance
        secret = "mike"
        brute = Brute(secret)
        
        # Mock randomGuess to return correct on 2 call
        mock_random = mocker.patch.object(brute, 'randomGuess', side_effect=["wrong", "mike", "wrong"])
        

        result = brute.bruteMany(limit=10)
        
        # Should succeed
        assert result != -1
        
        # Should only call randomGuess twice (stops after success)
        assert mock_random.call_count == 2
    
    def test_brute_many_verifies_brute_once_called(mocker):
        """Test that bruteMany calls bruteOnce with the random guesses"""
        # instance
        secret = "test"
        brute = Brute(secret)
        
        # Mock wornds
        mocker.patch.object(brute, 'randomGuess', side_effect=["guess1", "guess2", "guess3"])
        
        # Mock bruteOnce to track calls
        mock_brute_once = mocker.patch.object(brute, 'bruteOnce', return_value=False)
        
        # Try to crack with limit of 3
        result = brute.bruteMany(limit=3)
        
        # Verify bruteOnce was called 3 times
        assert mock_brute_once.call_count == 3
        
        # the guesses worked
        assert mock_brute_once.call_args_list[0][0][0] == "guess1"
        assert mock_brute_once.call_args_list[1][0][0] == "guess2"
        assert mock_brute_once.call_args_list[2][0][0] == "guess3"

