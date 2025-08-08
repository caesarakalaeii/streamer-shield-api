# Streamer Shield AI Training

This project provides tools and scripts for training and serving an AI model for streamer shield functionality. It includes Python scripts for training, data generation, and a REST API for model inference.

## Project Structure
- `auto_train.py`, `train.py`, `streamer_shield_train.py`: Training scripts
- `classification_helper.py`, `data_generator.py`, `vocab.py`, `vocabulary_5.json`: Helper modules and data
- `streamer_shield_rest.py`: REST API server
- `Dockerfile`: Containerization setup
- `requirements.txt`: Python dependencies

## Getting Started

### Prerequisites
- Python 3.12
- Docker (optional, for containerized deployment)

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd streamer-shield-api
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage
#### Training
Run any of the training scripts as needed:
```sh
python train.py
```

#### REST API
To start the REST API server:
```sh
python streamer_shield_rest.py
```
The server will run on port `38080` by default.

#### Docker
To build and run the Docker container:
```sh
# Build the image
docker build -t streamer-shield-api .

# Run the container
docker run -p 38080:38080 streamer-shield-api
```

## Environment Variables
- `PORT`: (optional) The port number for the REST API server. Defaults to `38080` if not set.

To run the server on a custom port, set the environment variable before starting:
```sh
export PORT=5000  # On Linux/macOS
set PORT=5000     # On Windows
python streamer_shield_rest.py
```

## Contributing
Feel free to open issues or submit pull requests for improvements.

## License
Specify your license here.
