"""Tools tests"""

import pytest
import tempfile
from pathlib import Path

class TestFileOperations:
    """Tests for FileOperations."""
    
    def test_read_write(self):
        """Test reading and writing files."""
        from tools.file_ops import FileOperations
        
        with tempfile.TemporaryDirectory() as tmpdir:
            ops = FileOperations(tmpdir)
            
            # Write file
            ops.write("test.txt", "Hello, World!")
            
            # Read file
            content = ops.read("test.txt")
            assert content == "Hello, World!"
    
    def test_edit(self):
        """Test editing files."""
        from tools.file_ops import FileOperations
        
        with tempfile.TemporaryDirectory() as tmpdir:
            ops = FileOperations(tmpdir)
            ops.write("test.txt", "Hello, World!")
            ops.edit("test.txt", "World", "Python")
            content = ops.read("test.txt")
            assert content == "Hello, Python!"

class TestCodeRunner:
    """Tests for CodeRunner."""
    
    def test_run_python(self):
        """Test running Python code."""
        from tools.code_runner import CodeRunner
        
        runner = CodeRunner()
        result = runner.run("print('Hello')")
        assert result.success
        assert "Hello" in result.stdout
    
    def test_run_invalid_code(self):
        """Test running invalid code."""
        from tools.code_runner import CodeRunner
        
        runner = CodeRunner()
        result = runner.run("invalid syntax here!!!")
        assert not result.success

class TestSearch:
    """Tests for Search."""
    
    def test_find_files(self):
        """Test finding files."""
        from tools.search import Search
        
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test files
            Path(tmpdir, "test1.py").touch()
            Path(tmpdir, "test2.py").touch()
            Path(tmpdir, "readme.md").touch()
            
            search = Search(tmpdir)
            py_files = search.find_files("*.py")
            assert len(py_files) == 2
