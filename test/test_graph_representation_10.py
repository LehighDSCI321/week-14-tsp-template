import pytest
from collections import defaultdict
from student_code import TSPGraph  
import time
import math

def test_max_flow():
    st=TSPGraph()
    t = time.time()
    nodes=["a","b","c","d"]
    loc={}
    loc={'a': (37, 70), 'b': (7, 9), 'c': (7, 83), 'd': (42, 77)}
    for nd in nodes:
        for nd2 in nodes:
            loc1=loc[nd]
            loc2=loc[nd2]
            st.add_edge(nd,nd2,edge_weight=math.sqrt((loc1[0]-loc2[0])**2+(loc1[1]-loc2[1])**2) )
    CApprox=st.tsp_approx("a")
    CApproxPath=CApprox[0]
    elapsed = time.time() - t
    CApproxPath.append("a")
    assert elapsed <0.1,"Your code took to long"
    assert abs(CApprox[1]-186.1)<1, "Your code did not produce the correct result"
    assert set(CApprox[0])==set(nodes), "Your path did not visit all the nodes"
    assert CApprox[0][0]=='a',"The path must start at node a"