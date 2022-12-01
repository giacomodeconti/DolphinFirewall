def delPolicy():
      import os
      from nameCheck import nameCheck
      from seekRule import seekRule

      # input for delete policy
      respond = input("Do you want to delete an Input or Output rule? (I/O) >>> ")
      string_input=input("\nInsert name of Policy to delete:\n")

      # file finder by input
      if respond == "I":
         file_chosen = "InBound.txt"

      elif respond == "O":
         file_chosen = "OutBound.txt"

      # call nameCheck function
      occurrencies = nameCheck(string_input,file_chosen)

      print("There are files that have the same name, which one do you want to delete?")
      for idx,name in enumerate(occurrencies):
         print(f" {idx + 1} >>> {name}")
      
      del_rule = int(input("Which rule do you want to delete?"))
      
      with open(file_chosen, "r") as inputd:
         with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in inputd:
                  rule = line.split(" ")
                  # if substring contain in a line then don't write it
                  if occurrencies[del_rule-1] != rule[0]:
                     output.write(line)

      rule_properties = seekRule(occurrencies[del_rule-1], file_chosen)
      
      if respond == "I":
         os.system(f"sudo iptables -D INPUT -s {rule_properties[1]} -j {rule_properties[4]}")
      elif respond == "O":
         os.system(f"sudo iptables -D OUTPUT -s {rule_properties[1]} -j {rule_properties[4]}")
      
      print('POLICY Deleted')

      # replace file with original name
      os.replace('temp.txt', file_chosen)