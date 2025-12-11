import pytest
import pytest_describe
import pytest_spec
import os
import shutil
from christmas_list import ChristmasList

# Test the if the file prints out right
# USe this

# def check_off_works_in_print_list(capsys):

#     do stuff heapreplace

#     cl.print_list()

#     captured = capsys.readouterr()
#     assert captured.out == "[x] bb gun\n"


# System tests for the ChristmasList class
# We need to control the environment - use empty database file for each test

def describe_christmas_list_system_tests():
    """System test suite for ChristmasList - controlling the environment"""
    
    def test_add_item_to_empty_list():
        """Test adding an item to an empty Christmas list"""
        # temp file for this
        test_file = "test_christmas_list_1.pkl"
        
        # Ensure the file doesn't exist that will goof stuff up
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # CChristmasList instance (Empty file!!!)
        christmas_list = ChristmasList(test_file)
        
        # Add an item
        christmas_list.add("Guitar")
        
        # COME BACK TO THIS
        # add a test here to see if it was added correctly? or will just texting the load be the smae?

        # Load items and test
        items = christmas_list.loadItems()
        assert len(items) == 1
        assert items[0]["name"] == "Guitar"
        assert items[0]["purchased"] == False
        
        # Clean up - remove test file
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_add_multiple_items():
        """Test adding multiple items to the list"""
        # temp name
        test_file = "test_christmas_list_2.pkl"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList instance
        christmas_list = ChristmasList(test_file)
        
        # Add multiple items
        christmas_list.add("Car")
        christmas_list.add("Guitar")
        christmas_list.add("Game")
        
        # Load and verify
        items = christmas_list.loadItems()
        assert len(items) == 3
        assert items[0]["name"] == "Car"
        assert items[0]["purchased"] == False
        assert items[1]["name"] == "Guitar"
        assert items[1]["purchased"] == False
        assert items[2]["name"] == "Game"
        assert items[2]["purchased"] == False
        
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_check_off_item():
        """Test checking off an item as purchased"""
        # Use a temporary file name
        test_file = "test_christmas_list_3.pkl"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList and add items
        christmas_list = ChristmasList(test_file)
        christmas_list.add("Bike")
        christmas_list.add("Book")
        
        # Check off one item
        christmas_list.check_off("Bike")
        
        # Load items and verify
        items = christmas_list.loadItems()
        assert len(items) == 2
        
        # Check that Bike is purchased and Book is not
        for item in items:
            if item["name"] == "Bike":
                assert item["purchased"] == True
            elif item["name"] == "Book":
                assert item["purchased"] == False
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_check_off_multiple_items():
        """Test checking off multiple items"""
        # Use a temporary file name
        test_file = "test_christmas_list_4.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList and add items
        christmas_list = ChristmasList(test_file)
        christmas_list.add("Item1")
        christmas_list.add("Item2")
        christmas_list.add("Item3")
        
        # Check off two items
        christmas_list.check_off("Item1")
        christmas_list.check_off("Item3")
        
        # Load and verify
        items = christmas_list.loadItems()
        assert len(items) == 3
        
        # Verify purchased status
        for item in items:
            if item["name"] == "Item1" or item["name"] == "Item3":
                assert item["purchased"] == True
            else:
                assert item["purchased"] == False
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_check_off_nonexistent_item():
        """Test checking off an item that doesn't exist - should not crash"""
        # Use a temporary file name
        test_file = "test_christmas_list_5.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList and add one item
        christmas_list = ChristmasList(test_file)
        christmas_list.add("Real item")
        
        # Try to check off item that doesn't exist
        # Should not crash, just do nothing
        christmas_list.check_off("Fake item")
        
        # Load and verify original item still there
        items = christmas_list.loadItems()
        assert len(items) == 1
        assert items[0]["name"] == "Real item"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_remove_item():
        """Test removing an item from the list"""
        # Use a temporary file name
        test_file = "test_christmas_list_6.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList and add items
        christmas_list = ChristmasList(test_file)
        christmas_list.add("Keep this")
        christmas_list.add("Remove this")
        christmas_list.add("Keep this too")
        
        # Remove one item
        christmas_list.remove("Remove this")
        
        # Load and verify
        items = christmas_list.loadItems()
        assert len(items) == 2
        assert items[0]["name"] == "Keep this"
        assert items[1]["name"] == "Keep this too"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_remove_multiple_items():
        """Test removing multiple items"""
        # Use a temporary file name
        test_file = "test_christmas_list_7.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList and add items
        christmas_list = ChristmasList(test_file)
        christmas_list.add("Item1")
        christmas_list.add("Item2")
        christmas_list.add("Item3")
        christmas_list.add("Item4")
        
        # Remove two items
        christmas_list.remove("Item2")
        christmas_list.remove("Item4")
        
        # Load and verify
        items = christmas_list.loadItems()
        assert len(items) == 2
        assert items[0]["name"] == "Item1"
        assert items[1]["name"] == "Item3"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_remove_nonexistent_item():
        """Test removing an item that doesn't exist - should not crash"""
        # Use a temporary file name
        test_file = "test_christmas_list_8.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList and add one item
        christmas_list = ChristmasList(test_file)
        christmas_list.add("Real item")
        
        # Try to remove item that doesn't exist
        # Should not crash
        christmas_list.remove("Fake item")
        
        # Load and verify original item still there
        items = christmas_list.loadItems()
        assert len(items) == 1
        assert items[0]["name"] == "Real item"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_remove_all_items():
        """Test removing all items from the list"""
        # Use a temporary file name
        test_file = "test_christmas_list_9.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList and add items
        christmas_list = ChristmasList(test_file)
        christmas_list.add("Item1")
        christmas_list.add("Item2")
        
        # Remove all items
        christmas_list.remove("Item1")
        christmas_list.remove("Item2")
        
        # Load and verify list is empty
        items = christmas_list.loadItems()
        assert len(items) == 0
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_add_remove_add_sequence():
        """Test a sequence of add, remove, add operations"""
        # Use a temporary file name
        test_file = "test_christmas_list_10.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList
        christmas_list = ChristmasList(test_file)
        
        # Add item
        christmas_list.add("First")
        
        # Remove it
        christmas_list.remove("First")
        
        # Add new item
        christmas_list.add("Second")
        
        # Load and verify
        items = christmas_list.loadItems()
        assert len(items) == 1
        assert items[0]["name"] == "Second"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_check_off_then_remove():
        """Test checking off an item then removing it"""
        # Use a temporary file name
        test_file = "test_christmas_list_11.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList and add item
        christmas_list = ChristmasList(test_file)
        christmas_list.add("Item1")
        christmas_list.add("Item2")
        
        # Check off Item1
        christmas_list.check_off("Item1")
        
        # Remove Item1
        christmas_list.remove("Item1")
        
        # Load and verify only Item2 remains
        items = christmas_list.loadItems()
        assert len(items) == 1
        assert items[0]["name"] == "Item2"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_empty_list_initialization():
        """Test that creating a ChristmasList with non-existent file creates empty list"""
        # Use a temporary file name that definitely doesn't exist
        test_file = "test_christmas_list_new.pkl"
        
        # Make sure it doesn't exist
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList - should create empty file
        christmas_list = ChristmasList(test_file)
        
        # Load and verify it's empty
        items = christmas_list.loadItems()
        assert len(items) == 0
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_persistence_across_instances():
        """Test that data persists when creating new ChristmasList instance"""
        # Use a temporary file name
        test_file = "test_christmas_list_persist.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create first instance and add item
        christmas_list1 = ChristmasList(test_file)
        christmas_list1.add("Persistent item")
        
        # Create second instance with same file
        christmas_list2 = ChristmasList(test_file)
        
        # Load from second instance and verify item is there
        items = christmas_list2.loadItems()
        assert len(items) == 1
        assert items[0]["name"] == "Persistent item"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_duplicate_item_names():
        """Test adding items with duplicate names"""
        # Use a temporary file name
        test_file = "test_christmas_list_duplicate.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList
        christmas_list = ChristmasList(test_file)
        
        # Add same name twice
        christmas_list.add("Duplicate")
        christmas_list.add("Duplicate")
        
        # Load and verify both are there
        items = christmas_list.loadItems()
        assert len(items) == 2
        assert items[0]["name"] == "Duplicate"
        assert items[1]["name"] == "Duplicate"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_print_list_with_unpurchased_item(capsys):
        """Test print_list shows unpurchased items with underscore"""
        # Use a temporary file name
        test_file = "test_christmas_list_print1.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList and add item
        christmas_list = ChristmasList(test_file)
        christmas_list.add("Toy car")
        
        # Print the list
        christmas_list.print_list()
        
        # Capture what was printed
        captured = capsys.readouterr()
        
        # Should show unpurchased item with underscore
        assert captured.out == "[_] Toy car\n"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    


    
    def test_print_list_with_purchased_item(capsys):
        """Test print_list shows purchased items with x"""
        # Use a temporary file name
        test_file = "test_christmas_list_print2.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList, add item, and check it off
        christmas_list = ChristmasList(test_file)
        christmas_list.add("bb gun")
        christmas_list.check_off("bb gun")
        
        # Print the list
        christmas_list.print_list()
        
        # Capture what was printed
        captured = capsys.readouterr()
        
        # Should show purchased item with x
        assert captured.out == "[x] bb gun\n"
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_print_list_with_multiple_items(capsys):
        """Test print_list with multiple items, some purchased"""
        # Use a temporary file name
        test_file = "test_christmas_list_print3.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList and add items
        christmas_list = ChristmasList(test_file)
        christmas_list.add("Bike")
        christmas_list.add("Book")
        christmas_list.add("Game")
        
        # Check off one item
        christmas_list.check_off("Book")
        
        # Print the list
        christmas_list.print_list()
        
        # Capture what was printed
        captured = capsys.readouterr()
        
        # Should show all items, Book with x, others with _
        assert "[_] Bike\n" in captured.out
        assert "[x] Book\n" in captured.out
        assert "[_] Game\n" in captured.out
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_print_list_empty_list(capsys):
        """Test print_list with empty list prints nothing"""
        # Use a temporary file name
        test_file = "test_christmas_list_print4.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create empty ChristmasList
        christmas_list = ChristmasList(test_file)
        
        # Print the list
        christmas_list.print_list()
        
        # Capture what was printed
        captured = capsys.readouterr()
        
        # Should print nothing
        assert captured.out == ""
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
    
    def test_print_list_all_purchased(capsys):
        """Test print_list when all items are purchased"""
        # Use a temporary file name
        test_file = "test_christmas_list_print5.pkl"
        
        # Clean up if exists
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Create ChristmasList and add items
        christmas_list = ChristmasList(test_file)
        christmas_list.add("Item1")
        christmas_list.add("Item2")
        
        # Check off both items
        christmas_list.check_off("Item1")
        christmas_list.check_off("Item2")
        
        # Print the list
        christmas_list.print_list()
        
        # Capture what was printed
        captured = capsys.readouterr()
        
        # Should show both items with x
        assert "[x] Item1\n" in captured.out
        assert "[x] Item2\n" in captured.out
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)

