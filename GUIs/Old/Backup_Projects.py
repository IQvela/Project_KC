# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:18:35 2021

@author: refor
"""
# import os
import pickle


def save_pr(Pr_l,filepath,filename):
    # default_path=def_path
    # if def_path=="":
    #     default_path=os.getcwd()
    with open("{}\{}.pkl".format(filepath,filename),"wb") as f:
        pickle.dump(Pr_l,f)      

def load_pr(filepath,filename):
    # default_path=def_path
    # if def_path=="":
    #     default_path=os.getcwd()
    Pr_l=[]
    with open("{}\{}.pkl".format(filepath,filename),"rb") as f:
        Pr_l=pickle.load(f)
    return Pr_l