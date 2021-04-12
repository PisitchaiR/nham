def main():
    for i in range(1, 6):
        score = int(input())
        if score >= 80:
            print ("นักเรียนคนที่"+  str(i)+ ": A")
        elif score >= 70:
            print ("นักเรียนคนที่"+  str(i)+ ": B")
        elif score >= 60:
            print ("นักเรียนคนที่"+  str(i)+ ": C")
        elif score >= 50:
            print ("นักเรียนคนที่"+  str(i)+ ": D")
        else:
            print ("นักเรียนคนที่"+  str(i)+ ": F")


main()
