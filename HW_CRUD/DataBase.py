class Database(object):
    user = []

    def add_user(self, new_user):
        # print(new_user.email, "add email")
        if len(self.user) > 0:
            flag = False
            for item in self.user:
                # print(item.email, "$")
                if new_user.email == item.email:
                    # print("test")
                    flag = True
            # print(flag)
            if flag is False:
                print("User added")
                self.user.append(new_user)
            else:
                print("User already exist")

        else:
            # print("#")
            print("User added")
            self.user.append(new_user)

    def show_database(self):
        for item in self.user:
            print("Element #", self.find_user_by_email(item.email))

    def find_user_by_email(self, find_email):
        for item in self.user:
            if find_email == item.email:
                return self.user.index(item), item.email, item.name, item.password, item.phone

    def remove_user_by_email(self, find_email):
        flag = True
        for item in self.user:
            if find_email == item.email:
                self.user.remove(item)
                flag = False
        if flag is True:
            print("User not exist")

    def find_user_by_index(self, index):
        return index, self.user[index].email, self.user[index].name, self.user[index].password, self.user[index].phone

    def remove_user_by_index(self, index):
        if index > len(self.user)-1:
            print("User not exist")
        else:
            self.user.pop(index)
