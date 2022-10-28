import sys
import warnings
import time
import logging
import json
import re
import numpy as np 
import matplotlib.pyplot as plt 

#from asyncore import read

import pandas as pd
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection
from rdflib.namespace import FOAF, RDF, RDFS, SKOS, XSD
from rdflib.serializer import Serializer
from rdfpandas.graph import to_dataframe
from SPARQLWrapper import XML, SPARQLWrapper
from .pictoralist_p import Pictoralist
f=open(sys.argv[1])
selected_message = json.load(f)
#print(type(content))
selected_message =json.dumps(selected_message)
performance_data_df = pd.read_csv(sys.argv[2])
pc=Pictoralist(selected_message,performance_data_df)
pc.create_graph()