# Function to generate the map.in file for a given supercell
def generate_map_file(a, b, c, n, file_path="map.in"):
    with open(file_path, "w") as f:
        # Write the header
        f.write(f"{a} {b} {c} {n}\n")
        f.write(f"# Map file for {a}x{b}x{c} cell.\n")
        
        atom_index = 1
        # Iterate over each unit cell in the supercell
        for z in range(c):
            for y in range(b):
                for x in range(a):
                    # For each unit cell, write the coordinates and atom identification
                    for atom_id in range(n):
                        f.write(f"{x} {y} {z} {atom_id} {atom_index}\n")
                        atom_index += 1

# Main function to get user inputs and generate the map file
if __name__ == "__main__":
    # Get user inputs
    a = int(input("Enter the replication along x axis (a): "))
    b = int(input("Enter the replication along y axis (b): "))
    c = int(input("Enter the replication along z axis (c): "))
    n = int(input("Enter how many atoms per unit cell: "))
    
    # Generate the map file
    generate_map_file(a, b, c, n)

