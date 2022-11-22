# Effective and Stable Role-based Multi-Agent Collaboration by Structural Information Principles.<br>
The ``SIRD`` is a mathematical structural information principles-based role discovery method, and the ``SR-MARL`` is a SIRD optimizing MARL framework for multi-agent collaboration.<br>
The implementation is written in ``Pytorch`` and based on ``PyMARL`` and ``SMAC``.<br>
Ths source code and partial experimental results are respectively shown in ``src`` and ``result``.<br>
## Installation instructions
Build the Dockerfile using<br>
```python
cd docker
bash build.sh
```
Set up StarCraft II and SMAC:<br>
```python
bash install_sc2.sh
```
This will download SC2 into the 3rdparty folder and copy the maps necessary to run over.<br>
## Run an experiment
```python
python src/main.py --config=sr_marl --env-config=sc2 with env_args.map_name=2c_vs_64zg t_max=5050000
```
All results will be stored in the ``result`` folder.
