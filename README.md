# map.in-file-for-LAMMPS-Phonon-Dispersion
This repository contains the code to generate the map.in file essential for computing the phonon dispersion relation using the fix phonon command in LAMMPS. The map.in file maps atom IDs to lattice indices for any supercell, enabling accurate phonon calculations in molecular dynamics simulations.
Sure! Below is a detailed `README.md` file for your GitHub repository:

---

# map.in file for LAMMPS-Phonon-Dispersion

This repository contains the essential code to generate the `map.in` file required for computing the phonon dispersion relation using the `fix phonon` command in LAMMPS. The `map.in` file maps atom IDs to lattice indices for any supercell, enabling accurate phonon calculations in molecular dynamics simulations.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/durjoysarkardhrubo/map.in-file-for-LAMMPS-Phonon-Dispersion.git
    cd map.in-file-for-LAMMPS-Phonon-Dispersion
    ```

2. **Ensure you have Python installed**:
    - Python 3.x is required.
    - You can download and install Python from [here](https://www.python.org/downloads/).

## Usage

1. **Run the script**:
    ```sh
    python generate_map_in.py
    ```

2. **Provide the necessary inputs**:
    - When prompted, enter the replication factors along the x, y, and z axes (a, b, c).
    - Enter the number of atoms per unit cell (n).

3. **Example input**:
    ```
    Enter the replication along x axis (a): 5
    Enter the replication along y axis (b): 5
    Enter the replication along z axis (c): 1
    Enter the number of atoms per unit cell: 4
    ```
## Contact

Please contact me at [durjoy2003026@gmail.com](mailto:durjoy2003026@gmail.com) if you have any queries.
