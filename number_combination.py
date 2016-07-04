ops = ["",'+','-','*','/']
actops = ['+','-','*','/']

'''main function that adds operation, call bracket functions 
and compiles final list'''
# sets up the intial values for the later functions
def start(ns):
   global numbers, n
   # str of intial numbers
   numbers = ns
   # tracks which number in the str is the current one
   n = 1
   # main loop function and where it should start
   addops(numbers[0])

# adds the the current number on to all the current combinations
def addops(current):
   # empty list of possible combinations
   new = []
   global n
   # goes through all current combinations and then the different operations
   for k in range(len(current)):
     for i in range(len(ops)):
          new += [current[k]+ops[i]+numbers[n]]
   n += 1
   # check to see if we have gotten to the end of the numbers
   if n < len(numbers):
      addops(new)
   # once at all combinations brackets can be added
   else:
       new = countops(new)
       print('final')
       for k in range(len(new)):
           new[k] += '=' + str(eval(new[k]))
       print(new)
   return new

#makes a list of ops for adding brackets then activated the addbracket function and where they are in the question
def countops(final):
   new = []
   for qs in final:
       opslist = []
       l = len(qs)
       for k in range(l):
           if qs[k] in actops:
               opslist += [k,qs[k]]
       # adds end condtions for the add brack function
       opslist += [l,-1,0]
       #print (opslist)
       new += (addbrackets(qs,opslist))
   return new

#add bracket only when appropriate
def addbrackets(qs,opslist):
   k = len(opslist)
   add = ['+','-']
   # if there is only one operation no bracket needed
   if k < 6:
      return [qs]
   # if operations in the same family bracket effect can be done by switching operation or has no effect
   elif sameoptest(opslist):
      return [qs]
   else:
      for n in range(k):
         # only adds brackets around + or - as they are after others
         if (opslist[n] in add):
             new = [qs]
             # error check for zero so you can't divide by it
             if eval(qs[opslist[(n-3)]+1:opslist[(n+1)]]) !=0 or opslist[(n-2)] == '*':
                nextqs = qs[0:opslist[(n-3)]+1]+'('+ qs[opslist[(n-3)]+1:opslist[(n+1)]] +')'+ qs[opslist[(n+1)]:]
                i=n
                # add to the placement of the later operation because of the new brackets
                while i<k:
                    opslist[i+1]+=2
                    i+=2
                # deletes this operation from the list that might need brackets round
                del opslist [n-1:n+1]
                # corrects end part of opslist
                opslist[-3] = len(nextqs)
                # call the function again if more brackets needed
                new += addbrackets(nextqs,opslist)
             return new
            
# when you have nothing but +- or ×÷ test
def sameoptest(opslist):
    startop = opslist[1]
    add = ['+','-']
    times = ['*','/']
    if startop in add:
        for op in opslist:
            if op in times:
               return 0
        return 1
    else:
        for op in opslist:
            if op in add:
               return 0
        return 1
      
#starts program
start(input('starting numbers   : '))

