from __future__ import division
import sys
import collections
import math
import operator

def CreateDT(data, infoGain, arcs):
    print("...build classifier...")
    #find the largest info gain.
    ig = max(infoGain.iteritems(), key=operator.itemgetter(1))[0]
    #print(ig)
    #find the split attributes
    spl_atts = arcs.get(ig)
    n_ig = dict(infoGain)
    del n_ig[ig]
    #iterate through
    for arc in arcs:
        temp = list(data)
        for t in temp:
            if arc not in t:
                temp.remove(t)
        b = True
        prev = temp[0][0]
        for t in temp:
            if prev != t[len(t)-1]:
                break
       #if b, we have a leaf
        if b:
            print(prev)
        else:
            CreateDT(temp, n_ig, arcs)
            
                
    

def calcInfoGain(data, attributes, target_class):
    print("...calculate the information gain...")
    #this method retruns two values. The information gain and the splitting attributes for each node
    gain_dic = {}
    split_dic = {}
    check_dic = {}
    #set target classes entropy
    c_index = attributes.index(target_class)
    class_dic = {}
    for t in data:
        if class_dic.has_key(t[c_index]):
            class_dic.update({t[c_index] : class_dic.get(t[c_index]) + 1})
        else:
            class_dic.update({t[c_index] : 1})
    entropyS = 0
    countS = sum(class_dic.values())
    for key in class_dic.keys():
        p = class_dic.get(key)/countS
        entropyS = entropyS - (p*(math.log(p, 2)))
    #print(entropyS)
   
    #set up gain dictionary with attributes
    c_index = attributes.index(target_class)
    for a in attributes:
        if a != target_class:
            gain_dic.update({a : entropyS});

    #get each attributes value count and calc gain
    for i in range(0, len(attributes)):
        if i != c_index:
            tran_dic = {}
            count_dic = {}
            for t in data:
                if tran_dic.has_key('{} {}'.format(t[i], t[c_index])):
                    tran_dic.update({'{} {}'.format(t[i], t[c_index]) : tran_dic.get('{} {}'.format(t[i], t[c_index]) ) + 1})
                else:
                    tran_dic.update({'{} {}'.format(t[i], t[c_index]) : 1})
                if count_dic.has_key(t[i]):
                    count_dic.update({t[i]: count_dic.get(t[i]) + 1})
                else:
                    count_dic.update({t[i] : 1})
            #print(tran_dic)
            #print(count_dic)

            #add the count dictinary to the split dictionary to be returned at the end
            split_dic.update({attributes[i] : count_dic})
            check_dic.update({attributes[i] : tran_dic})

            #order the dictionary
            ordered = collections.OrderedDict(sorted(tran_dic.items()))
        
            #find the gain for the attribute
            keys = ordered.keys()
            prev_key = keys[0].split()[0]
            dic = []
            top = 0
            bottom = 0
            count = 0
            entropy = 0
            for key in keys:
                if key.split()[0] == prev_key:
                    count += ordered.get(key)
                    top += 1
                    #print('Bottom:{}  Top: {}'.format(bottom, top))
                    #print("----------------------------------------")
                    if top == len(ordered.values()):
                        entropy = 0
                        for val in ordered.values()[bottom:top]:
                           #print(ordered.values()[bottom:top])
                            #print('Bottom:{}  Top: {}'.format(bottom, top))
                            #print("{}/{}".format(val, count))
                            p = val/count
                            entropy = entropy -( p*(math.log(p, 2)))
                            #print(entropy)
                            #print("----------------------------------------")
                        gain_dic.update({attributes[i] : gain_dic.get(attributes[i]) - ((count/countS)*entropy)})

                else:
                    #calculate the gain of the attribute and add it to the gain dictionary
                    entropy = 0
                    for val in ordered.values()[bottom:top]:
                        #print(ordered.values()[bottom:top])
                        #print('Bottom:{}  Top: {}'.format(bottom, top))
                        p = val/count
                        entropy =  entropy - (p*(math.log(p, 2)))
                        #print(entropy)
                        #print("----------------------------------------")
                    gain_dic.update({attributes[i] : gain_dic.get(attributes[i]) - ((count/countS)*entropy)})
                    
                    #move the position of the bottom to the top and change count
                    prev_key = key.split()[0]
                    bottom = top
                    top += 1
                    count = ordered.get(key)
            
    return gain_dic, split_dic
                        
        
    

if __name__ == "__main__":
    global class_att_values
    print("...main...")
   
    #open file
    filename = raw_input("Please enter the data's filename: ")
    f = None
    try:
        f = open(filename, 'r')
    except IOError:
        print("Cannot open {}. Check if it exists.".format(filename))
        sys.exit()

    #find if target attribute exists in file
    classname = raw_input("Please select a target attribute for classification: ")
    attributes = f.readline().split()
    if classname not in attributes:
        print("Target attribute does not exist in file. Please check your data and try again.")
        sys.exit()
    #print(attributes)

    #get the tuples
    tuples = []
    for line in f:
        if len(line.split()) > 0:
            tuples.append(line.split())
    #print(tuples)
    
    #calculate the Info gain for each attribute
    infoGain, arcs = calcInfoGain(tuples, attributes, classname)
    print(infoGain)
    print(arcs)
    
    #create the tree
    CreateDT(tuples, infoGain, arcs)
