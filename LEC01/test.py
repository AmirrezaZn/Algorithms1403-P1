import ipytest
import nbformat
from nbconvert import PythonExporter
import pytest


def load_notebook_functions(notebook_path):
    import nbformat

    # Open the notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)

    # Dictionary to store global variables/functions from the notebook
    global_vars = {}

    # Loop through all cells in the notebook
    for cell in notebook.cells:
        if cell.cell_type == "code":  # Only process code cells
            print(f"Executing cell:\n{cell.source}\n")  # Print the cell content
            try:
                exec(cell.source, global_vars)  # Execute the cell
            except Exception as e:
                print(f"Error in cell:\n{cell.source}\nError: {e}")
    
    return global_vars


# Function to execute a Jupyter Notebook and extract the defined variables/functions
def load_notebook(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)

    # Extract and execute Python code from notebook cells
    exporter = PythonExporter()
    code, _ = exporter.from_notebook_node(notebook)
    
    # Execute the code in the global namespace


# Load and execute the notebook
notebook_path = "LEC01.ipynb"
load_notebook(notebook_path)
m=load_notebook_functions(notebook_path)
# Sample test cases for the notebook's functions
def test_karatsuba():
    if "gradeSchoolMult" in m:  # Replace with your function name
        result = m["gradeSchoolMult"](1234567, 654321)
        print("Result:", result)
        assert result==1234567*654321
    else:
        print("Function not found in notebook!")
    

if __name__ == "__main__":
    ipytest.run()
