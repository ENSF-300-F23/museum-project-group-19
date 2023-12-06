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

def delete_user(user_name):
    cur.execute("DROP USER IF EXISTS %(username)s@localhost", {"username": user_name})
    cnx.commit()
    print("User deleted:", user_name)

def suspend_user(user_name):
    cur.execute("ALTER USER %(username)s@localhost ACCOUNT LOCK", {"username": user_name})
    cnx.commit()
    print("User suspended:", user_name)

def activate_user(user_name):
    cur.execute("ALTER USER %(username)s@localhost ACCOUNT UNLOCK", {"username": user_name})
    cnx.commit()
    print("User activated:", user_name)

def data_entry():

    running = True
    while(running):
      print("Data Entry Console: ")
      print("1- Add new Art Piece")
      print("2- Add new Artist")
      print("3- Add new Exhibition")
      print("4- Add new Collection")
      print("5- Museum View")
      print("9- Exit")
      selection = input()
      if selection == '1':
          add_art_piece()
      elif selection == '2':
          add_artist()
      elif selection == '3':
          add_exhibition()
      elif selection == '4':
          add_gallery_collection()
      elif selection == '5':
          museum_view()
      elif selection == '9':
          running = False
      else:
          print("Invalid selection")

def add_art_piece():
    print("Enter the following information for the new Art Piece:")
    while(True):
        art_id = int(input("Art Piece ID: "))
        if art_id != '' and check_if_exists(art_id, 'art_pieces') == False:
            break
        else:
            print("Invalid Art ID")
    art_exid = string_to_int(input("Art Piece Exhibition ID (press enter and leave blank if unknown): "))
    if(check_if_exists(art_exid, 'EXHIBIT_DETAILS') == False and art_exid != None):
        add_exhibition()
    art_name = input("Art Piece Name: ")
    art_artist = input("Art Piece Artist (press enter and leave blank if unknown): ") or None

    if(check_if_exists(art_artist, 'ARTIST_INFO') == False and art_artist != None):
        add_artist()
    art_year = string_to_int(input("Art Piece Year (press enter and leave blank if unknown): "))
    art_description = input("Art Piece Description (press enter and leave blank if unknown): ") or None
    while(True):
        art_type = input("Art Piece Type(Painting, Sculpture, Other): ")
        if art_type in ['Painting', 'Sculpture', 'Other']:
            break
        else:
            print("Invalid Art Type")
    art_origin = input("Art Piece Origin (press enter and leave blank if unknown): ") or None
    art_epoch = input("Art Piece Epoch (press enter and leave blank if unknown): ") or None
    while(True):
        art_status = input("Art Piece Status (Borrowed or Permanent): ")
        if art_status in ['Borrowed', 'Permanent']:
            break
        else:
            print("Invalid Art Status")
    
    inst_art_template= "insert into art_pieces values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    inst_art_data = (art_id, art_exid, art_name, art_artist, art_year, art_description, art_type, art_origin, art_epoch)
    cur.execute(inst_art_template, inst_art_data)
    cnx.commit()

    if art_type == 'Painting':
            add_painting_piece(art_id)
    elif art_type == 'Sculpture':
            add_sculpture(art_id)
    elif art_type == 'Other':
            add_other(art_id)
    
        
    if art_status == 'Borrowed':
            add_borrowed_collection(art_id)
    elif art_status == 'Permanent':
            add_permanent_collection(art_id)
            

def add_painting_piece(art_id):
    print("Enter the following information for the new Painting:")

    paint_type = input("Painting Type: ")
    paint_drawn = input("Painting Drawn On: ")
    paint_style = input("Painting Style (press enter to leave blank if unknown): ") or None

    inst_paint_template = "INSERT INTO paintings VALUES (%s, %s, %s, %s)"
    inst_paint_data = (art_id, paint_type, paint_drawn, paint_style)
    cur.execute(inst_paint_template, inst_paint_data)
    cnx.commit()
    print("Painting added successfully for art ID:", art_id)

def add_sculpture(art_id):
    print("Enter the following information for the new Sculpture:")

    sculpture_material = input("Sculpture Material: ")
    
    
    while True:
        try:
            sculpture_height = int(input("Sculpture Height (cm): "))
            if sculpture_height > 0:
                break
            else:
                print("Please enter a positive integer for height.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for height.")

  
    while True:
        try:
            sculpture_weight = float(input("Sculpture Weight (kg): "))
            if sculpture_weight > 0:
                break
            else:
                print("Please enter a positive float for weight.")
        except ValueError:
            print("Invalid input. Please enter a valid float for weight.")

    sculpture_style = input("Sculpture Style (press enter to leave blank if unknown): ") or None

    inst_sculpture_template = "INSERT INTO sculptures VALUES (%s, %s, %s, %s, %s)"
    inst_sculpture_data = (art_id, sculpture_material, sculpture_height, sculpture_weight, sculpture_style)

    cur.execute(inst_sculpture_template, inst_sculpture_data)
    cnx.commit()

    print("Sculpture added successfully for art ID:", art_id)

def add_other(art_id):
    print("Enter the following information for the new Art Piece:")

    other_type = input("Other Type: ")
    other_style = input("Other Style (press enter to leave blank if unknown): ") or None

    inst_other_template = "INSERT INTO other_art VALUES (%s, %s, %s)"
    inst_other_data = (art_id, other_type, other_style)

    cur.execute(inst_other_template, inst_other_data)
    cnx.commit()

    print("Other type art Piece added successfully for art ID:", art_id)
    
