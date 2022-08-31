nextprod = set()

def leftrecur(k,prod,lr) :
    for i in range(len(prod)):
        # to get the production which isn't left recursive
        if(k[0]!=prod[i][0]):

            # to add the new non-terminal with the productions which aren't left recursive
            nextprod.add(prod[i][0:]+k[0]+"'")

            # to define the new non-terminal
            new = prod[lr][1:]+k[0]+"'"

    # printing the new non-terminal production
    print(k[0] + "'->" + new + "/E")


prod=input("\nEnter the production: ")

k = prod.split("->")
r = k[1].split("/")

print("\nLeft eliminated grammar :- \n")

# to loop through the productions on the right side
for i in range(len(r)):

    # to find the production with left recursion
    if(k[0] == r[i][0]):
        leftrecur(k, r, i)

# to display the production which appends the new non-terminal with the production which isn't
# left recursive
for i in nextprod:
    print(k[0] + "->" + i)
