import os 
  
# Function to rename multiple files 
def main(): 
    i = 609
      
    for filename in os.listdir("NoHelmet"): 
        dst = str(i) + ".jpg"
        src = 'NoHelmet/'+ filename 
        dst ='NoHelmet/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()