# ATSP Project
A full rewrite of the federated learning enviroment we were provided, which did not work and was undocumented.

## Configuration
The server dictates how many clients are expected, then this many client notebooks should be ran (in parallel).

## Running

### Python venv
In order to use the virtual environment, create a virtual environment using `python -m venv .venv`, run it using `source .venv/bin/activate`, then install the requirements using `pip install -r requirements.txt`.

### Server
Open the file `ServerRewrite.ipynb`, select the virtual environment kernel, and run all cells.

See the top cell for configuration options.

### Client
Open the file `ClientRewrite.ipynb`, select the virtual environment kernel, and run all cells.

See the top cell for configuration options.

### Backdoor Client
This client requires some additional knowledge, the client count. Eta should remain 1. Further it can be configured which label the backdoor client should remap.