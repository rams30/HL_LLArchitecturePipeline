def analyze_requirements(text):
    
    functional_areas = extract_functional_areas(text)
    entities = extract_entities(text)
    business_rules = extract_business_rules(text)
    
   
    return {
        "functional_areas": functional_areas,
        "entities": entities,
        "business_rules": business_rules
    }

def extract_functional_areas(text):
  
    text = text.lower()
    
   
    areas = []
    
   
    action_words = ["create", "manage", "update", "delete", "view", 
                   "search", "generate", "process", "add", "edit", "remove"]
    
   
    sentences = text.split('.')
    
 
    for sentence in sentences:
        for action in action_words:
          
            if action in sentence:
                
                parts = sentence.split(action)
                if len(parts) > 1:
                    
                    next_words = parts[1].strip().split()[:4]
                    
                    target = " ".join(next_words)
                    
                    target = target.replace(',', '').replace('and', '').strip()
                   
                    areas.append(f"{action} {target}")
    
    return list(set(areas))

def extract_entities(text):
    
    text = text.lower()
    entities = []
    indicators = ["user", "customer", "admin", "product", "order", "account", 
                 "profile", "report", "notification", "payment", "item"]
    
    for entity in indicators:
        if entity in text:
            entities.append(entity)
    
    
    words = text.split()
    for i in range(len(words) - 1):
        if words[i] in ["the", "a", "an"] and len(words[i+1]) > 3:
            if words[i+1] not in ["system", "user", "should", "must", "will", "can"]:
                entities.append(words[i+1])
    
    return list(set(entities))

def extract_business_rules(text):
  
    text = text.lower()
    
    rules = []
    sentences = text.split('.')
    rule_keywords = ["must", "should", "required", "needs to", "have to"]
    
    for sentence in sentences:
        for keyword in rule_keywords:
            if keyword in sentence:
                
                rule = sentence.strip()
                if rule:  
                    rules.append(rule)
                break  
    
    return rules