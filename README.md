# Pictoralist
This Repository is python codebase that visualizes the output of the pfp-pipeline

## Install the pictoralist package globally

```sh
pip install pictoralist[/path/or/url/to/pictoralist-0.1.0-py3-none-any.whl]
```

## Installing the Pictoralist package in development mode

```sh
pip install -e [path/to/module/displaylab/pictoralist/python]
```
example

```sh
pip install -e /Users/uniquename/display-lab/pictoralist/pictoralist
```

## Running the pictoralist script 
```sh
 python -m pictoralist.pictoralist [/path/to/selected_message.json][/path/to/1_performers_all_measures.csv]
```

## Running the pfp pipeline (pfp.sh)
Note: This assumes that you installed the pfp pipeline installed and you have installed the esteemer package

```sh
cd $DISPLAY_LAB_HOME/vert-ramp-affirmation/vignettes/aspire
./$DISPLAY_LAB_HOME/vert-ramp-affirmation/pfp.sh
```
See vert-ramp-affirmation readme docs for more info




### Pictoralist
Pictoralist Visualizes the output of the PFP pipeline


#### Use (in progress):
Options:
- `-h | --help` print help and exit
- `-p | --pathways` path to causal pathways
- `-s | --spek` path to spek file (default to stdin)






