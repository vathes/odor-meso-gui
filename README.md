# odor-meso-gui
Graphical interface for odor meso experiments for Reimer Lab and Pfaffinger Lab at BCM.

# Running with python virtual environment

1. Clone repository
```bash
git clone https://github.com/reimerlab/odor-meso-gui.git
```

2. Set up virtual environment with pip or conda

3. Inside the virtual env, go to the cloned directory and

```bash
pip install -e .
```

4. Set up dj.config globally

5. run the server with

```bash
python odor_meso_gui/index.py
```
6. Go to 0.0.0.0:8000 in your browser to start using the GUI

# Running with docker

1. Clone repository
```bash
git clone https://github.com/reimerlab/odor-meso-gui.git
```
2. Go to the directory you just cloned.
3. Copy `.env_template` as `.env` and fill in the credentials
4. `docker-compose up -d`
5. Go to 0.0.0.0:8000 in your browser to start using the GUI

# How to update if running with Docker?

1. go to the directory `odor-meso-gui`
2. git pull
3. `docker-compose down`
4. `docker-compose up -d --build`
