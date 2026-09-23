#Contetxt Managers

class DatabaseConnection:
    def __init__(self,connection: str) -> None:
        self.connection = connection
    
    def __enter__(self) -> "DatabaseConnection":
        print(f"Connecting to database : {self.connection}")
        return self
    
    def execute(self, query: str) -> None:
        print(f"Executing query: {query}")
    
    def __exit__(self, exc_type, exc_value, traceback) -> bool:        
        print("Closing database connection")
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__} - {exc_value}")
        return False

with DatabaseConnection("postgresql://localhost/mydb") as db:
    db.execute("SELECT * FROM users")
with DatabaseConnection("postgresql://localhost/mydb") as db:
    db.execute("SELECT * FROM users")
    raise ValueError("Something went wrong")