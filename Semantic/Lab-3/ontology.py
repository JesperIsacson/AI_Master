from owlready2 import *
import owlready2

#Load the bacteria ontology file and store it in variable
onto = get_ontology("C://Users//isacs//source//repos//AI-Master//Semantic//Lab-3//bacteria.owl").load()

#Read all available classes in the ontology into a variable
ontologyClasses = list(onto.classes())
#Print all the classes
print(ontologyClasses)

#User input to decide what class to inspect futher
print("Input class to view subclasses")
userInputString = input()

#Find the class in the ontology with given input string by searching for the IRI
userInputClass = onto.search(iri = "*"+userInputString).first()

#Read all subclasses of the given class
subclasses = list(userInputClass.subclasses())

#Print the class's: definition, superclasses, subclasses, and instances
print(userInputClass.equivalent_to)
print(userInputClass.is_a)
print(subclasses)
print(userInputClass.instances())

#User input to choose to view data & object properties or not
print("View object and data properties?")
print("y/n")
userInputString = input()

#Check user input
if(str.lower(userInputString) == 'y'):
    #Read properties
    objectProperties = list(onto.object_properties())
    dataProperties = list(onto.data_properties())
    
    #Print properties
    print("all object propeties:")
    print(objectProperties)
    print("all data properties")
    print(dataProperties)

    #Print range and domain of object properties
    print("Domain and range of object properties:")
    for prop in objectProperties:
        print(str(prop.domain) + " >> " + str(prop.range))
    
    #Print range and domain of data properties
    print("Domain and range of data properties:")
    for prop in dataProperties:
        print(str(prop.domain) + " >> " + str(prop.range))

#Check user input
print("Run DL reasoning over the ontology?")
print("y/n")
userInputString = input()

#Locate Java runner
owlready2.JAVA_EXE = "C://Program Files//Eclipse Foundation//jdk-8.0.302.8-hotspot//bin//java.exe"
if(str.lower(userInputString) == 'y'):
    with onto:
        sync_reasoner()
    
    #Check for inconsistencies within the classes in the ontology
    inconsistencies = list(default_world.inconsistent_classes())
    print(inconsistencies)

    #Instance check every class
    for cl in ontologyClasses:
        print("instances of class: " + str(cl.name))
        print(onto.get_instances_of(cl))

#Load new ontology
onto = get_ontology("C://Users//isacs//source//repos//AI-Master//Semantic//Lab-3//bacteriaFamily.owl").load()

with onto:
    #Print the unknown_bacterium class
    print(onto.unknown_bacterium.__class__)
    rule = Imp()
    rule.set_name("Staphylococcus_Check")
    #Formulate the rule to check if a bacterium is a staphylococcus
    rule.set_as_rule("""Bacterium(?d), has_shape(?d, ?Round), has_grouping(?d, ?InCluster), gram_positive(?d, ?True) -> Bacterium(?d, ?Staphylococcus)""")
    sync_reasoner()
    print(onto.unknown_bacterium.__class__)