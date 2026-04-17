class Workspace:
    def __init__(self,workspace_name):
        self.workspace_name=workspace_name
   
class company(Workspace):
    def __init__(self, workspace_name,company_name):
        super().__init__(workspace_name)
        self.company_name=company_name
    
class process(company):
    def __init__(self,workspace_name,company_name,process_name):
        super().__init__(workspace_name,company_name)
        self.process_name=process_name
    
class employee(process):
   
    def __init__(self,Name,Id,process_name,company_name,workspace_name):
        super().__init__(workspace_name,company_name,process_name)
        self.Name=Name
        self.Id=Id
    def display_employee(self):
                   
       print(f"Name:{self.Name} ID:{self.Id} Process:{self.process_name} Company:{self.company_name} Workspace:{self.workspace_name}")              

#creating an objet of process class
Employee1=employee("Rudransh",620710,"AT&T","Sutherland","Mindspace")
Employee2=employee("Pankaj",315280,"AT&T","Sutherland","Mindspace")


Employee1.display_employee()
Employee2.display_employee()


