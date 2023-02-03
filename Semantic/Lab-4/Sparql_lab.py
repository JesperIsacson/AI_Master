from SPARQLWrapper import SPARQLWrapper, JSON

def printjson(result):
    body = result.popitem() 

    information = body[1]
    bindings = information.get('bindings')

    for item in bindings:
        print(item)


sparqlSwedishComedians = SPARQLWrapper("http://dbpedia.org/sparql")
sparqlSwedishComedians.setReturnFormat(JSON) 

print("Swedish Comedians:")
sparqlSwedishComedians.setQuery("""
    SELECT ?person
    {
        ?person dbo:occupation dbr:Comedian ;
        dbp:nationality ?nationality
        FILTER(?nationality = "Swedish"@en)
    }
""")

res = sparqlSwedishComedians.queryAndConvert()
printjson(res)

sparqlStarringEddieMurphy = SPARQLWrapper("http://dbpedia.org/sparql") 
sparqlStarringEddieMurphy.setReturnFormat(JSON)  

print("Movies with Eddie Murphy as a starring role:")
sparqlStarringEddieMurphy.setQuery("""
    SELECT ?movie
    {
        ?movie rdf:type dbo:Film ;
        dbo:starring ?actor
        FILTER(?actor = dbr:Eddie_Murphy)
    }
""")

result = sparqlStarringEddieMurphy.queryAndConvert()
printjson(result) 

