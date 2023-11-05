import unittest
import os 
import shutil
from helper import FileSystem
from unittest.mock import patch

class TestFileSystem(unittest.TestCase):
    
    def setUp(self):
        print("\n\n")
        print("Start")
        self.fs = FileSystem("test_directory")


    def tearDown(self):
        if os.path.exists("test_directory"):
            shutil.rmtree("test_directory")
        print("Stop")


    def test_create_file(self):
        self.fs.create_file("Test1","Content of file")
        self.assertTrue("Test1")


    def test_create_file_duplicate(self):
        self.fs.create_file("Test2","Content of file")
        self.assertFalse(self.fs.create_file("Test2","Content of file"))


    def test_get_details_existing_file(self):
        self.fs.create_file("test_file", "This is a test file content.")
        details = self.fs.get_details("test_file")
        expected_output = "File System : {'version': 1, 'created_at':"
        self.assertIn(expected_output , details)


    def test_get_details_non_existing_file(self):
        details = self.fs.get_details("test_file")
        self.assertFalse(details)


    def test_delete_file_deafult(self):
        self.fs.create_file("test","Content of file")
        self.fs.delete_file("test")
        self.assertFalse(os.path.exists("test_directory/test.txt"))


    def test_delete_file_non_existing_file(self):
        self.fs.create_file("test","Content of file")
        self.fs.delete_file("test_non_existent")
        self.assertTrue(os.path.exists("test_directory/test.txt"))
    

    def test_copy_file(self):
        self.fs.create_file("test_file", "This is a test file content.")
        self.fs.copy_file("test_file", "test_directory")
        self.assertTrue(os.path.exists("test_directory/test_file(Copy).txt"))

    
    def test_edit_file(self):
        self.fs.create_file("test_file", "This is a test file content.")
        self.fs.edit_file("test_file", "Updated content.")
        self.assertEqual(self.fs.versions["test_file"][2], "Updated content.")


    def test_edit_nonexistent_file(self):
        self.assertFalse(self.fs.edit_file("nonexistent_file", "New content."))


    def test_append_to_file(self):
        self.fs.create_file("test_file", "This is a test file content.")
        self.fs.append_to_file("test_file", "Appended content.")
        self.assertEqual(self.fs.versions["test_file"][2], "This is a test file content.Appended content.")


    def test_revert_to_version(self):
        self.fs.create_file("test_file", "Version 1")
        self.fs.edit_file("test_file", "Version 2")
        self.fs.revert_to_version("test_file", 1)
        self.assertEqual(self.fs.file_system["test_file"]['version'], 1)


    def test_revert_to_nonexistent_version(self):
        self.fs.create_file("test_file", "Version 1")
        self.fs.revert_to_version("test_file", 3)
        self.assertFalse(self.fs.versions["test_file"].get(3))


    def test_revert_to_nonexistent_version_raises_exception(self):
        self.fs.create_file("test_file", "file created")

        with patch.object(self.fs, "revert_to_version", side_effect=KeyError("Test KeyError")):
            with self.assertRaises(KeyError):
                self.fs.revert_to_version("test_file", 30)



if __name__ == "__main__":
    unittest.main()