def add_borrowed_collection(art_id):
    print("Enter the following information for the new Borrowed Art Piece:")
    
    
    while True:
        borrowed_collection = input("Borrowed Collection Name: ")
        if borrowed_collection != '' and not check_if_exists(borrowed_collection, 'borrowed_art'):
            break
        else:
            print("Invalid or existing collection name. Please provide a valid and non-existing name.")

    borrowed_date_borrowed = string_to_int(input("Borrowed Date Borrowed: "))
    borrowed_date_returned = string_to_int(input("Borrowed Date Returned (press enter to leave blank if unknown): "))

    inst_borrowed_template = "INSERT INTO borrowed_art VALUES (%s, %s, %s, %s)"
    inst_borrowed_data = (borrowed_collection, art_id, borrowed_date_borrowed, borrowed_date_returned)

    cur.execute(inst_borrowed_template, inst_borrowed_data)
    cnx.commit()

    print("Borrowed art Piece added successfully for art ID:", art_id)

def add_permanent_collection(art_id):
    print("Enter the following information for the new Permanent Art Piece:")

    Permanent_date_acquired = string_to_int(input("Permanent Year Acquired: "))
    Permanent_status = input("Permanent Status (press enter and leave blank if unknown): ") or None
    Permanent_cost = string_to_int(input("Permanent Cost (press enter and leave blank if unknown): "))

    inst_Permanent_template= "insert into Permanent_Collections values (%s,%s,%s,%s)"
    inst_Permanent_data = (art_id, Permanent_date_acquired, Permanent_status, Permanent_cost)

    cur.execute(inst_Permanent_template, inst_Permanent_data)
    cnx.commit()

def add_artist():
    print("Enter the following information for the new Artist:")
    while(True):
        artist_name = input("Artist Name: ")
        if artist_name != '' and check_if_exists(artist_name, 'artist_info') == False:
            break
        else:
            print("Invalid Artist Name")
    artist_born = string_to_int(input("Artist Date Born (press enter and leave blank if unknown): "))
    artist_died = string_to_int(input("Artist Date Died (press enter and leave blank if unknown): "))
    artist_country = input("Artist Country of Origin (press enter and leave blank if unknown): ") or None
    artist_epoch = input("Artist Epoch (press enter and leave blank if unknown): ") or None
    artist_style = input("Artist Main Style (press enter and leave blank if unknown): ") or None
    artist_description = input("Artist Description (press enter and leave blank if unknown): ") or None

    inst_artist_template= "insert into artist_info values (%s,%s,%s,%s,%s,%s,%s)"
    inst_artist_data = (artist_name,artist_born,artist_died,artist_country,artist_epoch,artist_style,artist_description)
    
    cur.execute(inst_artist_template, inst_artist_data)
    cnx.commit()



def add_exhibition():
    print("Enter the following information for the new Exhibition:")
    while(True):
        ex_id = string_to_int(input("Exhibition ID: "))
        if ex_id != None and check_if_exists(ex_id, 'exhibit_details') == False:
            break
        else:
            print("Invalid Exhibition ID")

    ex_name = input("Exhibition Name: ")
    ex_start = input("Exhibition Start Date (YYYY-MM-DD): ")
    ex_end = input("Exhibition End Date (YYYY-MM-DD): ")

    inst_ex_template= "insert into exhibit_details values (%s,%s,%s,%s)"
    inst_ex_data = (ex_id,ex_name,ex_start,ex_end)
    
    cur.execute(inst_ex_template, inst_ex_data)
    cnx.commit()


def add_gallery_collection():
    print("Enter the following information for the new Collection:")
    
    while True:
        collection_name = input("Collection Name: ")
        if collection_name != '' and not check_if_exists(collection_name, 'gallery_collections'):
            break
        else:
            print("Invalid Collection Name")

    collection_type = input("Collection Type: ")
    collection_description = input("Collection Description: ")
    collection_address = input("Collection Address: ")
    collection_phone = input("Collection Phone: ")
    collection_contact = input("Collection Contact: ")

    inst_collection_template = "INSERT INTO gallery_collections VALUES (%s, %s, %s, %s, %s, %s)"
    inst_collection_data = (collection_name, collection_type, collection_description, collection_address, collection_phone, collection_contact)

    cur.execute(inst_collection_template, inst_collection_data)
    cnx.commit()

    print("Collection added successfully:", collection_name)

def check_if_exists(id, table):
    if table == 'art_pieces':
        cur.execute("select ID_no from art_pieces")
        search_result=cur.fetchall()
        for row in search_result:
            if id == row[0]:
                return True
        return False

    elif table == 'artist_info':
        cur.execute("select artist_name from artist_info")
        search_result=cur.fetchall()
        for row in search_result:
            if id == row[0]:
                return True
        return False

    elif table == 'exhibit_details':
        cur.execute("select Exhibit_Id from exhibit_details")
        search_result=cur.fetchall()
        for row in search_result:
            if id == row[0]:
                return True
        return False
        
    elif table == 'gallery_collections':
        cur.execute("select collection_name from gallery_collections")
        search_result=cur.fetchall()
        for row in search_result:
            if id == row[0]:
                return True
        return False
    
    
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