

def generate_specifications(analysis):
    
    modules = generate_modules(analysis)
    schemas = generate_schemas(analysis)
    pseudocode = generate_pseudocode(analysis)
    
  
    return {
        "modules": modules,
        "schemas": schemas,
        "pseudocode": pseudocode
    }

def generate_modules(analysis):
    modules = []
    
    modules.append({
        "name": "UserModule",
        "description": "Handles user authentication and profile management",
        "functions": ["login", "logout", "resetPassword", "updateProfile"]
    })
    
    modules.append({
        "name": "DatabaseModule",
        "description": "Manages database connections and operations",
        "functions": ["connect", "disconnect", "executeQuery", "beginTransaction"]
    })
    
    for area in analysis["functional_areas"]:
       
        parts = area.split(" ", 1)
        action = parts[0]
        
        if len(parts) > 1:
            target = parts[1]
          
            module_name = target.capitalize() + "Manager"
            
          
            functions = []
          
            functions.append(action + target.capitalize())
            functions.append("get" + target.capitalize())
            functions.append("update" + target.capitalize())
            functions.append("delete" + target.capitalize())
            
           
            modules.append({
                "name": module_name,
                "description": f"Handles operations related to {target}",
                "functions": functions
            })
    
    return modules

def generate_schemas(analysis):
    
    schemas = []
    
   
    for entity in analysis["entities"]:
        
        if entity in ["system", "application", "page", "screen"]:
            continue
       
        fields = [
            {"name": "id", "type": "INTEGER", "description": "Unique identifier"},
            {"name": "created_at", "type": "DATETIME", "description": "Creation timestamp"}
        ]
        
        
        if entity in ["user", "customer", "admin"]:
          
            fields.extend([
                {"name": "name", "type": "VARCHAR(100)", "description": "User's full name"},
                {"name": "email", "type": "VARCHAR(100)", "description": "User's email address"},
                {"name": "password", "type": "VARCHAR(255)", "description": "Encrypted password"}
            ])
        elif entity in ["product", "item"]:
            
            fields.extend([
                {"name": "name", "type": "VARCHAR(100)", "description": "Product name"},
                {"name": "description", "type": "TEXT", "description": "Product description"},
                {"name": "price", "type": "DECIMAL(10,2)", "description": "Product price"}
            ])
        elif entity in ["order", "transaction"]:
            
            fields.extend([
                {"name": "user_id", "type": "INTEGER", "description": "Reference to user"},
                {"name": "total", "type": "DECIMAL(10,2)", "description": "Order total amount"},
                {"name": "status", "type": "VARCHAR(50)", "description": "Order status"}
            ])
        else:
            
            fields.extend([
                {"name": "name", "type": "VARCHAR(100)", "description": "Name"},
                {"name": "description", "type": "TEXT", "description": "Description"},
                {"name": "active", "type": "BOOLEAN", "description": "Whether it's active"}
            ])
        
    
        schemas.append({
            "table_name": entity,
            "fields": fields
        })
    
    return schemas

def generate_pseudocode(analysis):
  
    pseudocode = {}
    
   
    for entity in analysis["entities"]:
        
        if entity in ["system", "application", "page", "screen"]:
            continue
        
     
        entity_name = entity.capitalize()
        
     
        create_code = f"""
function create{entity_name}(data):
 
    if not isValid(data):
        return error("Invalid data")
   
    newRecord = {{
        "name": data.name,
        "created_at": getCurrentTime()
    }}
    
    id = database.insert("{entity}", newRecord)
    
    return {{ "id": id, "success": true }}
"""
        
        # Read function
        read_code = f"""
function get{entity_name}(id):
    
    record = database.findById("{entity}", id)
    
   
    if record is null:
        return error("Not found")
   
    return record
"""
        
        # Add functions to pseudocode
        pseudocode[f"create{entity_name}"] = create_code
        pseudocode[f"get{entity_name}"] = read_code
    
    return pseudocode