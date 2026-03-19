import subprocess
import os

def convert_to_pdf(notebook_files):
    for notebook in notebook_files:
        if not os.path.exists(notebook):
            print(f"File {notebook} not found, skipping...")
            continue
            
        print(f"Converting {notebook} to PDF...")
        try:
            # Using 'webpdf' since 'pdf' (LaTeX) is not installed on this system.
            # webpdf requires playwright or pyppeteer.
            result = subprocess.run(
                ["jupyter", "nbconvert", "--to", "webpdf", notebook],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"Successfully converted {notebook} to PDF.")
            else:
                print(f"Error converting {notebook}:")
                print(result.stderr)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    notebooks = [
        "MultiLayerPerceptrons_Workshop.ipynb",
        "MultiLayeredPerceptrons.ipynb"
    ]
    convert_to_pdf(notebooks)
