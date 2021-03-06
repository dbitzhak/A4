pred_file_name = "save_output.txt"
gold_file_name = "data/TRAIN.annotations"
sentnce_to_relation = {}
gold_items = set()
pred_set = set()

def remove_dot(st):
    if st[-1] == '.':
        return st[:-1]
    if st.endswith("\'s"):
        return st[:-2]
    return st

with open(gold_file_name) as f:
    for line in f:
        if "Live_In" in line:
            line = line.split("\t")
            sen_num = line[0]
            per = line[1]
            loc = line[3]
            per = remove_dot(per)
            loc = remove_dot(loc)
            sentnce_to_relation[sen_num] = sentnce_to_relation.get(sen_num,list())
            sentnce_to_relation[sen_num].append((per,loc))
            if (sen_num, per, loc) in gold_items:
                print("duplicate ",(sen_num, per, loc))
            gold_items.add((sen_num, per, loc))
good =0.0
bad =0.0
with open(pred_file_name,"r") as f:
    for line in f:
            line = line.strip().split("\t")
            per = line[1]
            loc = line[3]
            per = remove_dot(per)
            loc = remove_dot(loc)
            sen_num = line[0]
            pred_set.add((sen_num,per,loc))
            if sen_num in sentnce_to_relation:
                for pair  in sentnce_to_relation[sen_num]:

                    if (per,loc) == pair:
                        good += 1
                    else:
                        bad += 1
                        print(sen_num,per,loc)


prec = good / (good + bad)
recall = 1 - len(gold_items - pred_set) / len(gold_items)

print()
print()
print ("missed relations")
for mis_ele in (gold_items - pred_set):
    print( mis_ele  )

print("good", good)
print("len of all Live in ", len(gold_items))

print ("prec " + str(prec))
print ("recall " + str(recall))
