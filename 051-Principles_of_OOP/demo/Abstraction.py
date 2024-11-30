class ATM():
    def __init__(self):
        # The database holds a list that contains: 1. username 2. money
        self.__database = [["Minerva",5000000],["You",0]]
        self.total_user_count = len(self.__database)
    def return_specific_user(self,user):
        return self.__database[user]


if __name__ == "__main__":
    atm = ATM()
    print(f"Give me my user: {atm.return_specific_user(0)}")
    print(f"Total ATM user count is: {atm.total_user_count}")
    try:
        print(f"I am a hacker, give me your database! {atm.__database}")
    except Exception as e:
        print(f"Oops, got caught. Gotta book it. \n{e}")
    
