#!/usr/bin/env python3
"""
Execute a Jupyter notebook by extracting and running code cells
"""
import json
import sys
from pathlib import Path

def run_notebook(notebook_path):
    """Execute all code cells in a notebook"""
    import os

    print(f"\n{'='*70}")
    print(f"Ejecutando: {notebook_path}")
    print(f"{'='*70}\n")

    # Get absolute path and change to notebook's directory
    notebook_path = Path(notebook_path).resolve()
    notebook_dir = notebook_path.parent

    os.chdir(notebook_dir)
    print(f"Working directory: {notebook_dir}\n")

    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # Extract code cells
    code_cells = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            code = ''.join(cell['source'])
            # Remove IPython magic commands
            lines = code.split('\n')
            filtered_lines = []
            for line in lines:
                # Skip magic commands
                if line.strip().startswith('%'):
                    continue
                # Replace display() with print()
                if 'display(' in line:
                    line = line.replace('display(', 'print(')
                filtered_lines.append(line)
            code = '\n'.join(filtered_lines)
            if code.strip():  # Skip empty cells
                code_cells.append(code)

    # Create combined script
    full_code = '\n\n'.join(code_cells)

    # Execute with matplotlib non-interactive backend
    import matplotlib
    matplotlib.use('Agg')

    exec_globals = {'__name__': '__main__'}
    exec(full_code, exec_globals)

    print(f"\n{'='*70}")
    print(f"✅ Notebook completado: {notebook_path}")
    print(f"{'='*70}\n")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python run_notebook.py <notebook_path>")
        sys.exit(1)

    notebook_path = sys.argv[1]
    if not Path(notebook_path).exists():
        print(f"Error: {notebook_path} not found")
        sys.exit(1)

    run_notebook(notebook_path)
