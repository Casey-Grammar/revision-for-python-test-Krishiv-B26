# Task 9 Cat problem
# You've collected too many cats. Write a program to count how
# many cats you have by reading in their names. All your cats only
# have first names, with no spaces.

def main():
    #Write your code here
    list_of_cats_names = input("Cats: ")
    list_of_cats_names = list_of_cats_names.split()
    print("You have " + str(len(list_of_cats_names)) + " cats.")
     



    # End of your code here





if __name__ == '__main__':
    main()