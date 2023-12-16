with open('2023\Day15\input.txt') as f:
    sequence=f.read().split(',')

def convert_steps(step):

    def hash_alg(char,start):
        return ((start+ord(char))*17)%256

    res=0
    for i in step:
        res=hash_alg(i,res) 
    return res

seq_sum=0
for s in sequence:
    seq_sum+=convert_steps(s)
print(seq_sum)