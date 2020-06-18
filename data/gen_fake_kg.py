import numpy as np
import random


readable_dict = {"RelatedTo": "is related to", "FormOf" : "is form of", "IsA":"is a", "PartOf": "is part of", "HasA":"has a", 
                "UsedFor":"is used for","CapableOf":"is capable of", "AtLocation":"is at","Causes":"causes", "MannerOf" : "is manner of", 
                "HasSubevent":"has subevent", "LocatedNear":"is located near", "HasContext" : "has context", "SimilarTo" : "is similar to", 
                 "EtymologicallyRelatedTo" : "is etymologically related to", "CausesDesire" : "causes desire", 
                 "MadeOf" : "is made of",  "ReceivesAction" : "receives action","HasFirstSubevent": "has first subevent of",
                 "HasLastSubevent" : "has last subevent of", "HasPrerequisite" :"has prerequisite for", 
                 "HasProperty": "has property", "MotivatedByGoal" : "is motivted by", "ObstructedBy": "is obstructed by", 
                 "Desires": "desires","CreatedBy": "is created by","Synonym": "is synonym of", 
                 "Antonym ": "is antonym of","DistinctFrom":"is distinct from","DerivedFrom":"is derived from",
                "SymbolOf":"is symbol of","DefinedAs":"is defined as"}

inverse_dict=dict([val,key] for key,val in readable_dict.items())
del(inverse_dict["is a"])
inverse_dict["is a "] = "IsA"


with open("./knog.txt", "r") as fstd:
    with open("./knog_neg.txt", "w", encoding="utf-8") as fout:
        with open("gpt2_gentext.txt", "r", encoding="utf-8") as fin:
            keywords = inverse_dict.keys()
            out_list = []
            gold_list = fstd.readlines()
            for line in fin:
                if line == '\n' or '===' in line:
                    continue
                if line not in gold_list or len(line) > 100:
                    label = False
                    for key in keywords:
                        if key in line:
                            label = True
                    if (label):
                        continue
                    out_list.append(line)
                            
            out_set = set(out_list)
            out_list = list(out_set)
            for line in out_list:
                fout.write(line)



    
 

with open("./knog.txt", "r") as fin:
    with open("./knog_repeat.txt", "w") as fout:
        keywords = inverse_dict.keys()
        for sen in fin:
            for pattern in keywords:
                if pattern in sen:
                    if pattern == "is a ":
                        pattern = "is a"
                    start,end = sen.split(pattern,1)
                    repeat = np.random.choice([start.strip(), end.replace('.','').replace('\n','').strip()])
                    fout.write(repeat + " " + pattern + ' ' + repeat + '\n')
                    break



with open("./knog.txt", "r") as fin:
    with open("./knog_replace.txt", "w") as fout:
        keywords = inverse_dict.keys()
        start_list, end_list = [], []
        for sen in fin:
            for pattern in keywords:
                if pattern in sen:
                    start,end = sen.split(pattern,1)
                    start_list.append(start.strip())
                    end_list.append(end.replace('.','').replace('\n','').strip())
                    break
        
        np.random.shuffle(start_list)
        np.random.shuffle(end_list)


with open("./knog.txt", "r") as fin:
    with open("./knog_replace.txt", "w") as fout:
        count = 0
        for sen in fin:
            for pattern in keywords:
                if pattern in sen:
                    if pattern == "is a ":
                        pattern = "is a"
                    fout.write(start_list[count] + " " + pattern + ' ' + end_list[count] + '\n')
                    count += 1
                    break

        