import mysql.connector
from tabulate import tabulate
def admin_consol():

    running = True
    while(running):
      print("Admin Console: ")
      print("1- Enter SQL Commands")
      print("2- Provide path to SQL file")
      print("3- User Management")
      print("4- Data Entry")
      print("5- View Museum Data")
      print("9- Exit")

      selection = input()

      if selection == '1':
          print("Enter your SQL Command Type:")
          print("1- Select Query")
          print("2- Anything Else")
          sql_selection = input()
          if sql_selection == '1':
                sql_command = input("Enter your SQL command(SELECT): ")
                cur.execute(sql_command)
                print_tables(cur)
          else:
                sql_command = input("Enter your SQL command(NO SELECT): ")
                cur.execute(sql_command)
                cnx.commit()

      elif selection == '2':
          path = input("Enter the path to your SQL file(NO SELECT QUERIES): ")
          fd = open(path, 'r')
          sqlFile = fd.read()
          fd.close()
          sqlCommands = sqlFile.split(';')
          print(sqlCommands)

          for command in sqlCommands:
              try:
                  if command.strip() != '':
                      cur.execute(command)
              except (IOError):
                  print("Command skipped: ")
          cnx.commit()

      elif selection == '3':
          user_management()
      elif selection == '4':
          data_entry()
      elif selection == '5':
          museum_view()
      elif selection == '9':
          running = False
      else:
          print("Invalid selection")

def user_management():
    running = True
    while(running):  
        print("User Management Console: ")

        print("1- Add new User")
        print("2- Access Control")
        print("3- Manage User")
        print("9- Exit")

        selection = input()

        if selection == '1':
            add_user()
        elif selection == '2':
            access_control()
        elif selection == '3':
            manage_user()
        elif selection == '9':
            running = False
        else:
            print("Invalid selection")



def add_user():
    print("Enter the following information for the new User:")
    user_name = input("User Name: ")
    user_password = input("User Password: ")
    
    if user_name and user_password:
        cur.execute("DROP USER IF EXISTS %(username)s@localhost", {"username": user_name})
        cur.execute("CREATE USER %(username)s@localhost IDENTIFIED WITH mysql_native_password BY %(password)s", {"username": user_name, "password": user_password})
        cur.execute("GRANT db_admin@localhost TO %(username)s@localhost", {"username": user_name})
        cur.execute("SET DEFAULT ROLE ALL TO %(username)s@localhost", {"username": user_name})
        cnx.commit()
        print("User added successfully:", user_name)
    else:
        print("Invalid User Name or Password")

def access_control():
    print("Enter the following information for the User:")
    user_name = input("User Name: ")

    if user_name:
        print("1- Revoke Access")
        print("2- Grant Access")
        selection = input("Enter your choice: ")

        if selection == '1':
            revoke_access(user_name)
        elif selection == '2':
            grant_access(user_name)
        else:
            print("Invalid selection")

def revoke_access(user_name):
    cur.execute("REVOKE ALL PRIVILEGES, GRANT OPTION FROM %(username)s@localhost", {"username": user_name})
    cnx.commit()
    print("Access revoked for user:", user_name)

def grant_access(user_name):
    cur.execute("GRANT db_admin@localhost TO %(username)s@localhost", {"username": user_name})
    cur.execute("SET DEFAULT ROLE ALL TO %(username)s@localhost", {"username": user_name})
    cnx.commit()
    print("Access granted for user:", user_name)

def manage_user():
    print("Enter the following information for the User:")
    user_name = input("User Name: ")

    if user_name:
        print("1- Delete User")
        print("2- Suspend User")
        print("3- Activate User")
        selection = input("Enter your choice: ")

        if selection == '1':
            delete_user(user_name)
        elif selection == '2':
            suspend_user(user_name)
        elif selection == '3':
            activate_user(user_name)
        else:
            print("Invalid selection")


    
def string_to_int(string):
    try:
        return int(string)
    except ValueError:
        return None
if __name__ == "__main__":
    
   
    print("Museum Database:")
    print("In order to proceed select your role from the list below:")
    print("1-DB Admin")
    print("2-Data Entry")
    print("3-Browse as guest")

    selection = input("type 1, 2, or 3 to select your role: ")

    if selection in ['1','2']:
        username= input("user name: ")
        passcode= input("password: ")
    else:
        username="guest"
        passcode="Guest123!"


    
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user=username,
        password= passcode)    

    cur = cnx.cursor()
 
    cur.execute("use museum;")


    if selection == '1':
        admin_consol()
    elif selection == '2':
        data_entry()
    else:
        museum_view()   
    
    
    cnx.close()