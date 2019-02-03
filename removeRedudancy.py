givenstr = """"So Alexander led his troops down the Indus River and was severely wounded during a battle with the Malli.
In early 324 B.C., Alexander reached the city of Susa in Persia.
The Macedonian army resented Alexander’s attempt to change their culture and many mutinied.
But after Alexander took a firm stand and replaced Macedonian officers and troops with Persians, his army backed down.
After surviving battle after fierce battle, Alexander the Great died in June 323 B.C. at age 32.
Nonetheless, many conquered lands retained the Greek influence Alexander introduced—some cities he founded remain important cultural centers even today—and Alexander the Great is revered as one of the most powerful and influential leaders the ancient world ever produced.
Alexander the Great.
Alexander the Great.
Alexander the Great of Macedon Biography.
Alexander of Macedonia."""

def findall(inpstr, sub):
    ptr = 0
    indexlist = []
    while ptr < len(inpstr)-1:
        index = inpstr.find(sub, ptr, len(inpstr)-1)
        if index == -1:
            return indexlist
        indexlist.append(index)
        ptr = index+1
    return indexlist

def removeString(inpstr, index, remove):
    newstr = inpstr[0:index]
    newstr2 = inpstr[index+remove-1:]
    return newstr+" "+newstr2

def removeRedundancy(givenstr):
    indexlist = findall(givenstr, "\n")
    for ind in indexlist[::-1]:
        givenstr = removeString(givenstr, ind, 2)
    periodIndex = findall(givenstr, ".")

    for i in range(len(periodIndex)-2):
        if periodIndex[i+1]-periodIndex[i] == periodIndex[i+2]-periodIndex[i+1]:
            if givenstr[periodIndex[i]] == givenstr[periodIndex[i+1]]:
                givenstr = removeString(givenstr, periodIndex[i], periodIndex[i + 1] - periodIndex[i])
    return givenstr

