def rec_ep(state):
    curr=nfa[state][-1]
    if(curr==None):
        return
    else:
        if(type(curr)==set):
            for st in curr:
                if(st in dfa_st):
                    continue
                dfa_st.add(st)
                rec_ep(st)
        else:
            if curr in dfa_st:
                return
            dfa_st.add(curr)
            rec_ep(curr)
        return



alphapet={'a','ep'}

nfa={
    'q1':[None,{'q1','q2','q4'}],
    'q2':['q3','q2'],
    'q3':[None,{'q2','q3','q4'}],
    'q4':[None,'q4']
    }

nfa_start_st='q1'
nfa_accepted=['q4']
dfa_st=set({nfa_start_st})
rec_ep(nfa_start_st)
dfa_states=[dfa_st]
dfa={}



for curr in dfa_states:
    tmp=[None]*(len(alphapet)-1)
    for i in range(len(tmp)):
        dfa_st=set()
        for sing_st in curr:
            curr_trans=nfa[sing_st][i]
            if curr_trans == None:
                continue
            elif(type(curr_trans)==set):
                for st in curr_trans:
                    dfa_st.add(st)
                    rec_ep(st)
            else:
                dfa_st.add(curr_trans)
                rec_ep(curr_trans)
        tmp[i]=dfa_st
        if(dfa_st not in dfa_states and len(dfa_st)>0):
            dfa_states.append(dfa_st)
    dfa[frozenset(curr)]=tmp
dfa_accepted=[]
for i in dfa:
    for j in i:
        if(j in nfa_accepted):
            dfa_accepted.append(i)
print(dfa_accepted)
