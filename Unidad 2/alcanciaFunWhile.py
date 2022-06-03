def main():
    print("Alcancia Digital")
    
    objetivo= float(input("¿Cuanto desea ahorrar?: "))
    
    ahorrado=0.0  
    while objetivo >=ahorrado:
        ahorrado += float(input("¿Cuanto desea depositar?: "))
        
    print(f"Has cumplido tu objetivo, has ahorrado: ${ahorrado}") 
    print(f"te ha sobrado ${ahorrado-objetivo}")
    

if __name__== "__main__":
    main()