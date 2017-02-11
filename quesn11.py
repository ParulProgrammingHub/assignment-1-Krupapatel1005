#WRITE A PROGRAM TO ENTER PRINCIPAL AMOUNT, TIME AND INTEREST RATE. CREATE COMPOUND_INTEREST(PRINCIPAL,TIME,RATE) FUNCTION TO CALCULATE COMPOUND INTEREST.
P1=int(input("ENTER THE PRINCIPAL AMOUNT"))
T1=int(input("ENTER THE TIME"))
I1=int(input("ENTER THE INTEREST RATE"))
def compound_interest(P,T,I):
    i=1
    CI=0
    while(i<=T):
        C=P*I/100
        P=P+C
        CI=CI+C
        i =i+1
    print("COMPOUND INTEREST:",CI)
C1=compound_interest(P1,T1,I1)
