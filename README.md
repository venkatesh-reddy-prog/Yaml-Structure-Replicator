📁 **YAML Structure Replicator**\\
Intelligent Folder and YAML File Structure Replication with Data Integrity.

The YAML Structure Replicator is a Python utility designed to duplicate a source directory structure into a destination directory, with a powerful focus on replicating and merging content within YAML configuration files while preserving existing data.

✨ Key Features:
Full Structure Replication: Duplicates the entire folder and file hierarchy from the source path to a new destination path.

YAML-Aware Merging: Specifically targets .yaml and .yml files, ensuring that any structural or key-value modifications from the source are applied to the destination.

Data Integrity Preservation (Non-Destructive Merge): The core feature is its ability to apply new keys and structure updates from the source YAML files to the destination without altering or deleting existing, custom data in the destination. This is crucial for maintaining base configurations (source) across multiple, unique environment configurations (destination).

Other File Handling: Files other than YAML are simply copied directly.

🚀 **Installation**:
This project is a Python script and can be set up easily by cloning the repository.

**Prerequisites**
Python 3.x

Steps
Clone the Repository:

Bash

git clone https://github.com/venkatesh-reddy-prog/Yaml-Structure-Replicator.git
cd Yaml-Structure-Replicator
Install Dependencies:
You will need the PyYAML library for parsing YAML files.

Bash

pip install pyyaml
(Note: If a requirements.txt file is present in the repository, use pip install -r requirements.txt instead.)

**🛠️ Usage**
The tool is executed by running the main Python script and providing the paths for the source and destination folders.

Command Syntax
Bash

python <SCRIPT_NAME> <SOURCE_FOLDER_PATH> <DESTINATION_FOLDER_PATH>
Replace <SCRIPT_NAME> with the actual entry point of the script (e.g., main.py or the relevant file within the Task1 directory).

Example Scenario
This example demonstrates how the replicator merges new structure while preserving existing custom data.

Action	Source File (./template/config.yaml)	Destination File (./env_dev/config.yaml)
Initial State	default_timeout: 10	(Folder does not exist yet)
Run 1: Replication	default_timeout: 10	Result: default_timeout: 10
Manual Update	(No change)	default_timeout: 5 (Custom data)
Source Update	default_timeout: 10\nnew_key: true (New key added)	default_timeout: 5
Run 2: Replication	default_timeout: 10\nnew_key: true	Final Result: default_timeout: 5\nnew_key: true

Export to Sheets
The custom value of 5 was preserved, and the new key (new_key: true) was successfully added.

🤝 Contributing
We welcome contributions! If you have suggestions for improving the merging logic, handling more complex YAML structures, or streamlining the utility, please feel free to:

Fork the repository.

Create a feature branch (git checkout -b feature/your-feature).

Commit your changes.

Open a Pull Request.

