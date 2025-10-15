📁 YAML Structure Replicator:

Intelligent Folder and YAML File Structure Replication with Data Integrity.

The YAML Structure Replicator is a Python utility designed to duplicate a source directory structure into a destination directory, with a powerful focus on replicating and merging content within YAML configuration files while preserving existing data.

✨ Key Features

Full Structure Replication: Duplicates the entire folder and file hierarchy from the source path to a new destination path.

YAML-Aware Merging: Specifically targets .yaml and .yml files, ensuring that any structural or key-value modifications from the source are applied to the destination.

Data Integrity Preservation (Non-Destructive Merge): The core feature is its ability to apply new keys and structure updates from the source YAML files to the destination without altering or deleting existing, custom data in the destination. This is crucial for maintaining base configurations (source) across multiple, unique environment configurations (destination).

Other File Handling: Files other than YAML are simply copied directly.

🚀 Installation:

This project is a Python script and can be set up easily by cloning the repository.

Prerequisites:

Python 3.x

Steps

1) Clone the Repository:
   
git clone https://github.com/venkatesh-reddy-prog/Yaml-Structure-Replicator.git

cd Yaml-Structure-Replicator

3) Install Dependencies:
   
You will need the PyYAML library for parsing YAML files.

pip install pyyaml

🛠️ Usage:

The tool is executed by running the main Python script and providing the paths for the source and destination folders.

Command Syntax:

python <SCRIPT_NAME> <SOURCE_FOLDER_PATH> <DESTINATION_FOLDER_PATH>

Replace <SCRIPT_NAME> with the actual entry point of the script (e.g., main.py or the relevant file within the Task1 directory).

🤝 Contributing:

We welcome contributions! If you have suggestions for improving the merging logic, handling more complex YAML structures, or streamlining the utility, please feel free to:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes.
Open a Pull Request.

