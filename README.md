
Experiments

inspired by https://github.com/w3c/csvw/blob/gh-pages/examples/graph-templating.md


lib/ 		for uritemplate library
map1.ttlt	sample turtle-based template file
t1.csv		sample CSV data
rdfize1.py	demo python script embedding simple metadata; reads the above and generates
_out.ttl	sample output

e.g. ./rdfize1.py | turtle > _cleanoutput.nt

('turtle' is a simple turtle parser included with Jena, here just confirming we can parse the output)
