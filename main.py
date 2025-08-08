import mysql.connector
import tkinter as tk

def executeQuery(dataBase, cursorObject, actionInput, entityInput, params):
    # Generate query
    query = ""
    match actionInput:
        case "1": # Create new entry
            query += "INSERT INTO "
            match entityInput:
                case "1": # Location
                    query += "Locations (loc_name, loc_street, loc_city, loc_state, loc_zip) "
                case "2": # Employee
                    query += "Employees (emp_name, emp_street, emp_city, emp_state, emp_zip, emp_payrate, emp_payperiod, emp_location) "
                case "3": # Product
                    query += "Products (prod_name, prod_manufacturer, prod_msrp) "
            query += "VALUES ("
            for i in range(len(params) - 1):
                query += f"{params[i]}, "
            query += f"{params[-1]})"
        case "2": # View name of existing entry
            query += "SELECT "
            match entityInput:
                case "1": # Location
                    query += "loc_name FROM Locations WHERE loc_id = "
                case "2": # Employee
                    query += "emp_name FROM Employees WHERE emp_id = "
                case "3": # Product
                    query += "prod_name FROM Products WHERE prod_id = "
            query += params[0]
        case "3": # Delete existing entry
            query += "DELETE FROM "
            match entityInput:
                case "1": # Location
                    query += "Locations WHERE loc_id = "
                case "2": # Employee
                    query += "Employees WHERE emp_id = "
                case "3": # Product
                    query += "Products WHERE prod_id = "
            query += params[0]
    
    # Execute query
    try:
        cursorObject.execute(query)
        if actionInput in ["1", "3"]:
            dataBase.commit()
    except Exception as e:
        return f"An error occurred! Details: {e}"
    
    # Process results
    match actionInput:
        case "1":
            return "Insertion successful!"
        case "2":
            ret = cursorObject.fetchall()
            return f"Name: {ret[0][0]}"
        case "3":
            return "Deletion successful!"

if __name__ == "__main__":
    # Connect to database
    dataBase = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "password",
        database = "DBFinalProject"
    )
    cursorObject = dataBase.cursor(buffered=True)

    # Start main loop
    cont = True
    while cont:
        # Get intended action
        actionInput = input("What action would you like to perform?\n1. Create new entry\n2. View name of existing entry\n3. Delete existing entry\nInput: ")
        if actionInput not in ['1', '2', '3']:
            print("Invalid input! Terminating program.")
            break

        entityInput = input("\nOk! What entity would you like to perform that action on?\n1. Location\n2. Employee\n3. Product\nInput: ")
        if entityInput not in ['1', '2', '3']:
            print("Invalid input! Terminating program.")
            break

        # Get params
        params = []
        print("")
        match actionInput:
            case "1": # Create new entry
                match entityInput:
                    case "1": # Location
                        name = "\'" + input("Please enter the name of the new location: ") + "\'"
                        street = "\'" + input("Please enter the street address of the new location: ") + "\'"
                        city = "\'" + input("Please enter the city of the new location: ") + "\'"
                        state = "\'" + input("Please enter the state of the new location: ") + "\'"
                        zip = input("Please enter the zip code of the new location: ")
                        params = [name, street, city, state, zip]
                    case "2": # Employee
                        name = "\'" + input("Please enter the name of the new employee: ") + "\'"
                        street = "\'" + input("Please enter the street address of the new employee: ") + "\'"
                        city = "\'" + input("Please enter the city of the new employee: ") + "\'"
                        state = "\'" + input("Please enter the state of the new employee: ") + "\'"
                        zip = input("Please enter the zip code of the new employee: ")
                        payrate = input("Please enter the payrate of the new employee: ")
                        payperiod = "\'" + input("Please enter the pay period of the new employee: ") + "\'"
                        location = input("Please enter the location id where the new employee works: ")
                        params = [name, street, city, state, zip, payrate, payperiod, location]
                    case "3": # Product
                        name = "\'" + input("Please enter the name of the new product: ") + "\'"
                        manufacturer = "\'" + input("Please enter the manufacturer of the new product: ") + "\'"
                        msrp = input("Please enter the MSRP of the new product: ")
                        params = [name, manufacturer, msrp]
                print("")
            case "2": # View existing entry
                id = input("Please enter the ID of the entry to view: ")
                params = [id]
            case "3": # Delete existing entry
                id = ""
                if entityInput == "3":
                    deleteProductGUI = tk.Tk()
                    deleteProductGUI.title("Delete Product")
                    tk.Label(deleteProductGUI, text='ID: ').grid(row=0, column=0)
                    userInput = tk.StringVar()
                    entryBox = tk.Entry(deleteProductGUI, textvariable=userInput)
                    entryBox.grid(row=0, column=1)
                    def getID():
                        global id
                        id = userInput.get()
                        deleteProductGUI.destroy()
                    enterButton = tk.Button(deleteProductGUI, text="Submit", command=getID)
                    enterButton.grid(row=0, column=2)
                    deleteProductGUI.mainloop()
                else:
                    id = input("Please enter the ID of the entry to delete: ")
                params = [id]

        # Calculate and display results
        ret = executeQuery(dataBase, cursorObject, actionInput, entityInput, params)
        print(ret)

        # Allow users to end the program
        contInput = input("\nWould you like to continue?\n1. Yes\n2. No\nInput: ")
        match contInput:
            case '1':
                print("")
                pass
            case '2':
                print("See you next time!")
                cont = False
            case _:
                print("Invalid input! Terminating program.")
                cont = False

    dataBase.close()