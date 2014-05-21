
Experiments

Based on
* https://github.com/w3c/csvw/blob/gh-pages/examples/simple-weather-observation.md
* https://github.com/w3c/csvw/blob/gh-pages/examples/graph-templating.md


* lib/uritemplate 		for uritemplate library
* lib/csvrdfize			crude example of template-based rdf generation
* samples/map1.ttlt		sample turtle-based template file
* samples/t1.csv		sample CSV data
* test1.py			demo python script embedding simple metadata; reads the above and generates
* output/_out.ttl		sample output


This is a simple piece of Python code that reads (a) basic metadata defining short names for CSV columns (b) a Turtle file whose URIs include URI Template column names
(c) CSV files. 
