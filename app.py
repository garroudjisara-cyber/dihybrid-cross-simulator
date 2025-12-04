import tkinter as tk
from tkinter import messagebox
from itertools import product

def calculate_dihybrid():
    # Get inputs
    p1 = entry_p1.get().strip().upper()
    p2 = entry_p2.get().strip().upper()

    # Validate input
    if len(p1) != 4 or len(p2) != 4:
        messagebox.showerror("Erreur", "Chaque génotype doit avoir 4 lettres (ex: AaBb)")
        return
    if not all(c in 'ABab' for c in p1 + p2):
        messagebox.showerror("Erreur", "Utilisez seulement A, a, B, b")
        return

    # Extract alleles
    gene1_p1 = sorted(p1[0] + p1[1])
    gene2_p1 = sorted(p1[2] + p1[3])
    gene1_p2 = sorted(p2[0] + p2[1])
    gene2_p2 = sorted(p2[2] + p2[3])

    # Generate gametes (4 per parent)
    gametes_p1 = [a + b for a in gene1_p1 for b in gene2_p1]
    gametes_p2 = [a + b for a in gene1_p2 for b in gene2_p2]

    # Generate 16 offspring
    offspring = []
    for g1 in gametes_p1:
        row = []
        for g2 in gametes_p2:
            geno1 = ''.join(sorted(g1[0] + g2[0]))
            geno2 = ''.join(sorted(g1[1] + g2[1]))
            row.append(geno1 + geno2)
        offspring.append(row)

    # Clear previous result
    for widget in result_frame.winfo_children():
        widget.destroy()

    # Title
    tk.Label(result_frame, text="Dihybrid Cross 4×4 – Sara Garroudji", font=("Arial", 16, "bold"), fg="darkblue").grid(row=0, column=0, columnspan=6, pady=15)

    # Header (Parent 2 gametes)
    tk.Label(result_frame, text="", width=10).grid(row=1, column=0)
    for i, g in enumerate(gametes_p2):
        tk.Label(result_frame, text=g, font=("Arial", 12, "bold"), width=10).grid(row=1, column=i+1)

    # Phenotype colors
    colors = {
        "AABB": "#90EE90", "AABb": "#90EE90", "AaBB": "#90EE90", "AaBb": "#90EE90",  # Green: AB
        "AAbb": "#FFFF99", "Aabb": "#FFFF99",                                      # Yellow: Ab
        "aaBB": "#FFB6C1", "aaBb": "#FFB6C1",                                      # Pink: aB
        "aabb": "#FFFFFF"                                                          # White: ab
    }

    # Display grid
    for i, g1 in enumerate(gametes_p1):
        tk.Label(result_frame, text=g1, font=("Arial", 12, "bold"), width=10).grid(row=i+2, column=0)
        for j, geno in enumerate(offspring[i]):
            bg = colors.get(geno, "#FFFFFF")
            tk.Label(result_frame, text=geno, font=("Arial", 11), relief="solid", width=10, height=2, bg=bg).grid(row=i+2, column=j+1, padx=2, pady=2)

    # Classic ratio
    tk.Label(result_frame, text="\nRatio phénotypique classique → 9:3:3:1", font=("Arial", 14, "bold"), fg="purple").grid(row=7, column=0, columnspan=6, pady=10)

# Main window
root = tk.Tk()
root.title("Dihybrid Cross Simulator – Sara Garroudji PhD")
root.geometry("850x750")
root.configure(bg="#f0f8ff")

# Title
tk.Label(root, text="Dihybrid Cross Simulator", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="darkblue").pack(pady=20)

# Input frame
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

tk.Label(frame, text="Parent 1 :", font=("Arial", 14), bg="#f0f8ff").grid(row=0, column=0, padx=10)
entry_p1 = tk.Entry(frame, font=("Arial", 14), width=10)
entry_p1.grid(row=0, column=1)
entry_p1.insert(0, "AaBb")

tk.Label(frame, text="Parent 2 :", font=("Arial", 14), bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=10)
entry_p2 = tk.Entry(frame, font=("Arial", 14), width=10)
entry_p2.grid(row=1, column=1)
entry_p2.insert(0, "AaBb")

tk.Button(frame, text="Calculate Dihybrid Cross", font=("Arial", 14), bg="darkblue", fg="white", command=calculate_dihybrid).grid(row=2, column=0, columnspan=2, pady=20)

# Result frame
result_frame = tk.Frame(root, bg="#f0f8ff")
result_frame.pack(fill="both", expand=True, padx=20)

# Footer
tk.Label(root, text="Made with ❤️ by Sara Garroudji – PhD Biology & Genetics 2025", bg="#f0f8ff", fg="gray").pack(side="bottom", pady=10)

root.mainloop()