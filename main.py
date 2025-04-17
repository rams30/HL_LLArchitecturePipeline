import os
import json
from analyzer import analyze_requirements
from generator import generate_specifications

def main():
    print("\nEnter your business requirements below (press Enter twice when done):")
    
  
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    
    
    requirements_text = "\n".join(lines)
    
   
    if not requirements_text.strip():
        print("No requirements provided.")
        return
    
    print("\nProcessing requirements")
 
    analysis = analyze_requirements(requirements_text)
  
    print(f"Found {len(analysis['functional_areas'])} functional areas:")
    for area in analysis['functional_areas']:
        print(f"  - {area}")
    
    print(f"\nFound {len(analysis['entities'])} entities:")
    for entity in analysis['entities']:
        print(f"  - {entity}")
    
    print(f"\nFound {len(analysis['business_rules'])} business rules")
    

    specs = generate_specifications(analysis)
    
    specs["original_requirements"] = requirements_text
    
    
    if not os.path.exists("output"):
        os.makedirs("output")
 
    output_file = "output/technical_specs.json"
    with open(output_file, 'w') as f:
        json.dump(specs, f, indent=2)
    
    print(f"\nSpecifications saved to {output_file}")
    
    
    print("\n===== Summary =====")
    print(f"Generated {len(specs['modules'])} modules")
    print(f"Generated {len(specs['schemas'])} database schemas")
    print(f"Generated {len(specs['pseudocode'])} pseudocode functions")
    print("\nGlad to help you!")

if __name__ == "__main__":
    main()