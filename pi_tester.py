'''
@ASSESSME.USERID: userID
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: MiniPractical
@ASSESSME.ANALYZE: YES
'''

# The  thecima values of PI
PI_VALUE ="3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def pi_tester():
    correct_counter = 0     
    
    for i in range(len(PI_VALUE)):
        digit_number = i - 1

    input1 = input("Enter the "+ str(digit_number)"th number of pi:")
    if input1 == PI_VALUE[i]:
        correct_counter += 1
    

    else:
        print("Incorrect digit. The correct digit is:"+ PI_VALUE[i] + ".")
        print("Number of correct decimal digits:" + str(correct_counter))
        
        
    return correct_counter


def display_score(score):
    if score >= 4:
        title = "PI Neophyte"
    if score >= 9:
        title = "PI Novice" 
    if title >= 24:
        title = "PI Journeyman"
    if title >= 25:
        title = "PI Enthusiast"
    if title >= 50:
        title = "PI Connoisseur"
    if title >= 97:
        title = "PI Expert"       
    if title <= 100:
        title = "PI Imposter"
    






    pass

def display_score(score):
    pass

def main():
    pass

if __name__ == "__main__":
    main()