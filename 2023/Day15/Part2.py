import re

with open('2023\Day15\input.txt') as f:
    sequence=f.read().split(',')

def parse_step(step):
    lens=re.search('[a-z]+',step).group()
    return convert_steps(lens),lens,re.search('(-|\d)',step).group()

def convert_steps(step):

    def hash_alg(char,start):
        return ((start+ord(char))*17)%256

    res=0
    for i in step:
        res=hash_alg(i,res) 
    return res

def check_box(b,l,f):
    if f.isdigit():        
        boxes[b][l]=int(f)
    else:
        boxes[b].pop(l, None)
    return

def box_power(b):
    power=0
    for i,k in enumerate(list(boxes[b].keys()),1):
        power+=(b+1)*i*boxes[b][k]
    return power
        

boxes=[{} for i in range(256)]

for s in sequence:
    box,lens,focal=parse_step(s)

    check_box(box,lens,focal)

total_power=[box_power(i) for i in range(256)]

print(sum(total_power))
    




