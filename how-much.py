# I always thought that my old friend John was rather richer than he looked, but I never knew exactly how much money he actually had. 
# One day (as I was plying him with questions) he said: "Imagine I have between m and n Zloty (or did he say Quetzal? I can't remember!)

# If I were to buy 9 cars costing c each, I'd only have 1 Zlotty (or was it Meticals?) left.

# And if I were to buy 7 boats at b each, I'd only have 2 Ringglets (or was it Zlotty?) left.

# Could you tell me in each possible case:

# how much money f he could possibly have
# the cost c of a car
# the cost b of a boat?
# So, I will have a better idea about his fortune. Note that if m-n is big enough, you might have a lot of possible answers.

# Each answer will be given as ["M: f", "B: b", "C: c"] and all the answers as [ ["M: f", "B: b", "C: c"] ... ]. M stands for "Money", B for boats, C for cars.

# m and n are positive or null integers with m <= n or m >= n, m and n inclusive.

# Examples:

# howmuch(1, 100) => [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]]
# howmuch(1000, 1100) => [["M: 1045", "B: 149", "C: 116"]]
# howmuch(10000, 9950) => [["M: 9991", "B: 1427", "C: 1110"]]
# howmuch(0, 200) => [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]]

def howmuch(m, n):
    result = []
    for i in range(min(m,n),max(m,n)+1):
            if i % 9 == 1 and i % 7 == 2:
                result.append(["M: "+str(i), "B: "+str(int((i-2)/7)), "C: "+str(int((i-1)/9))])
    return result
    
# Another shorter solution is

def howmuch(m, n):    
    return [['M: %d'%i, 'B: %d'%(i/7), 'C: %d'%(i/9)] for i in range(min(m,n), max(m,n)+1) if i%7 == 2 and i%9 == 1]
    
