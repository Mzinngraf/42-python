import importlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def check_packages() -> bool:
    required = ["pandas", "numpy", "matplotlib"]
    print("LOADING STATUS: Loading programs...")
    all_ok = True

    for lib in required:
        try:
            module = importlib.import_module(lib)
            # Exibe a versão conforme solicitado no briefing
            print(f"[OK] {lib} ({module.__version__}) - Ready")
        except ImportError:
            print(f"[ERROR] {lib} is missing!")
            all_ok = False

    return all_ok


def run_analysis() -> None:
    try:
        print("Analyzing Matrix data...")
        # Cria dados simulados usando numpy
        data = np.random.randn(100)
        df = pd.DataFrame(data, columns=['Signal'])

        # Gera e salva a visualização
        plt.figure(figsize=(10, 6))
        plt.plot(df['Signal'], color='green')
        plt.title("Matrix Data Stream Analysis")
        plt.savefig("matrix_analysis.png")

        print("Analysis complete! Results saved to: matrix_analysis.png")

    except Exception as e:
        print(f"An error occurred during analysis: {e}")


if __name__ == "__main__":
    if check_packages():
        run_analysis()
    else:
        print("\nFail: Please install dependencies using:")
        print("pip install -r requirements.txt OR poetry install")
